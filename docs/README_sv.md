# ChipPeek

En lättviktsflytande hårdvaruövervakningswidget för Windows. Realtidsövervakning av CPU/GPU-frekvens, temperatur, VRAM och minnesanvändning, alltid ovanpå även i helskärmsläge.

> **Andra språk**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | **Svenska** | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Funktioner

- **Realtidsövervakning**: CPU-frekvens, CPU-temperatur, GPU-frekvens, GPU-temperatur, VRAM-användning, minnesanvändning
- **Dubbla visningslägen**: Hörnwidget / Topplist, ett-klicksbyte
- **Anpassningsbar visning**: Välj fritt vilka mätvärden som ska visas, växla mellan procent/faktiska värden
- **Alltid ovanpå**: Förblir ovanför alla fönster, fungerar i helskärmsspel
- **Automatisk storlek**: Fönsterbredden justeras automatiskt efter innehållet
- **Justerbar stil**: Fönsteropacitet, bakgrundstransparens, teckenstorlek - allt går att justera
- **Flera språk stöds**: 20+ språk, upptäcker automatiskt systemspråket
- **Kvickhantering**: Vänsterklicka och dra för att flytta, högerklicksmeny för snabbinställningar, automatisk fästning mot skärmkanter
- **Konfigurerbar samplingsfrekvens**: 200ms - 3000ms justerbar
- **Autostart**: Startar automatiskt vid Windows-inloggning
- **Låg resursanvändning**: Minimal fotavtryck i bakgrunden

## Snabbstart

### Direkt användning

Ladda ner `ChipPeek.exe` och dubbelklicka för att köra (begär automatiskt administratörsbehörighet för CPU-temperatur och korrekt frekvensavläsning).

### Kör från källkod

```bash
# Klona repositoryt
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Installera beroenden
pip install -r requirements.txt

# Kör
python main.py
```

## Systemkrav

- Windows 10 / Windows 11
- Administratörsbehörighet (rekommenderas), annars kan CPU-temperatur och korrekt frekvens inte vara tillgänglig
- .NET Framework 4.7.2 eller högre (krävs av LibreHardwareMonitor)

## Bygg som EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Efter byggandet finns EXE-filen på `dist/ChipPeek.exe`.

## Användning

### Grundläggande åtgärder

| Åtgärd | Beskrivning |
|------|------|
| Vänsterklicka och dra | Flytta fönsterposition |
| Högerklicka | Öppna meny (byta läge / inställningar / avsluta) |
| Automatisk fästning | Fäster automatiskt inom 20px från skärmkanterna |

### Visningslägen

- **Hörnwidget**: Alla mätvärden ordnade vertikalt, kan placeras i valfritt skärmhörn
- **Topplist**: Alla mätvärden ordnade horisontellt, centrerad längst upp på skärmen som standard

### Inställningar

- **Visningsläge**: Hörnwidget / Topplist
- **Widgetposition**: Nederst till höger / Nederst till vänster / Överst till höger / Överst till vänster
- **Fönsteropacitet**: 30% - 100% total fönstertransparens
- **Bakgrundstransparens**: 0% - 100% bakgrundstransparent (text förblir skarp)
- **Samplingsintervall**: 200ms - 3000ms datauppdateringshastighet
- **Teckenstorlek**: 8 - 20 punkter
- **Språk**: 20+ språk, upptäcker automatiskt systemspråket
- **Visningsvärden**: Växla varje mätvärde oberoende av varandra
- **Visningsformat**: VRAM / Minne kan växla mellan procent eller faktiska värden
- **Autostart**: Kör automatiskt när du loggar in på Windows

## Teknikstack

- **GUI**：Tkinter
- **Hårdvarudata**：LibreHardwareMonitorLib (via pythonnet), psutil, pynvml (alternativ för NVIDIA GPU)
- **Systemintegration**：pywin32 (fönster alltid ovanpå, autostartregister)
- **Paketering**：PyInstaller

## Projektstruktur

```
ChipPeek/
├── main.py                  # Startpunkt
├── monitor_window.py        # Fönster-UI och interaktionslogik
├── hardware_monitor.py      # Hårdvarudatainsamling
├── config.py                # Konfigurationshantering
├── i18n.py                  # Internationalisering
├── generate_icon.py         # Ikongeneringsskript
├── admin.manifest           # UAC-adminbehörighetsmanifest
├── app.ico                  # Applikationsikon
├── app.png                  # Ikonförhandsgranskning
├── requirements.txt         # Python-beroenden
├── docs/                    # Flerspråkig dokumentation
│   └── README_*.md
├── i18n/                    # Översättningsfiler
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Kompilerad körbar fil
```

## Konfigurationsfil

`config.json`-filen sparas i samma katalog som EXE-filen och innehåller alla justerbara inställningar. Inställningar sparas automatiskt när de ändras.

## Licens

MIT License

## Utvecklare

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- Projekt-URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Tack

- LibreHardwareMonitor - Hårdvaruövervakningsbibliotek
- psutil - Plattformsoberoende systemövervakning
- PyInstaller - Python-paketeringsverktyg
