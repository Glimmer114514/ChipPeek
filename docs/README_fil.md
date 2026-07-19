# ChipPeek

Isang magaan na Windows hardware monitoring floating widget. Real-time na pagsubaybay sa dalas ng CPU/GPU, temperatura, VRAM, at paggamit ng memorya, laging nasa itaas kasama ang mga fullscreen app.

> **Iba pang mga Wika**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | **Filipino** | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Mga Tampok

- **Real-time na pagsubaybay**: Dalas ng CPU, temperatura ng CPU, dalas ng GPU, temperatura ng GPU, paggamit ng VRAM, paggamit ng memorya
- **Dalawang mode ng pagpapakita**: Widget sa sulok / Bar sa itaas, isang click lang ang paglipat
- **Nako-customize na pagpapakita**: Malayang pumili kung aling mga sukatan ang ipapakita, magpalitan sa pagitan ng porsyento/tunay na halaga
- **Laging nasa itaas**: Nananatili sa itaas ng lahat ng bintana, gumagana sa mga fullscreen na laro
- **Awtomatikong pagsasaayos ng laki**: Ang lapad ng bintana ay awtomatikong umaangkop sa nilalaman
- **Naaayos na istilo**: Opacity ng bintana, transparency ng background, laki ng font ay lahat maaaring i-adjust
- **Suporta sa maraming wika**: 20+ na wika, awtomatikong nakakakita ng wika ng system
- **Maginhawang operasyon**: Kaliwang drag para ilipat, kanang click menu para sa mabilis na setting, awtomatikong dumikit sa mga gilid ng screen
- **Naaayos na sampling**: 200ms - 3000ms na maaaring i-adjust
- **Awtomatikong pagsisimula**: Awtomatikong maglunsad sa pag-login ng Windows
- **Mababang paggamit ng resource**: Minimal na bakas sa background

## Mabilis na Pagsisimula

### Direktang Paggamit

I-download ang `ChipPeek.exe` at i-double click para patakbuhin (awtomatikong hihingi ng admin privileges para sa temperatura ng CPU at tumpak na pagbabasa ng dalas).

### Patakbuhin mula sa Source

```bash
# I-clone ang repository
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# I-install ang mga dependencies
pip install -r requirements.txt

# Patakbuhin
python main.py
```

## Mga Kinakailangan ng System

- Windows 10 / Windows 11
- Administrator privileges (inirerekomenda), kung hindi ay maaaring hindi available ang temperatura ng CPU at tumpak na dalas
- .NET Framework 4.7.2 o mas mataas (kinakailangan ng LibreHardwareMonitor)

## I-build bilang EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Pagkatapos mag-build, ang EXE file ay matatagpuan sa `dist/ChipPeek.exe`.

## Paggamit

### Mga Pangunahing Operasyon

| Kilos | Paglalarawan |
|------|------|
| Kaliwang drag | Ilipat ang posisyon ng bintana |
| Kanang pag-click | Buksan ang menu (palitan ang mode / mga setting / lumabas) |
| Auto snap | Awtomatikong dumikit sa loob ng 20px ng mga gilid ng screen |

### Mga Mode ng Pagpapakita

- **Widget sa Sulok**: Lahat ng sukatan ay nakaayos nang patayo, maaaring ilagay sa anumang sulok ng screen
- **Bar sa Itaas**: Lahat ng sukatan ay nakaayos nang pahalang, nakasentro sa itaas ng screen bilang default

### Mga Setting

- **Mode ng pagpapakita**: Widget sa sulok / Bar sa itaas
- **Posisyon ng widget**: Ibaba sa kanan / Ibaba sa kaliwa / Itaas sa kanan / Itaas sa kaliwa
- **Opacity ng bintana**: 30% - 100% na pangkalahatang transparency ng bintana
- **Transparency ng background**: 0% - 100% na transparent na background (nananatiling malinaw ang teksto)
- **Pagitan ng sampling**: 200ms - 3000ms na bilis ng pag-refresh ng data
- **Laki ng font**: 8 - 20 point na font
- **Wika**: 20+ na wika, awtomatikong nakakakita ng wika ng system
- **Mga sukatan ng pagpapakita**: I-toggle ang bawat sukatan nang magkahiwalay
- **Format ng pagpapakita**: Ang VRAM / Memorya ay maaaring i-toggle sa pagitan ng porsyento o tunay na halaga
- **Awtomatikong pagsisimula**: Awtomatikong patakbuhin kapag nag-login sa Windows

## Tech Stack

- **GUI**：Tkinter
- **Data ng hardware**：LibreHardwareMonitorLib (sa pamamagitan ng pythonnet), psutil, pynvml (NVIDIA GPU fallback)
- **Pagsasama ng system**：pywin32 (window topmost, auto-start registry)
- **Pagpapakete**：PyInstaller

## Istraktura ng Proyekto

```
ChipPeek/
├── main.py                  # Entry point
├── monitor_window.py        # UI ng bintana at lohika ng pakikipag-ugnayan
├── hardware_monitor.py      # Pagkolekta ng data ng hardware
├── config.py                # Pamamahala ng configuration
├── i18n.py                  # Internasyonalisasyon
├── generate_icon.py         # Script ng pagbuo ng icon
├── admin.manifest           # Manifest ng pribilehiyo ng UAC admin
├── app.ico                  # Icon ng aplikasyon
├── app.png                  # Preview ng icon
├── requirements.txt         # Mga dependencies ng Python
├── docs/                    # Mga dokumento sa maraming wika
│   └── README_*.md
├── i18n/                    # Mga file ng pagsasalin
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Naka-compile na executable
```

## File ng Configuration

Ang `config.json` file ay naka-save sa parehong direktoryo gaya ng EXE, na naglalaman ng lahat ng maaaring i-adjust na mga setting. Ang mga setting ay awtomatikong naka-save kapag binago.

## Lisensya

MIT License

## Tagagawa

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL ng Proyekto: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Mga Pagkilala

- LibreHardwareMonitor - Library ng pagsubaybay ng hardware
- psutil - Cross-platform na pagsubaybay ng system
- PyInstaller - Tool ng pagpapakete ng Python
