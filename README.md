# ChipPeek

A lightweight Windows hardware monitoring floating widget. Real-time monitoring of CPU/GPU frequency, temperature, VRAM, and memory usage, always on top including fullscreen apps.

> **Other Languages**: [简体中文](docs/README_zh-CN.md) | [繁體中文](docs/README_zh-TW.md) | **English** | [日本語](docs/README_ja.md) | [한국어](docs/README_ko.md) | [Español](docs/README_es.md) | [Français](docs/README_fr.md) | [Deutsch](docs/README_de.md) | [Português](docs/README_pt.md) | [Русский](docs/README_ru.md) | [العربية](docs/README_ar.md) | [ไทย](docs/README_th.md) | [Tiếng Việt](docs/README_vi.md) | [Bahasa Indonesia](docs/README_id.md) | [Türkçe](docs/README_tr.md) | [Italiano](docs/README_it.md) | [Nederlands](docs/README_nl.md) | [Polski](docs/README_pl.md) | [हिन्दी](docs/README_hi.md) | [বাংলা](docs/README_bn.md) | [Svenska](docs/README_sv.md) | [Norsk](docs/README_no.md) | [Dansk](docs/README_da.md) | [Suomi](docs/README_fi.md) | [Čeština](docs/README_cs.md) | [Ελληνικά](docs/README_el.md) | [Magyar](docs/README_hu.md) | [Română](docs/README_ro.md) | [Українська](docs/README_uk.md) | [Slovenčina](docs/README_sk.md) | [Български](docs/README_bg.md) | [Hrvatski](docs/README_hr.md) | [Српски](docs/README_sr.md) | [Català](docs/README_ca.md) | [Slovenščina](docs/README_sl.md) | [Eesti](docs/README_et.md) | [Latviešu](docs/README_lv.md) | [Lietuvių](docs/README_lt.md) | [فارسی](docs/README_fa.md) | [Bahasa Melayu](docs/README_ms.md) | [اردو](docs/README_ur.md) | [தமிழ்](docs/README_ta.md) | [తెలుగు](docs/README_te.md) | [मराठी](docs/README_mr.md) | [ગુજરાતી](docs/README_gu.md) | [ਪੰਜਾਬੀ](docs/README_pa.md) | [ಕನ್ನಡ](docs/README_kn.md) | [മലയാളം](docs/README_ml.md) | [Қазақша](docs/README_kk.md) | [O'zbekcha](docs/README_uz.md) | [עברית](docs/README_he.md) | [မြန်မာဘာသာ](docs/README_my.md) | [ភាសាខ្មែរ](docs/README_km.md) | [ພາສາລາວ](docs/README_lo.md) | [Kiswahili](docs/README_sw.md) | [Afrikaans](docs/README_af.md) | [አማርኛ](docs/README_am.md) | [isiZulu](docs/README_zu.md)

## Features

- **Real-time monitoring**: CPU frequency, CPU temperature, GPU frequency, GPU temperature, VRAM usage, memory usage
- **Dual display modes**: Corner widget / Top bar, one-click switch
- **Customizable display**: Freely choose which metrics to show, toggle between percentage/actual values
- **Always on top**: Stays above all windows, works in fullscreen games
- **Auto-sizing**: Window width automatically adjusts to fit content
- **Adjustable style**: Window opacity, background transparency, font size all adjustable
- **Multi-language support**: 20+ languages, auto-detects system language
- **Convenient operation**: Left-drag to move, right-click menu for quick settings, auto snap to screen edges
- **Configurable sampling**: 200ms - 3000ms adjustable
- **Auto start**: Launch automatically on Windows login
- **Low resource usage**: Minimal footprint in background

## Quick Start

### Direct Use

Download `ChipPeek.exe` and double-click to run (will automatically request admin privileges for CPU temperature and accurate frequency reading).

### Run from Source

```bash
# Clone the repository
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

## System Requirements

- Windows 10 / Windows 11
- Administrator privileges (recommended), otherwise CPU temperature and accurate frequency may not be available
- .NET Framework 4.7.2 or higher (required by LibreHardwareMonitor)

## Build as EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

After building, the EXE file is located at `dist/ChipPeek.exe`.

## Usage

### Basic Operations

| Action | Description |
|------|------|
| Left drag | Move window position |
| Right click | Open menu (switch mode / settings / exit) |
| Auto snap | Automatically snaps within 20px of screen edges |

### Display Modes

- **Corner Widget**: All metrics arranged vertically, can be placed at any screen corner
- **Top Bar**: All metrics arranged horizontally, centered at the top of the screen by default

### Settings

- **Display mode**: Corner widget / Top bar
- **Widget position**: Bottom right / Bottom left / Top right / Top left
- **Window opacity**: 30% - 100% overall window transparency
- **Background transparency**: 0% - 100% background transparent (text stays crisp)
- **Sampling interval**: 200ms - 3000ms data refresh rate
- **Font size**: 8 - 20 point font
- **Language**: 20+ languages, auto-detects system language
- **Display metrics**: Toggle each metric independently
- **Display format**: VRAM / Memory can toggle between percentage or actual values
- **Auto start**: Run automatically when logging into Windows

## Tech Stack

- **GUI**：Tkinter
- **Hardware data**：LibreHardwareMonitorLib (via pythonnet), psutil, pynvml (NVIDIA GPU fallback)
- **System integration**：pywin32 (window topmost, auto-start registry)
- **Packaging**：PyInstaller

## Project Structure

```
ChipPeek/
├── main.py                  # Entry point
├── monitor_window.py        # Window UI and interaction logic
├── hardware_monitor.py      # Hardware data collection
├── config.py                # Configuration management
├── i18n.py                  # Internationalization
├── generate_icon.py         # Icon generation script
├── admin.manifest           # UAC admin privilege manifest
├── app.ico                  # Application icon
├── app.png                  # Icon preview
├── requirements.txt         # Python dependencies
├── docs/                    # Multi-language docs
│   └── README_*.md
├── i18n/                    # Translation files
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Compiled executable
```

## Configuration File

The `config.json` file is saved in the same directory as the EXE, containing all adjustable settings. Settings are saved automatically when modified.

## License

MIT License

## Developer

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- Project URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Credits

- LibreHardwareMonitor - Hardware monitoring library
- psutil - Cross-platform system monitoring
- PyInstaller - Python packaging tool
