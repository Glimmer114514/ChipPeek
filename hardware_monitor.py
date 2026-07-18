import psutil
import time
import threading
import ctypes
import sys
import os

try:
    import clr
    HAS_PYTHONNET = True
except ImportError:
    HAS_PYTHONNET = False

try:
    import pynvml
    HAS_NVML = True
except ImportError:
    HAS_NVML = False


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def get_resource_dir():
    """获取资源文件目录，兼容PyInstaller onefile模式"""
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


def get_config_dir():
    """获取配置文件目录（与EXE同目录）"""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


class HardwareMonitor:
    def __init__(self, sampling_interval_ms=500):
        self._lock = threading.Lock()
        self._sampling_interval = sampling_interval_ms / 1000.0
        self._data = {
            'cpu_freq': 0.0,
            'cpu_temp': 0.0,
            'cpu_usage': 0.0,
            'gpu_freq': 0.0,
            'gpu_temp': 0.0,
            'gpu_usage': 0.0,
            'vram_used': 0.0,
            'vram_total': 0.0,
            'mem_used': 0.0,
            'mem_total': 0.0,
        }
        self._computer = None
        self._running = False
        self._thread = None
        self._is_admin = is_admin()
        self._has_lhm = False

    def set_sampling_interval(self, ms):
        self._sampling_interval = ms / 1000.0

    def start(self):
        if self._running:
            return
        self._init_lhm()
        self._running = True
        self._sample()
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=2)
        self._shutdown_lhm()

    def _init_lhm(self):
        if not HAS_PYTHONNET:
            return

        resource_dir = get_resource_dir()
        dll_path = os.path.join(resource_dir, 'libs', 'lhm', 'lib', 'net472', 'LibreHardwareMonitorLib.dll')
        if not os.path.exists(dll_path):
            return

        try:
            sys.path.insert(0, os.path.dirname(dll_path))
            clr.AddReference(dll_path)
            from LibreHardwareMonitor.Hardware import Computer
            self._computer = Computer()
            self._computer.IsCpuEnabled = True
            self._computer.IsGpuEnabled = True
            self._computer.IsMemoryEnabled = True
            self._computer.Open()
            self._has_lhm = True
        except Exception:
            self._computer = None
            self._has_lhm = False

    def _shutdown_lhm(self):
        if self._computer:
            try:
                self._computer.Close()
            except Exception:
                pass
            self._computer = None

    def _loop(self):
        while self._running:
            self._sample()
            time.sleep(self._sampling_interval)

    def _sample(self):
        data = {}
        self._sample_cpu(data)
        self._sample_memory(data)
        self._sample_gpu(data)
        with self._lock:
            self._data.update(data)

    def _sample_cpu(self, data):
        try:
            data['cpu_usage'] = psutil.cpu_percent(interval=None)
        except Exception:
            data['cpu_usage'] = 0.0

        cpu_freq = 0.0
        cpu_temp = 0.0

        if self._has_lhm and self._computer:
            try:
                from LibreHardwareMonitor.Hardware import HardwareType
                for hw in self._computer.Hardware:
                    if str(hw.HardwareType) == 'Cpu':
                        hw.Update()
                        freqs = []
                        package_temp = 0.0
                        core_temps = []
                        for s in hw.Sensors:
                            st = str(s.SensorType)
                            sname = str(s.Name)
                            if st == 'Clock' and s.Value is not None and 'Bus' not in sname:
                                freqs.append(float(s.Value))
                            elif st == 'Temperature' and s.Value is not None:
                                if 'Package' in sname or 'Tctl' in sname or 'Tdie' in sname:
                                    package_temp = float(s.Value)
                                elif 'Core' in sname and 'TjMax' not in sname:
                                    core_temps.append(float(s.Value))
                        if freqs:
                            # 使用所有核心频率的平均值，与任务管理器显示的"整体频率"一致
                            cpu_freq = sum(freqs) / len(freqs) / 1000.0
                        if package_temp > 0:
                            cpu_temp = package_temp
                        elif core_temps:
                            cpu_temp = max(core_temps)
                        break
            except Exception:
                pass

        if cpu_freq == 0.0:
            try:
                freq = psutil.cpu_freq()
                if freq:
                    cpu_freq = freq.current / 1000.0
            except Exception:
                pass

        data['cpu_freq'] = cpu_freq
        data['cpu_temp'] = cpu_temp

    def _sample_memory(self, data):
        if self._has_lhm and self._computer:
            try:
                from LibreHardwareMonitor.Hardware import HardwareType
                for hw in self._computer.Hardware:
                    if str(hw.HardwareType) == 'Memory':
                        hw.Update()
                        used = 0.0
                        available = 0.0
                        for s in hw.Sensors:
                            if str(s.SensorType) == 'Data' and s.Value is not None:
                                sname = str(s.Name)
                                if 'Virtual' in sname:
                                    continue
                                if 'Used' in sname:
                                    used = float(s.Value)
                                elif 'Available' in sname:
                                    available = float(s.Value)
                        if used > 0 or available > 0:
                            data['mem_used'] = used
                            data['mem_total'] = used + available
                            return
                        break
            except Exception:
                pass

        try:
            mem = psutil.virtual_memory()
            data['mem_total'] = mem.total / (1024 ** 3)
            data['mem_used'] = mem.used / (1024 ** 3)
        except Exception:
            data['mem_total'] = 0.0
            data['mem_used'] = 0.0

    def _sample_gpu(self, data):
        data['gpu_freq'] = 0.0
        data['gpu_temp'] = 0.0
        data['gpu_usage'] = 0.0
        data['vram_used'] = 0.0
        data['vram_total'] = 0.0

        if self._has_lhm and self._computer:
            try:
                from LibreHardwareMonitor.Hardware import HardwareType
                for hw in self._computer.Hardware:
                    ht = str(hw.HardwareType)
                    if 'Gpu' in ht:
                        hw.Update()
                        for s in hw.Sensors:
                            st = str(s.SensorType)
                            sname = str(s.Name)
                            if st == 'Temperature' and s.Value is not None and 'Core' in sname:
                                data['gpu_temp'] = float(s.Value)
                            elif st == 'Clock' and s.Value is not None and 'Core' in sname:
                                data['gpu_freq'] = float(s.Value) / 1000.0
                            elif st == 'Load' and s.Value is not None and 'Core' in sname:
                                data['gpu_usage'] = float(s.Value)
                            elif st == 'SmallData' and s.Value is not None:
                                if 'Total' in sname and 'Memory' in sname:
                                    data['vram_total'] = float(s.Value) / 1024.0
                                elif 'Used' in sname and 'Memory' in sname:
                                    data['vram_used'] = float(s.Value) / 1024.0
                        break
                if data['gpu_temp'] > 0 or data['gpu_freq'] > 0:
                    return
            except Exception:
                pass

        self._sample_gpu_nvml(data)

    def _sample_gpu_nvml(self, data):
        if not HAS_NVML:
            return
        try:
            pynvml.nvmlInit()
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            try:
                data['gpu_temp'] = float(pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU))
            except Exception:
                pass
            try:
                info = pynvml.nvmlDeviceGetMemoryInfo(handle)
                data['vram_total'] = info.total / (1024 ** 3)
                data['vram_used'] = info.used / (1024 ** 3)
            except Exception:
                pass
            try:
                util = pynvml.nvmlDeviceGetUtilizationRates(handle)
                data['gpu_usage'] = float(util.gpu)
            except Exception:
                pass
            try:
                clk = pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_GRAPHICS)
                data['gpu_freq'] = clk / 1000.0
            except Exception:
                pass
            pynvml.nvmlShutdown()
        except Exception:
            pass

    def get_data(self):
        with self._lock:
            return dict(self._data)
