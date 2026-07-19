# ChipPeek

En lettvekts flytende maskinvareovervåkingswidget for Windows. Realtidsovervåking av CPU/GPU-frekvens, temperatur, VRAM og minnebruk, alltid øverst også i fullskjermsapp.

> **Andre språk**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | **Norsk** | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Funksjoner

- **Realtimeovervåking**: CPU-frekvens, CPU-temperatur, GPU-frekvens, GPU-temperatur, VRAM-bruk, minnebruk
- **To visningsmoduser**: Hjørnewidget / Toppliste, ett-klikk bytte
- **Tilpassbar visning**: Velg fritt hvilke måleverdier som skal vises, bytt mellom prosent/faktiske verdier
- **Alltid øverst**: Forblir over alle vinduer, fungerer i fullskjermspill
- **Automatisk størrelse**: Vindusbredden justeres automatisk etter innholdet
- **Justerbar stil**: Vindusopasitet, bakgrunnsgjennomsiktighet, skriftstørrelse - alt kan justeres
- **Flerspråklig støtte**: 20+ språk, oppdager automatisk systemspråket
- **Enkel håndtering**: Venstreklikk og dra for å flytte, høyreklikkmeny for raske innstillinger, automatisk feste til skjermkantene
- **Konfigurerbar samplingsfrekvens**: 200ms - 3000ms justerbar
- **Autostart**: Starter automatisk ved Windows-pålogging
- **Lav resursbruk**: Minimal fotavtrykk i bakgrunnen

## Hurtigstart

### Direkte bruk

Last ned `ChipPeek.exe` og dobbeltklikk for å kjøre (behov automatisk administratorrettigheter for CPU-temperatur og nøyaktig frekvensavlesning).

### Kjør fra kildekode

```bash
# Klon depotet
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Installer avhengigheter
pip install -r requirements.txt

# Kjør
python main.py
```

## Systemkrav

- Windows 10 / Windows 11
- Administratorrettigheter (anbefalt), ellers kan CPU-temperatur og nøyaktig frekvens ikke være tilgjengelig
- .NET Framework 4.7.2 eller høyere (kreves av LibreHardwareMonitor)

## Bygg som EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Etter bygging finnes EXE-filen på `dist/ChipPeek.exe`.

## Bruk

### Grunnleggende operasjoner

| Handling | Beskrivelse |
|------|------|
| Venstreklikk og dra | Flytt vindusposisjon |
| Høyreklikk | Åpne meny (bytt modus / innstillinger / avslutt) |
| Automatisk festing | Fester automatisk innen 20px fra skjermkantene |

### Visningsmoduser

- **Hjørnewidget**: Alle måleverdier ordnet vertikalt, kan plasseres i ethvert hjørne av skjermen
- **Toppliste**: Alle måleverdier ordnet horisontalt, sentrert øverst på skjermen som standard

### Innstillinger

- **Visningsmodus**: Hjørnewidget / Toppliste
- **Widgetposisjon**: Nederst til høyre / Nederst til venstre / Øverst til høyre / Øverst til venstre
- **Vindusopasitet**: 30% - 100% total vindusgjennomsiktighet
- **Bakgrunnsgjennomsiktighet**: 0% - 100% bakgrunnsgjennomsiktig (tekst forblir skarp)
- **Samplingsintervall**: 200ms - 3000ms dataoppdateringshastighet
- **Skriftstørrelse**: 8 - 20 punkter
- **Språk**: 20+ språk, oppdager automatisk systemspråket
- **Visningsverdier**: Slå av/på hver måleverdi uavhengig
- **Visningsformat**: VRAM / Minne kan bytte mellom prosent eller faktiske verdier
- **Autostart**: Kjør automatisk når du logger på Windows

## Teknistabel

- **GUI**：Tkinter
- **Maskinvare-data**：LibreHardwareMonitorLib (via pythonnet), psutil, pynvml (alternativ for NVIDIA GPU)
- **Systemintegrasjon**：pywin32 (vindu alltid øverst, autostartregister)
- **Pakking**：PyInstaller

## Prosjektstruktur

```
ChipPeek/
├── main.py                  # Startpunkt
├── monitor_window.py        # Vindu-UI og interaksjonslogikk
├── hardware_monitor.py      # Innhenting av maskinvare-data
├── config.py                # Konfigurasjonsstyring
├── i18n.py                  # Internasjonalisering
├── generate_icon.py         # Ikon-genereringsskript
├── admin.manifest           # UAC-adminrettighetsmanifest
├── app.ico                  # Applikasjonsikon
├── app.png                  # Ikon forhåndsvisning
├── requirements.txt         # Python-avhengigheter
├── docs/                    # Flerspråklig dokumentasjon
│   └── README_*.md
├── i18n/                    # Oversettelsesfiler
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Kompilert kjørbar fil
```

## Konfigurasjonsfil

`config.json`-filen lagres i samme mappe som EXE-filen og inneholder alle justerbare innstillinger. Innstillingene lagres automatisk når de endres.

## Lisens

MIT License

## Utvikler

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- Prosjekt-URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Kreditter

- LibreHardwareMonitor - Maskinvareovervåkingsbibliotek
- psutil - Plattformuavhengig systemovervåking
- PyInstaller - Python-pakkingsverktøy
