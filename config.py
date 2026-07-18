import json
import os
import sys

def get_config_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

CONFIG_FILE = os.path.join(get_config_dir(), "config.json")

DEFAULT_CONFIG = {
    "display_mode": "widget",
    "widget_position": "bottom_right",
    "opacity": 0.85,
    "bg_transparency": 0,
    "bg_color": "#1a1a2e",
    "text_color": "#ffffff",
    "accent_color": "#00d4ff",
    "font_size": 11,
    "show_cpu_freq": True,
    "show_cpu_temp": True,
    "show_gpu_freq": True,
    "show_gpu_temp": True,
    "show_vram": True,
    "show_memory": True,
    "vram_show_percent": False,
    "memory_show_percent": False,
    "refresh_interval_ms": 500,
    "sampling_interval_ms": 500,
    "auto_start": False,
}


class Config:
    def __init__(self):
        self._data = dict(DEFAULT_CONFIG)
        self.load()

    def load(self):
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    self._data.update(loaded)
        except Exception:
            pass

    def save(self):
        try:
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(self._data, f, indent=2, ensure_ascii=False)
        except Exception:
            pass

    def get(self, key):
        return self._data.get(key, DEFAULT_CONFIG.get(key))

    def set(self, key, value):
        self._data[key] = value
        self.save()
