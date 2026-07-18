import tkinter as tk
from tkinter import ttk, Toplevel, Checkbutton, IntVar, StringVar, DoubleVar
import sys
import ctypes
import os
import winreg

try:
    import win32gui
    import win32con
    HAS_WIN32 = True
except ImportError:
    HAS_WIN32 = False


APP_NAME = "ChipPeek"
APP_DISPLAY_NAME = "ChipPeek 硬件监控"
APP_VERSION = "1.0.0"
APP_DEVELOPER = "R41NH4RD"
APP_GITHUB = "https://github.com/Glimmer114514/ChipPeek"
APP_LICENSE = "MIT License"


def set_auto_start(enabled):
    """设置开机自启动（写入注册表 HKCU\\...\\Run）"""
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE,
        )
        if enabled:
            if getattr(sys, 'frozen', False):
                exe_path = sys.executable
                value = f'"{exe_path}"'
            else:
                script = os.path.abspath("main.py")
                value = f'pythonw "{script}"'
            winreg.SetValueEx(key, APP_NAME, 0, winreg.REG_SZ, value)
        else:
            try:
                winreg.DeleteValue(key, APP_NAME)
            except FileNotFoundError:
                pass
        winreg.CloseKey(key)
        return True
    except Exception:
        return False


def get_auto_start():
    """读取当前开机自启动状态"""
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_READ,
        )
        try:
            winreg.QueryValueEx(key, APP_NAME)
            winreg.CloseKey(key)
            return True
        except FileNotFoundError:
            winreg.CloseKey(key)
            return False
    except Exception:
        return False


def get_icon_path():
    """获取图标文件路径，兼容PyInstaller onefile模式"""
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, "app.ico")
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.ico")


def set_window_icon(window):
    """为窗口设置图标（从app.ico加载）"""
    try:
        icon_path = get_icon_path()
        if os.path.exists(icon_path):
            window.iconbitmap(icon_path)
    except Exception:
        pass


ITEMS = [
    ("cpu_freq", "CPU频率", "GHz", "#00d4ff"),
    ("cpu_temp", "CPU温度", "°C", "#ff6b6b"),
    ("gpu_freq", "GPU频率", "GHz", "#a29bfe"),
    ("gpu_temp", "GPU温度", "°C", "#ff6b6b"),
    ("vram", "显存占用", "", "#fdcb6e"),
    ("memory", "内存占用", "", "#55efc4"),
]


