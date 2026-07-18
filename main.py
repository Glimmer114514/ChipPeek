import sys
import ctypes

from hardware_monitor import HardwareMonitor
from monitor_window import MonitorWindow
from config import Config


def main():
    config = Config()
    sampling_ms = config.get("sampling_interval_ms")
    monitor = HardwareMonitor(sampling_interval_ms=sampling_ms)
    monitor.start()

    try:
        window = MonitorWindow(monitor, config)
        window.run()
    finally:
        monitor.stop()


if __name__ == "__main__":
    main()
