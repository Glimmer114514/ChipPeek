# ChipPeek

一款輕量級 Windows 硬體監控懸浮窗工具。支援 CPU/GPU 頻率、溫度、顯存、記憶體佔用即時監控，以懸浮窗形式常駐桌面，支援全畫面置頂顯示。

> **其他語言**: [简体中文](README_zh-CN.md) | **繁體中文** | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md)

## 功能特性

- **即時監控**：CPU 頻率、CPU 溫度、GPU 頻率、GPU 溫度、顯存佔用、記憶體佔用
- **雙顯示模式**：角落小框 / 頂部橫條，一鍵切換
- **自訂顯示**：可自由選擇顯示哪些指標，支援百分比/實際數值切換
- **懸浮置頂**：始終顯示在所有程式最頂層，支援全畫面遊戲置頂
- **自適應大小**：視窗寬度根據內容自動調整，文字完整顯示
- **可調整式樣**：視窗透明度、背景透明度、字號大小均可調節
- **多語言支援**：支援 20+ 種主流語言，自動偵測系統語言
- **便捷操作**：左鍵拖動移動位置，右鍵選單快速設定，自動吸附螢幕邊緣
- **採樣頻率**：200ms - 3000ms 可調節
- **開機自啟**：支援開機自動啟動
- **低資源佔用**：後台執行佔用極低

## 快速開始

### 直接使用

下載 `ChipPeek.exe`，雙擊執行（會自動請求管理員權限以讀取 CPU 溫度和精確頻率）。

### 原始碼執行

```bash
# 複製專案
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# 安裝依賴
pip install -r requirements.txt

# 執行
python main.py
```

## 系統需求

- Windows 10 / Windows 11
- 管理員權限（推薦），否則 CPU 溫度和精確頻率可能無法讀取
- .NET Framework 4.7.2 或更高（LibreHardwareMonitor 依賴）

## 打包為 EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

打包完成後，EXE 檔案位於 `dist/ChipPeek.exe`。

## 使用說明

### 基本操作

| 操作 | 說明 |
|------|------|
| 左鍵拖動 | 移動視窗位置 |
| 右鍵 | 打開選單（切換模式 / 設定 / 退出） |
| 自動吸附 | 拖動到螢幕邊緣 20px 內自動吸附 |

### 顯示模式

- **角落小框**：縱向排列所有指標，可放在螢幕四角
- **頂部橫條**：橫向排列所有指標，預設置中顯示在螢幕頂部

### 設定選項

- **顯示模式**：角落小框 / 頂部橫條
- **小框位置**：右下角 / 左下角 / 右上角 / 左上角
- **視窗透明度**：30% - 100% 整體視窗透明度
- **背景透明度**：0% - 100% 背景透明（文字保持清晰）
- **採樣間隔**：200ms - 3000ms 資料重新整理頻率
- **字號大小**：8 - 20 號字型
- **語言**：支援 20+ 種語言，自動偵測系統語言
- **顯示指標**：可獨立開關每一項指標
- **顯示格式**：顯存 / 記憶體可切換百分比或實際數值
- **開機自啟動**：登入 Windows 後自動執行

## 技術棧

- **GUI**：Tkinter
- **硬體資料**：LibreHardwareMonitorLib（透過 pythonnet 呼叫）、psutil、pynvml（NVIDIA GPU 備用方案）
- **系統整合**：pywin32（視窗置頂、自動啟動註冊表）
- **打包**：PyInstaller

## 專案結構

```
ChipPeek/
├── main.py                  # 程式入口
├── monitor_window.py        # 視窗 UI 與互動邏輯
├── hardware_monitor.py      # 硬體資料採集
├── config.py                # 設定管理
├── i18n.py                  # 多語言支援
├── generate_icon.py         # 圖示生成指令碼
├── admin.manifest           # UAC 管理員權限清單
├── app.ico                  # 程式圖示
├── app.png                  # 圖示預覽
├── requirements.txt         # Python 依賴
├── docs/                    # 多語言文件
│   └── README_*.md
├── i18n/                    # 翻譯檔案
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # 編譯後的可執行檔
```

## 設定檔

設定檔 `config.json` 儲存在 EXE 同目錄下，包含所有可調整設定。修改設定後會自動儲存。

## 授權條款

MIT License

## 開發者

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- 專案地址: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## 致謝

- LibreHardwareMonitor - 硬體監控庫
- psutil - 跨平台系統監控
- PyInstaller - Python 程式打包工具
