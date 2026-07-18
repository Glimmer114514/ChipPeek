# ChipPeek

一款轻量级 Windows 硬件监控悬浮窗工具。支持 CPU/GPU 频率、温度、显存、内存占用实时监控，以悬浮窗形式常驻桌面，支持全屏置顶显示。

> **其他语言**: **简体中文** | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md)

## 功能特性

- **实时监控**：CPU 频率、CPU 温度、GPU 频率、GPU 温度、显存占用、内存占用
- **双显示模式**：角落小框 / 顶部横条，一键切换
- **自定义显示**：可自由选择显示哪些指标，支持百分比/实际数值切换
- **悬浮置顶**：始终显示在所有程序最顶层，支持全屏游戏置顶
- **自适应大小**：窗口宽度根据内容自动调整，文字完整显示
- **可调节样式**：窗口透明度、背景透明度、字号大小均可调节
- **多语言支持**：支持 20+ 种主流语言，自动检测系统语言
- **便捷操作**：左键拖动移动位置，右键菜单快速设置，自动吸附屏幕边缘
- **采样频率**：200ms - 3000ms 可调节
- **开机自启**：支持开机自动启动
- **低资源占用**：后台运行占用极低

## 快速开始

### 直接使用

下载 `ChipPeek.exe`，双击运行（会自动请求管理员权限以读取 CPU 温度和精确频率）。

### 源码运行

```bash
# 克隆项目
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# 安装依赖
pip install -r requirements.txt

# 运行
python main.py
```

## 系统要求

- Windows 10 / Windows 11
- 管理员权限（推荐），否则 CPU 温度和精确频率可能无法读取
- .NET Framework 4.7.2 或更高（LibreHardwareMonitor 依赖）

## 打包为 EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

打包完成后，EXE 文件位于 `dist/ChipPeek.exe`。

## 使用说明

### 基本操作

| 操作 | 说明 |
|------|------|
| 左键拖动 | 移动窗口位置 |
| 右键 | 打开菜单（切换模式 / 设置 / 退出） |
| 自动吸附 | 拖动到屏幕边缘 20px 内自动吸附 |

### 显示模式

- **角落小框**：纵向排列所有指标，可放在屏幕四角
- **顶部横条**：横向排列所有指标，默认居中显示在屏幕顶部

### 设置选项

- **显示模式**：角落小框 / 顶部横条
- **小框位置**：右下角 / 左下角 / 右上角 / 左上角
- **窗口透明度**：30% - 100% 整体窗口透明度
- **背景透明度**：0% - 100% 背景透明（文字保持清晰）
- **采样间隔**：200ms - 3000ms 数据刷新频率
- **字号大小**：8 - 20 号字体
- **语言**：支持 20+ 种语言，自动检测系统语言
- **显示指标**：可独立开关每一项指标
- **显示格式**：显存 / 内存可切换百分比或实际数值
- **开机自启动**：登录 Windows 后自动运行

## 技术栈

- **GUI**：Tkinter
- **硬件数据**：LibreHardwareMonitorLib（通过 pythonnet 调用）、psutil、pynvml（NVIDIA GPU 备用方案）
- **系统集成**：pywin32（窗口置顶、自动启动注册表）
- **打包**：PyInstaller

## 项目结构

```
ChipPeek/
├── main.py                  # 程序入口
├── monitor_window.py        # 窗口 UI 与交互逻辑
├── hardware_monitor.py      # 硬件数据采集
├── config.py                # 配置管理
├── i18n.py                  # 多语言支持
├── generate_icon.py         # 图标生成脚本
├── admin.manifest           # UAC 管理员权限清单
├── app.ico                  # 程序图标
├── app.png                  # 图标预览
├── requirements.txt         # Python 依赖
├── docs/                    # 多语言文档
│   └── README_*.md
├── i18n/                    # 翻译文件
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # 编译后的可执行文件
```

## 配置文件

配置文件 `config.json` 保存在 EXE 同目录下，包含所有可调节设置。修改设置后会自动保存。

## 许可证

MIT License

## 开发者

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- 项目地址: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## 致谢

- LibreHardwareMonitor - 硬件监控库
- psutil - 跨平台系统监控
- PyInstaller - Python 程序打包工具
