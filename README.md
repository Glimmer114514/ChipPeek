# ChipView

一款轻量级 Windows 硬件监控悬浮窗工具。支持 CPU/GPU 频率、温度、显存、内存占用实时监控，以悬浮窗形式常驻桌面，支持全屏置顶显示。

![ChipView](app.png)

## ✨ 功能特性

- **实时监控**：CPU 频率、CPU 温度、GPU 频率、GPU 温度、显存占用、内存占用
- **双显示模式**：角落小框 / 顶部横条，一键切换
- **自定义显示**：可自由选择显示哪些指标，支持百分比/实际数值切换
- **悬浮置顶**：始终显示在所有程序最顶层，支持全屏游戏置顶
- **自适应大小**：窗口宽度根据内容自动调整，文字完整显示
- **可调节样式**：窗口透明度、背景透明度、字号大小均可调节
- **便捷操作**：左键拖动移动位置，右键菜单快速设置，自动吸附屏幕边缘
- **采样频率**：200ms - 3000ms 可调节
- **开机自启**：支持开机自动启动
- **低资源占用**：后台运行占用极低

## 🚀 快速开始

### 直接使用

下载 `硬件监控.exe`，右键以管理员身份运行（CPU 温度和精确频率需要管理员权限读取 MSR 寄存器）。

### 源码运行

```bash
# 克隆项目
git clone https://github.com/R41NH4RD/ChipView.git
cd ChipView

# 安装依赖
pip install -r requirements.txt

# 运行
python main.py
```

## 🔧 系统要求

- Windows 10 / Windows 11
- 需要管理员权限（推荐），否则 CPU 温度和精确频率可能无法读取
- .NET Framework 4.7.2 或更高（LibreHardwareMonitor 依赖）

## 📦 打包为 EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipView" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

打包完成后，EXE 文件位于 `dist/ChipView.exe`。

## 🎮 使用说明

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
- **显示指标**：可独立开关每一项指标
- **显示格式**：显存 / 内存可切换百分比或实际数值
- **开机自启动**：登录 Windows 后自动运行

## 🏗️ 技术栈

- **GUI**：Tkinter
- **硬件数据**：
  - [LibreHardwareMonitorLib](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor)（通过 pythonnet 调用）
  - [psutil](https://github.com/giampaolo/psutil)
  - [pynvml](https://pypi.org/project/nvidia-ml-py/)（NVIDIA GPU 备用方案）
- **系统集成**：pywin32（窗口置顶、自动启动注册表）
- **打包**：PyInstaller

## 📁 项目结构

```
ChipView/
├── main.py                  # 程序入口
├── monitor_window.py        # 窗口 UI 与交互逻辑
├── hardware_monitor.py      # 硬件数据采集
├── config.py                # 配置管理
├── generate_icon.py         # 图标生成脚本
├── admin.manifest           # UAC 管理员权限清单
├── app.ico                  # 程序图标
├── app.png                  # 图标预览
├── requirements.txt         # Python 依赖
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipView.exe         # 编译后的可执行文件
```

## 📝 配置文件

配置文件 `config.json` 保存在 EXE 同目录下，包含所有可调节设置。修改设置后会自动保存。

## 🪪 许可证

[MIT License](LICENSE)

## 👤 开发者

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/R41NH4RD)
- 项目地址: [https://github.com/R41NH4RD/ChipView](https://github.com/R41NH4RD/ChipView)

## 🙏 致谢

- [LibreHardwareMonitor](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor) - 硬件监控库
- [psutil](https://github.com/giampaolo/psutil) - 跨平台系统监控
- [PyInstaller](https://github.com/pyinstaller/pyinstaller) - Python 程序打包工具