class SettingsWindow(Toplevel):
    def __init__(self, parent, config, on_apply):
        super().__init__(parent)
        self.config_obj = config
        self.on_apply = on_apply
        self.title(f"{APP_DISPLAY_NAME} - 设置")
        self.resizable(False, False)
        self._init_vars()
        self._init_ui()
        set_window_icon(self)
        self.transient(parent)
        self.grab_set()

    def _init_vars(self):
        self.mode_var = StringVar(value=self.config_obj.get("display_mode"))
        self.pos_var = StringVar(value=self.config_obj.get("widget_position"))
        self.opacity_var = DoubleVar(value=self.config_obj.get("opacity"))
        self.bg_transparency_var = DoubleVar(value=float(self.config_obj.get("bg_transparency")))
        self.sample_var = DoubleVar(value=self.config_obj.get("sampling_interval_ms"))
        self.font_size_var = DoubleVar(value=float(self.config_obj.get("font_size")))
        self.cb_cpu_freq = IntVar(value=int(self.config_obj.get("show_cpu_freq")))
        self.cb_cpu_temp = IntVar(value=int(self.config_obj.get("show_cpu_temp")))
        self.cb_gpu_freq = IntVar(value=int(self.config_obj.get("show_gpu_freq")))
        self.cb_gpu_temp = IntVar(value=int(self.config_obj.get("show_gpu_temp")))
        self.cb_vram = IntVar(value=int(self.config_obj.get("show_vram")))
        self.cb_memory = IntVar(value=int(self.config_obj.get("show_memory")))
        self.cb_vram_percent = IntVar(value=int(self.config_obj.get("vram_show_percent")))
        self.cb_memory_percent = IntVar(value=int(self.config_obj.get("memory_show_percent")))
        self.cb_auto_start = IntVar(value=int(get_auto_start()))

    def _init_ui(self):
        frm = ttk.Frame(self, padding=15)
        frm.grid(row=0, column=0, sticky="nsew")

        row = 0
        ttk.Label(frm, text="显示模式:").grid(row=row, column=0, sticky="w", pady=3)
        mode_frame = ttk.Frame(frm)
        mode_frame.grid(row=row, column=1, sticky="w", pady=3)
        ttk.Radiobutton(mode_frame, text="角落小框", variable=self.mode_var, value="widget").pack(side="left", padx=5)
        ttk.Radiobutton(mode_frame, text="顶部横条", variable=self.mode_var, value="bar").pack(side="left", padx=5)
        row += 1

        ttk.Label(frm, text="小框位置:").grid(row=row, column=0, sticky="w", pady=3)
        self.pos_combo = ttk.Combobox(frm, state="readonly", width=15)
        self.pos_combo['values'] = ("右下角", "左下角", "右上角", "左上角")
        pos_map = {"bottom_right": 0, "bottom_left": 1, "top_right": 2, "top_left": 3}
        self.pos_combo.current(pos_map.get(self.pos_var.get(), 0))
        self.pos_combo.grid(row=row, column=1, sticky="w", pady=3)
        row += 1

        ttk.Label(frm, text="窗口透明度:").grid(row=row, column=0, sticky="w", pady=3)
        opacity_frame = ttk.Frame(frm)
        opacity_frame.grid(row=row, column=1, sticky="w", pady=3)
        self.opacity_scale = ttk.Scale(opacity_frame, from_=30, to=100, command=self._on_opacity_change, orient="horizontal", length=140)
        self.opacity_scale.set(self.opacity_var.get() * 100)
        self.opacity_scale.pack(side="left")
        self.opacity_label = ttk.Label(opacity_frame, text=f"{int(self.opacity_var.get() * 100)}%", width=8)
        self.opacity_label.pack(side="left", padx=8)
        row += 1

        ttk.Label(frm, text="背景透明度:").grid(row=row, column=0, sticky="w", pady=3)
        bg_frame = ttk.Frame(frm)
        bg_frame.grid(row=row, column=1, sticky="w", pady=3)
        self.bg_scale = ttk.Scale(bg_frame, from_=0, to=100, variable=self.bg_transparency_var, orient="horizontal", length=140, command=self._on_bg_transparency_change)
        self.bg_scale.pack(side="left")
        self.bg_label = ttk.Label(bg_frame, text=f"{int(self.bg_transparency_var.get())}%", width=8)
        self.bg_label.pack(side="left", padx=8)
        row += 1

        ttk.Label(frm, text="采样间隔:").grid(row=row, column=0, sticky="w", pady=3)
        sample_frame = ttk.Frame(frm)
        sample_frame.grid(row=row, column=1, sticky="w", pady=3)
        self.sample_scale = ttk.Scale(sample_frame, from_=200, to=3000, variable=self.sample_var, orient="horizontal", length=140, command=self._on_sample_change)
        self.sample_scale.pack(side="left")
        self.sample_label = ttk.Label(sample_frame, text=f"{int(self.sample_var.get())}ms", width=8)
        self.sample_label.pack(side="left", padx=8)
        row += 1

        ttk.Label(frm, text="字号大小:").grid(row=row, column=0, sticky="w", pady=3)
        font_frame = ttk.Frame(frm)
        font_frame.grid(row=row, column=1, sticky="w", pady=3)
        self.font_scale = ttk.Scale(font_frame, from_=8, to=20, variable=self.font_size_var, orient="horizontal", length=140, command=self._on_font_size_change)
        self.font_scale.pack(side="left")
        self.font_label = ttk.Label(font_frame, text=f"{int(self.font_size_var.get())}", width=8)
        self.font_label.pack(side="left", padx=8)
        row += 1

        ttk.Separator(frm, orient="horizontal").grid(row=row, column=0, columnspan=2, sticky="ew", pady=10)
        row += 1

        ttk.Label(frm, text="显示指标:").grid(row=row, column=0, sticky="nw", pady=3)
        checks_frame = ttk.Frame(frm)
        checks_frame.grid(row=row, column=1, sticky="w", pady=3)
        Checkbutton(checks_frame, text="CPU频率", variable=self.cb_cpu_freq).pack(anchor="w")
        Checkbutton(checks_frame, text="CPU温度", variable=self.cb_cpu_temp).pack(anchor="w")
        Checkbutton(checks_frame, text="GPU频率", variable=self.cb_gpu_freq).pack(anchor="w")
        Checkbutton(checks_frame, text="GPU温度", variable=self.cb_gpu_temp).pack(anchor="w")
        Checkbutton(checks_frame, text="显存占用", variable=self.cb_vram).pack(anchor="w")
        Checkbutton(checks_frame, text="内存占用", variable=self.cb_memory).pack(anchor="w")
        row += 1

        ttk.Separator(frm, orient="horizontal").grid(row=row, column=0, columnspan=2, sticky="ew", pady=10)
        row += 1

        ttk.Label(frm, text="显示格式:").grid(row=row, column=0, sticky="nw", pady=3)
        fmt_frame = ttk.Frame(frm)
        fmt_frame.grid(row=row, column=1, sticky="w", pady=3)
        Checkbutton(fmt_frame, text="显存以百分比显示", variable=self.cb_vram_percent).pack(anchor="w")
        Checkbutton(fmt_frame, text="内存以百分比显示", variable=self.cb_memory_percent).pack(anchor="w")
        row += 1

        ttk.Separator(frm, orient="horizontal").grid(row=row, column=0, columnspan=2, sticky="ew", pady=10)
        row += 1

        ttk.Label(frm, text="其他选项:").grid(row=row, column=0, sticky="nw", pady=3)
        other_frame = ttk.Frame(frm)
        other_frame.grid(row=row, column=1, sticky="w", pady=3)
        Checkbutton(other_frame, text="开机自启动", variable=self.cb_auto_start).pack(anchor="w")
        row += 1

        ttk.Separator(frm, orient="horizontal").grid(row=row, column=0, columnspan=2, sticky="ew", pady=10)
        row += 1

        btn_frame = ttk.Frame(frm)
        btn_frame.grid(row=row, column=0, columnspan=2, sticky="ew")
        ttk.Button(btn_frame, text="关于", command=self._show_about).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="确定", command=self._apply).pack(side="right", padx=5)
        ttk.Button(btn_frame, text="取消", command=self.destroy).pack(side="right", padx=5)

    def _show_about(self):
        about = Toplevel(self)
        about.title(f"关于 {APP_DISPLAY_NAME}")
        about.resizable(False, False)
        set_window_icon(about)
        about.transient(self)
        about.grab_set()

        frm = ttk.Frame(about, padding=20)
        frm.grid(row=0, column=0, sticky="nsew")

        ttk.Label(frm, text=APP_DISPLAY_NAME, font=("Microsoft YaHei", 14, "bold")).grid(row=0, column=0, pady=(0, 5))
        ttk.Label(frm, text=f"版本 {APP_VERSION}").grid(row=1, column=0, sticky="w", pady=2)
        ttk.Label(frm, text=f"开发者：{APP_DEVELOPER}").grid(row=2, column=0, sticky="w", pady=2)
        ttk.Label(frm, text="一款轻量级 Windows 硬件监控工具").grid(row=3, column=0, sticky="w", pady=2)
        ttk.Label(frm, text="支持 CPU/GPU 频率温度、显存、内存监控").grid(row=4, column=0, sticky="w", pady=2)
        ttk.Label(frm, text="基于 LibreHardwareMonitorLib 和 psutil").grid(row=5, column=0, sticky="w", pady=2)

        ttk.Separator(frm, orient="horizontal").grid(row=6, column=0, sticky="ew", pady=10)
        ttk.Label(frm, text=f"开源协议：{APP_LICENSE}", font=("Microsoft YaHei", 9, "bold")).grid(row=7, column=0, sticky="w")
        ttk.Label(frm, text=f"GitHub：{APP_GITHUB}", foreground="#0066cc").grid(row=8, column=0, sticky="w", pady=(2, 0))

        ttk.Separator(frm, orient="horizontal").grid(row=9, column=0, sticky="ew", pady=10)
        ttk.Label(frm, text="快捷操作：", font=("Microsoft YaHei", 9, "bold")).grid(row=10, column=0, sticky="w")
        ttk.Label(frm, text="• 左键拖动：移动窗口位置").grid(row=11, column=0, sticky="w")
        ttk.Label(frm, text="• 右键菜单：切换模式 / 设置 / 退出").grid(row=12, column=0, sticky="w")
        ttk.Label(frm, text="• 自动吸附屏幕边缘").grid(row=13, column=0, sticky="w")

        ttk.Button(frm, text="关闭", command=about.destroy).grid(row=14, column=0, pady=(15, 0))

        about.update_idletasks()
        about_w = about.winfo_reqwidth()
        about_h = about.winfo_reqheight()
        about.geometry(f"{about_w}x{about_h}")
        about.geometry(f"+{self.winfo_x() + 50}+{self.winfo_y() + 50}")

    def _on_opacity_change(self, value):
        self.opacity_label.config(text=f"{int(float(value))}%")

    def _on_sample_change(self, value):
        self.sample_label.config(text=f"{int(float(value))}ms")

    def _on_font_size_change(self, value):
        self.font_label.config(text=f"{int(float(value))}")

    def _on_bg_transparency_change(self, value):
        self.bg_label.config(text=f"{int(float(value))}%")

    def _apply(self):
        pos_list = ["bottom_right", "bottom_left", "top_right", "top_left"]
        pos_idx = self.pos_combo.current()
        pos_val = pos_list[pos_idx] if 0 <= pos_idx < len(pos_list) else "bottom_right"

        self.config_obj.set("display_mode", self.mode_var.get())
        self.config_obj.set("widget_position", pos_val)
        self.config_obj.set("opacity", float(self.opacity_scale.get()) / 100.0)
        self.config_obj.set("bg_transparency", int(self.bg_transparency_var.get()))
        self.config_obj.set("sampling_interval_ms", int(self.sample_var.get()))
        self.config_obj.set("refresh_interval_ms", int(self.sample_var.get()))
        self.config_obj.set("font_size", int(self.font_size_var.get()))
        self.config_obj.set("show_cpu_freq", bool(self.cb_cpu_freq.get()))
        self.config_obj.set("show_cpu_temp", bool(self.cb_cpu_temp.get()))
        self.config_obj.set("show_gpu_freq", bool(self.cb_gpu_freq.get()))
        self.config_obj.set("show_gpu_temp", bool(self.cb_gpu_temp.get()))
        self.config_obj.set("show_vram", bool(self.cb_vram.get()))
        self.config_obj.set("show_memory", bool(self.cb_memory.get()))
        self.config_obj.set("vram_show_percent", bool(self.cb_vram_percent.get()))
        self.config_obj.set("memory_show_percent", bool(self.cb_memory_percent.get()))

        auto_start_enabled = bool(self.cb_auto_start.get())
        self.config_obj.set("auto_start", auto_start_enabled)
        set_auto_start(auto_start_enabled)

        self.on_apply()
        self.destroy()


