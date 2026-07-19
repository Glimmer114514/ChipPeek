# ChipPeek

軽量なWindowsハードウェアモニタリングツール。CPU/GPUの周波数、温度、VRAM、メモリ使用率をリアルタイムで監視し、フルスクリーンアプリでも最前面に表示されます。

> **他の言語**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | **日本語** | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## 機能

- **リアルタイム監視**: CPU周波数、CPU温度、GPU周波数、GPU温度、VRAM使用率、メモリ使用率
- **2つの表示モード**: コーナーウィジェット / トップバー、ワンクリックで切り替え
- **カスタマイズ可能な表示**: 表示する指標を自由に選択、パーセント/実値切り替え可能
- **常に最前面**: 全てのウィンドウの上に表示、フルスクリーンゲームでも動作
- **自動サイズ調整**: ウィンドウ幅がコンテンツに合わせて自動調整
- **調整可能なスタイル**: ウィンドウ透明度、背景透明度、フォントサイズが調整可能
- **多言語対応**: 20以上の言語、システム言語を自動検出
- **簡単操作**: 左ドラッグで移動、右クリックメニューでクイック設定、画面端に自動吸着
- **サンプリング間隔調整**: 200ms - 3000ms 調整可能
- **自動起動**: Windowsログイン時に自動起動
- **低リソース**: バックグラウンドでのリソース消費は最小限

## クイックスタート

### 直接使用

`ChipPeek.exe`をダウンロードしてダブルクリックで実行（CPU温度と正確な周波数読み取りのため、自動的に管理者権限を要求します）。

### ソースから実行

```bash
# リポジトリをクローン
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# 依存関係をインストール
pip install -r requirements.txt

# 実行
python main.py
```

## システム要件

- Windows 10 / Windows 11
- 管理者権限（推奨）、ない場合はCPU温度と正確な周波数が読み取れない場合があります
- .NET Framework 4.7.2 以上（LibreHardwareMonitorに必要）

## EXEとしてビルド

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

ビルド後、EXEファイルは `dist/ChipPeek.exe` に生成されます。

## 使い方

### 基本操作

| 操作 | 説明 |
|------|------|
| 左ドラッグ | ウィンドウを移動 |
| 右クリック | メニューを開く（モード切替 / 設定 / 終了） |
| 自動吸着 | 画面端の20px以内で自動的に吸着 |

### 表示モード

- **コーナーウィジェット**: 全指標を縦に配置、画面の四隅に配置可能
- **トップバー**: 全指標を横に配置、デフォルトで画面上部中央に表示

### 設定

- **表示モード**: コーナーウィジェット / トップバー
- **ウィジェット位置**: 右下 / 左下 / 右上 / 左上
- **ウィンドウ透明度**: 30% - 100% 全体の透明度
- **背景透明度**: 0% - 100% 背景透明（テキストは鮮明なまま）
- **サンプリング間隔**: 200ms - 3000ms データ更新間隔
- **フォントサイズ**: 8 - 20ポイント
- **言語**: 20以上の言語、システム言語を自動検出
- **表示指標**: 各指標を個別にオン/オフ可能
- **表示形式**: VRAM / メモリはパーセントまたは実値に切り替え可能
- **自動起動**: Windowsログイン時に自動実行

## 技術スタック

- **GUI**：Tkinter
- **ハードウェアデータ**：LibreHardwareMonitorLib（pythonnet経由）、psutil、pynvml（NVIDIA GPU代替）
- **システム統合**：pywin32（ウィンドウ最前面、自動起動レジストリ）
- **パッケージ**：PyInstaller

## プロジェクト構成

```
ChipPeek/
├── main.py                  # エントリーポイント
├── monitor_window.py        # ウィンドウUIとインタラクション
├── hardware_monitor.py      # ハードウェアデータ収集
├── config.py                # 設定管理
├── i18n.py                  # 国際化対応
├── generate_icon.py         # アイコン生成スクリプト
├── admin.manifest           # UAC管理者権限マニフェスト
├── app.ico                  # アプリケーションアイコン
├── app.png                  # アイコンプレビュー
├── requirements.txt         # Python依存関係
├── docs/                    # 多言語ドキュメント
│   └── README_*.md
├── i18n/                    # 翻訳ファイル
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # コンパイル済み実行ファイル
```

## 設定ファイル

設定ファイル `config.json` はEXEと同じディレクトリに保存され、全ての調整可能な設定が含まれています。設定の変更は自動的に保存されます。

## ライセンス

MIT License

## 開発者

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- プロジェクトURL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## 謝辞

- LibreHardwareMonitor - ハードウェアモニタリングライブラリ
- psutil - クロスプラットフォームシステムモニタリング
- PyInstaller - Pythonパッケージツール
