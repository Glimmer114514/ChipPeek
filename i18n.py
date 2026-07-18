"""
ChipPeek 多语言支持模块
"""
import json
import os
import sys
import locale


LANGUAGES = {
    "zh-CN": "简体中文",
    "zh-TW": "繁體中文",
    "en": "English",
    "ja": "日本語",
    "ko": "한국어",
    "es": "Español",
    "fr": "Français",
    "de": "Deutsch",
    "pt": "Português",
    "ru": "Русский",
    "ar": "العربية",
    "th": "ไทย",
    "vi": "Tiếng Việt",
    "id": "Bahasa Indonesia",
    "tr": "Türkçe",
    "it": "Italiano",
    "nl": "Nederlands",
    "pl": "Polski",
    "hi": "हिन्दी",
    "bn": "বাংলা",
}


TRANSLATIONS = {
    "zh-CN": {
        "app_name": "ChipPeek 硬件监控",
        "settings": "设置",
        "about": "关于",
        "display_mode": "显示模式",
        "widget_mode": "角落小框",
        "bar_mode": "顶部横条",
        "widget_position": "小框位置",
        "bottom_right": "右下角",
        "bottom_left": "左下角",
        "top_right": "右上角",
        "top_left": "左上角",
        "window_opacity": "窗口透明度",
        "bg_transparency": "背景透明度",
        "sampling_interval": "采样间隔",
        "font_size": "字号大小",
        "show_items": "显示项目",
        "cpu_freq": "CPU频率",
        "cpu_temp": "CPU温度",
        "gpu_freq": "GPU频率",
        "gpu_temp": "GPU温度",
        "vram": "显存",
        "memory": "内存",
        "display_format": "显示格式",
        "vram_percent": "显存显示百分比",
        "memory_percent": "内存显示百分比",
        "other_options": "其他选项",
        "auto_start": "开机自启动",
        "language": "语言",
        "ok": "确定",
        "cancel": "取消",
        "close": "关闭",
        "version": "版本",
        "developer": "开发者",
        "license": "开源协议",
        "quick_actions": "快捷操作",
        "action_drag": "左键拖动：移动窗口位置",
        "action_right_click": "右键菜单：切换模式 / 设置 / 退出",
        "action_snap": "自动吸附屏幕边缘",
        "menu_switch_mode": "切换显示模式",
        "menu_settings": "设置",
        "menu_exit": "退出",
        "cpu_freq_label": "CPU",
        "cpu_temp_label": "CPU温度",
        "gpu_freq_label": "GPU",
        "gpu_temp_label": "GPU温度",
        "vram_label": "显存",
        "memory_label": "内存",
        "ghz_unit": "GHz",
        "mhz_unit": "MHz",
        "celsius_unit": "°C",
        "gb_unit": "GB",
        "percent_unit": "%",
        "about_description_1": "一款轻量级 Windows 硬件监控工具",
        "about_description_2": "支持 CPU/GPU 频率温度、显存、内存监控",
        "about_description_3": "基于 LibreHardwareMonitorLib 和 psutil",
    },
    "en": {
        "app_name": "ChipPeek Hardware Monitor",
        "settings": "Settings",
        "about": "About",
        "display_mode": "Display Mode",
        "widget_mode": "Corner Widget",
        "bar_mode": "Top Bar",
        "widget_position": "Widget Position",
        "bottom_right": "Bottom Right",
        "bottom_left": "Bottom Left",
        "top_right": "Top Right",
        "top_left": "Top Left",
        "window_opacity": "Window Opacity",
        "bg_transparency": "Background Transparency",
        "sampling_interval": "Sampling Interval",
        "font_size": "Font Size",
        "show_items": "Show Items",
        "cpu_freq": "CPU Frequency",
        "cpu_temp": "CPU Temperature",
        "gpu_freq": "GPU Frequency",
        "gpu_temp": "GPU Temperature",
        "vram": "VRAM",
        "memory": "Memory",
        "display_format": "Display Format",
        "vram_percent": "VRAM as Percentage",
        "memory_percent": "Memory as Percentage",
        "other_options": "Other Options",
        "auto_start": "Auto Start",
        "language": "Language",
        "ok": "OK",
        "cancel": "Cancel",
        "close": "Close",
        "version": "Version",
        "developer": "Developer",
        "license": "License",
        "quick_actions": "Quick Actions",
        "action_drag": "Left drag: Move window",
        "action_right_click": "Right click: Menu / Settings / Exit",
        "action_snap": "Auto snap to screen edges",
        "menu_switch_mode": "Switch Mode",
        "menu_settings": "Settings",
        "menu_exit": "Exit",
        "cpu_freq_label": "CPU",
        "cpu_temp_label": "CPU Temp",
        "gpu_freq_label": "GPU",
        "gpu_temp_label": "GPU Temp",
        "vram_label": "VRAM",
        "memory_label": "Memory",
        "ghz_unit": "GHz",
        "mhz_unit": "MHz",
        "celsius_unit": "°C",
        "gb_unit": "GB",
        "percent_unit": "%",
        "about_description_1": "A lightweight Windows hardware monitor tool",
        "about_description_2": "CPU/GPU frequency & temp, VRAM, memory monitoring",
        "about_description_3": "Based on LibreHardwareMonitorLib and psutil",
    },
}


def get_resource_dir():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


def get_i18n_dir():
    return os.path.join(get_resource_dir(), "i18n")


def load_translations():
    """从 i18n 目录加载所有语言的翻译文件"""
    i18n_dir = get_i18n_dir()
    if not os.path.exists(i18n_dir):
        return TRANSLATIONS

    all_trans = dict(TRANSLATIONS)
    for lang_code in LANGUAGES:
        file_path = os.path.join(i18n_dir, f"{lang_code}.json")
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    all_trans[lang_code] = data
            except Exception:
                pass
    return all_trans


def detect_system_language():
    """检测系统默认语言"""
    try:
        lang = locale.getdefaultlocale()[0]
        if lang:
            lang = lang.replace("_", "-")
            if lang in LANGUAGES:
                return lang
            # 尝试匹配前缀（如 zh-CN 匹配 zh）
            prefix = lang.split("-")[0]
            for code in LANGUAGES:
                if code.startswith(prefix):
                    return code
    except Exception:
        pass
    return "en"


class I18n:
    def __init__(self, language=None):
        self._translations = load_translations()
        if language is None:
            language = detect_system_language()
        self._language = language

    @property
    def language(self):
        return self._language

    def set_language(self, lang):
        if lang in LANGUAGES:
            self._language = lang

    def t(self, key):
        """获取翻译文本"""
        lang_data = self._translations.get(self._language, {})
        if key in lang_data:
            return lang_data[key]
        # fallback to English
        en_data = self._translations.get("en", {})
        if key in en_data:
            return en_data[key]
        # fallback to Chinese
        zh_data = self._translations.get("zh-CN", {})
        return zh_data.get(key, key)

    def get_languages(self):
        """返回可用语言列表 [(code, name), ...]"""
        return [(code, name) for code, name in LANGUAGES.items()]