class MonitorWindow:
    SNAP_THRESHOLD = 20

    def __init__(self, monitor, config):
        self.monitor = monitor
        self.config = config
        self._drag_x = 0
        self._drag_y = 0
        self._is_dragging = False
        self._labels = {}
        self._row_frames = {}
        self._build_window()

    def _build_window(self):
        self.root = tk.Tk()
        self.root.title(APP_DISPLAY_NAME)

        self._setup_window_icon()
        self._setup_window_style()
        self._create_ui()
        self._setup_context_menu()
        self._setup_drag()
        self._apply_position()
        self._setup_topmost_timer()

        interval = self.config.get("refresh_interval_ms")
        self.root.after(interval, self._update_data)

    def _setup_window_icon(self):
        """加载程序图标（任务栏显示）"""
        try:
            icon_path = get_icon_path()
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
                try:
                    self.root.wm_iconbitmap(icon_path)
                except Exception:
                    pass
        except Exception:
            pass

    def _setup_window_style(self):
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        opacity = self.config.get("opacity")
        self.root.attributes("-alpha", opacity)

        bg_color = self.config.get("bg_color")
        self.root.configure(bg=bg_color)

        # 应用背景透明度：>0 时使用 -transparentcolor 让背景透出桌面
        self._apply_bg_transparency()

        if HAS_WIN32:
            try:
                self.root.update_idletasks()
                hwnd = win32gui.GetParent(self.root.winfo_id())
                if not hwnd:
                    hwnd = self.root.winfo_id()
                ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
                ex_style |= win32con.WS_EX_TOOLWINDOW
                ex_style |= win32con.WS_EX_TOPMOST
                win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style)
            except Exception:
                pass

    def _apply_bg_transparency(self):
        """根据 bg_transparency 配置应用背景透明效果"""
        bg_transparency = self.config.get("bg_transparency")
        bg_color = self.config.get("bg_color")
        try:
            if bg_transparency > 0:
                # 启用透明色：与背景色相同的像素将透出桌面
                self.root.wm_attributes("-transparentcolor", bg_color)
            else:
                # 关闭透明色（设为空字符串取消）
                self.root.wm_attributes("-transparentcolor", "")
        except Exception:
            pass

    def _setup_topmost_timer(self):
        self._force_topmost()
        self.root.after(2000, self._setup_topmost_timer)

    def _force_topmost(self):
        if not HAS_WIN32:
            return
        try:
            self.root.update_idletasks()
            hwnd = win32gui.GetParent(self.root.winfo_id())
            if not hwnd:
                hwnd = self.root.winfo_id()
            flags = (win32con.SWP_NOMOVE | win32con.SWP_NOSIZE |
                     win32con.SWP_NOACTIVATE | win32con.SWP_SHOWWINDOW)
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, flags)
            try:
                win32gui.SetForegroundWindow(hwnd)
            except Exception:
                pass
        except Exception:
            pass

    def _get_visible_items(self):
        show_map = {
            "cpu_freq": self.config.get("show_cpu_freq"),
            "cpu_temp": self.config.get("show_cpu_temp"),
            "gpu_freq": self.config.get("show_gpu_freq"),
            "gpu_temp": self.config.get("show_gpu_temp"),
            "vram": self.config.get("show_vram"),
            "memory": self.config.get("show_memory"),
        }
        visible = [item for item in ITEMS if show_map.get(item[0], True)]
        if not visible:
            visible = [ITEMS[0]]
        return visible

    def _create_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self._labels.clear()
        self._row_frames.clear()

        mode = self.config.get("display_mode")
        if mode == "bar":
            self._create_bar_ui()
        else:
            self._create_widget_ui()

    def _create_widget_ui(self):
        bg_color = self.config.get("bg_color")
        text_color = self.config.get("text_color")
        font_size = self.config.get("font_size")
        font_name = "Microsoft YaHei"
        font = (font_name, font_size)
        font_bold = (font_name, font_size, "bold")

        visible_items = self._get_visible_items()

        outer = tk.Frame(self.root, bg=bg_color, bd=0, highlightthickness=0)
        outer.pack(fill="both", expand=True, padx=12, pady=8)

        for key, label, unit, color in visible_items:
            row = tk.Frame(outer, bg=bg_color, bd=0, highlightthickness=0)
            row.pack(fill="x", pady=2)

            name_lbl = tk.Label(row, text=label, fg=text_color, bg=bg_color,
                                font=font, padx=1)
            name_lbl.pack(side="left")

            val_lbl = tk.Label(row, text=f"-- {unit}", fg=color, bg=bg_color,
                               font=font_bold, padx=1)
            val_lbl.pack(side="right")

            self._labels[key] = val_lbl
            self._row_frames[key] = row

        self.root.update_idletasks()
        # 计算每行所需宽度，取最大值，确保刚好显示所有内容
        max_row_w = 0
        for row in self._row_frames.values():
            row.update_idletasks()
            rw = row.winfo_reqwidth()
            if rw > max_row_w:
                max_row_w = rw
        outer.update_idletasks()
        w = max_row_w + 24  # 左右各12的内边距
        h = outer.winfo_reqheight() + 16  # 上下各8的内边距
        self.root.geometry(f"{w}x{h}")

    def _create_bar_ui(self):
        bg_color = self.config.get("bg_color")
        text_color = self.config.get("text_color")
        font_size = self.config.get("font_size")
        font_name = "Microsoft YaHei"
        font = (font_name, font_size)
        font_bold = (font_name, font_size, "bold")

        visible_items = self._get_visible_items()

        outer = tk.Frame(self.root, bg=bg_color, bd=0, highlightthickness=0)
        outer.pack(fill="both", expand=True, padx=16, pady=6)

        for key, label, unit, color in visible_items:
            row = tk.Frame(outer, bg=bg_color, bd=0, highlightthickness=0)
            row.pack(side="left", padx=12)

            name_lbl = tk.Label(row, text=label, fg=text_color, bg=bg_color,
                                font=font, padx=1)
            name_lbl.pack(side="left")

            val_lbl = tk.Label(row, text=f"-- {unit}", fg=color, bg=bg_color,
                               font=font_bold, padx=1)
            val_lbl.pack(side="left")

            self._labels[key] = val_lbl
            self._row_frames[key] = row

        self.root.update_idletasks()
        outer.update_idletasks()
        # bar模式：每行有 padx=12（两侧共24），外层 padx=16（两侧共32）
        total_row_w = 0
        for row in self._row_frames.values():
            row.update_idletasks()
            total_row_w += row.winfo_reqwidth() + 24
        w = total_row_w + 32
        h = outer.winfo_reqheight() + 12
        self.root.geometry(f"{w}x{h}")

    def _apply_position(self):
        self.root.update_idletasks()
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        w = self.root.winfo_width()
        h = self.root.winfo_height()

        if w < 10:
            w = 280
        if h < 10:
            h = 150

        mode = self.config.get("display_mode")
        if mode == "bar":
            x = (screen_w - w) // 2
            y = 0
            self.root.geometry(f"{w}x{h}+{x}+{y}")
        else:
            pos = self.config.get("widget_position")
            margin = 20
            taskbar_h = 60
            if pos == "bottom_right":
                x = screen_w - w - margin
                y = screen_h - h - margin - taskbar_h
            elif pos == "bottom_left":
                x = margin
                y = screen_h - h - margin - taskbar_h
            elif pos == "top_right":
                x = screen_w - w - margin
                y = margin
            elif pos == "top_left":
                x = margin
                y = margin
            else:
                x = screen_w - w - margin
                y = screen_h - h - margin - taskbar_h
            self.root.geometry(f"{w}x{h}+{x}+{y}")

    def _snap_to_edge(self, x, y):
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        w = self.root.winfo_width()
        h = self.root.winfo_height()

        if x < self.SNAP_THRESHOLD:
            x = 0
        elif x + w > screen_w - self.SNAP_THRESHOLD:
            x = screen_w - w
        if y < self.SNAP_THRESHOLD:
            y = 0
        elif y + h > screen_h - self.SNAP_THRESHOLD - 40:
            y = screen_h - h - 40

        return x, y

    def _setup_context_menu(self):
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="切换显示模式", command=self._toggle_mode)
        self.menu.add_command(label="设置...", command=self._open_settings)
        self.menu.add_separator()
        self.menu.add_command(label="退出", command=self._quit)

        self._bind_event_recursive(self.root, "<Button-3>", self._show_menu)

    def _bind_event_recursive(self, widget, event, handler):
        try:
            widget.bind(event, handler)
            for child in widget.winfo_children():
                self._bind_event_recursive(child, event, handler)
        except Exception:
            pass

    def _show_menu(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def _setup_drag(self):
        self._bind_event_recursive(self.root, "<ButtonPress-1>", self._on_drag_start)
        self._bind_event_recursive(self.root, "<B1-Motion>", self._on_drag_motion)
        self._bind_event_recursive(self.root, "<ButtonRelease-1>", self._on_drag_end)

    def _on_drag_start(self, event):
        self._is_dragging = True
        self._drag_x = event.x_root - self.root.winfo_x()
        self._drag_y = event.y_root - self.root.winfo_y()

    def _on_drag_motion(self, event):
        if not self._is_dragging:
            return
        x = event.x_root - self._drag_x
        y = event.y_root - self._drag_y
        self.root.geometry(f"+{x}+{y}")

    def _on_drag_end(self, event):
        if not self._is_dragging:
            return
        self._is_dragging = False
        x = event.x_root - self._drag_x
        y = event.y_root - self._drag_y
        x, y = self._snap_to_edge(x, y)
        self.root.geometry(f"+{x}+{y}")

    def _toggle_mode(self):
        current = self.config.get("display_mode")
        new_mode = "bar" if current == "widget" else "widget"
        self.config.set("display_mode", new_mode)
        self._apply_config()

    def _open_settings(self):
        SettingsWindow(self.root, self.config, self._apply_config)

    def _apply_config(self):
        opacity = self.config.get("opacity")
        self.root.attributes("-alpha", opacity)

        sample_ms = self.config.get("sampling_interval_ms")
        self.monitor.set_sampling_interval(sample_ms)

        self._create_ui()
        self._apply_position()
        self._apply_bg_transparency()
        self._setup_context_menu()
        self._setup_drag()

    def _update_data(self):
        data = self.monitor.get_data()
        vram_percent = self.config.get("vram_show_percent")
        memory_percent = self.config.get("memory_show_percent")

        for key, label, unit, color in ITEMS:
            if key in self._labels:
                if key == "cpu_freq":
                    text = f"{data['cpu_freq']:.2f} GHz" if data['cpu_freq'] > 0 else "-- GHz"
                elif key == "cpu_temp":
                    text = f"{data['cpu_temp']:.0f} °C" if data['cpu_temp'] > 0 else "-- °C"
                elif key == "gpu_freq":
                    text = f"{data['gpu_freq']:.2f} GHz" if data['gpu_freq'] > 0 else "-- GHz"
                elif key == "gpu_temp":
                    text = f"{data['gpu_temp']:.0f} °C" if data['gpu_temp'] > 0 else "-- °C"
                elif key == "vram":
                    if data['vram_total'] > 0:
                        if vram_percent:
                            pct = (data['vram_used'] / data['vram_total']) * 100
                            text = f"{pct:.0f}%"
                        else:
                            text = f"{data['vram_used']:.1f}/{data['vram_total']:.1f} GB"
                    else:
                        text = "-- GB"
                elif key == "memory":
                    if data['mem_total'] > 0:
                        if memory_percent:
                            pct = (data['mem_used'] / data['mem_total']) * 100
                            text = f"{pct:.0f}%"
                        else:
                            text = f"{data['mem_used']:.1f}/{data['mem_total']:.1f} GB"
                    else:
                        text = "-- GB"
                else:
                    text = f"-- {unit}"
                self._labels[key].config(text=text)

        # 数据更新后，如果窗口宽度不足以容纳内容，自动调整宽度
        self._auto_resize_if_needed()

        interval = self.config.get("refresh_interval_ms")
        self.root.after(interval, self._update_data)

    def _auto_resize_if_needed(self):
        """数据更新后检查并调整窗口宽度以自适应内容"""
        try:
            self.root.update_idletasks()
            mode = self.config.get("display_mode")
            current_w = self.root.winfo_width()
            current_h = self.root.winfo_height()
            current_x = self.root.winfo_x()
            current_y = self.root.winfo_y()

            if mode == "bar":
                # bar模式：横向布局，宽度为所有行宽度总和（含每行padx=12两侧共24，外层padx=16两侧共32）
                total_row_w = 0
                for row in self._row_frames.values():
                    row.update_idletasks()
                    total_row_w += row.winfo_reqwidth() + 24
                needed_w = total_row_w + 32
                needed_h = current_h
                # bar模式总是调整到精确宽度，并保持水平居中
                if abs(needed_w - current_w) > 1:
                    screen_w = self.root.winfo_screenwidth()
                    new_x = (screen_w - needed_w) // 2
                    self.root.geometry(f"{needed_w}x{needed_h}+{new_x}+{current_y}")
            else:
                # widget模式：纵向布局，宽度为最宽行的宽度
                max_row_w = 0
                for row in self._row_frames.values():
                    row.update_idletasks()
                    rw = row.winfo_reqwidth()
                    if rw > max_row_w:
                        max_row_w = rw
                needed_w = max_row_w + 24
                needed_h = current_h
                # widget模式：宽度变化超过阈值时调整，保持原位置
                if abs(needed_w - current_w) > 2:
                    self.root.geometry(f"{needed_w}x{needed_h}+{current_x}+{current_y}")
        except Exception:
            pass

    def _quit(self):
        try:
            self.monitor.stop()
        except Exception:
            pass
        self.root.destroy()
        sys.exit(0)

    def run(self):
        self.root.mainloop()
