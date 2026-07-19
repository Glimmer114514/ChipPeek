# ChipPeek

Lehký plovoucí widget pro monitorování hardwaru ve Windows. Sledování frekvence CPU/GPU, teploty, VRAM a využití paměti v reálném čase, vždy navrchu, včetně aplikací na celou obrazovku.

> **Jiné jazyky**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | **Čeština** | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Funkce

- **Monitorování v reálném čase**: frekvence CPU, teplota CPU, frekvence GPU, teplota GPU, využití VRAM, využití paměti
- **Dva režimy zobrazení**: widget v rohu / horní lišta, přepnutí jedním kliknutím
- **Přizpůsobitelné zobrazení**: volně si vyberte, které metriky zobrazit, přepínejte mezi procentuálními/skutečnými hodnotami
- **Vždy navrchu**: zůstává nad všemi okny, funguje i ve hrách na celou obrazovku
- **Automatická velikost**: šířka okna se automaticky přizpůsobí obsahu
- **Nastavitelný styl**: průhlednost okna, průhlednost pozadí, velikost písma - vše lze nastavit
- **Podpora více jazyků**: 20+ jazyků, automaticky rozpozná jazyk systému
- **Pohodlné ovládání**: přesouvejte tažením levým tlačítkem, menu pravým tlačítkem pro rychlá nastavení, automatické přichytávání k okrajům obrazovky
- **Nastavitelná vzorkovací frekvence**: 200ms - 3000ms nastavitelné
- **Automatické spuštění**: spouští se automaticky při přihlášení do Windows
- **Nízká spotřeba prostředků**: minimální nároky na prostředky v pozadí

## Rychlý start

### Přímé použití

Stáhněte si `ChipPeek.exe` a dvakrát klikněte pro spuštění (automaticky požádá o oprávnění správce pro teplotu CPU a přesné čtení frekvence).

### Spuštění ze zdrojového kódu

```bash
# Naklonujte repozitář
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Nainstalujte závislosti
pip install -r requirements.txt

# Spusťte
python main.py
```

## Systémové požadavky

- Windows 10 / Windows 11
- Oprávnění správce (doporučeno), jinak teplota CPU a přesná frekvence nemusí být dostupné
- .NET Framework 4.7.2 nebo vyšší (vyžadováno knihovnou LibreHardwareMonitor)

## Sestavení jako EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Po sestavení se EXE soubor nachází v `dist/ChipPeek.exe`.

## Použití

### Základní operace

| Operace | Popis |
|------|------|
| Tažení levým tlačítkem | Přesunutí okna |
| Pravé tlačítko | Otevření menu (změna režimu / nastavení / ukončení) |
| Automatické přichytávání | Automaticky se přichytí do 20px od okrajů obrazovky |

### Režimy zobrazení

- **Widget v rohu**: všechny metriky uspořádané svisle, lze umístit do kterékoli části obrazovky
- **Horní lišta**: všechny metriky uspořádané vodorovně, standardně zarovnány uprostřed horní části obrazovky

### Nastavení

- **Režim zobrazení**: widget v rohu / horní lišta
- **Pozice widgetu**: vpravo dole / vlevo dole / vpravo nahoře / vlevo nahoře
- **Průhlednost okna**: 30% - 100% celková průhlednost okna
- **Průhlednost pozadí**: 0% - 100% průhledné pozadí (text zůstává čistý)
- **Vzorkovací interval**: 200ms - 3000ms frekvence obnovy dat
- **Velikost písma**: 8 - 20 bodů
- **Jazyk**: 20+ jazyků, automaticky rozpozná jazyk systému
- **Zobrazované metriky**: každou metriku lze nezávisle zapnout/vypnout
- **Formát zobrazení**: VRAM / paměť lze přepnout na procenta nebo skutečné hodnoty
- **Automatické spuštění**: spouštět automaticky při přihlášení do Windows

## Technologický stack

- **GUI**：Tkinter
- **Hardware data**：LibreHardwareMonitorLib (přes pythonnet), psutil, pynvml (záložní řešení pro NVIDIA GPU)
- **Systémová integrace**：pywin32 (okno vždy navrchu, registr automatického spuštění)
- **Balení**：PyInstaller

## Struktura projektu

```
ChipPeek/
├── main.py                  # Vstupní bod
├── monitor_window.py        # UI okna a logika interakce
├── hardware_monitor.py      # Sběr dat hardwaru
├── config.py                # Správa konfigurace
├── i18n.py                  # Internacionalizace
├── generate_icon.py         # Skript pro generování ikon
├── admin.manifest           # Manifest oprávnění správce UAC
├── app.ico                  # Ikona aplikace
├── app.png                  # Náhled ikony
├── requirements.txt         # Závislosti Python
├── docs/                    # Vícejazyčná dokumentace
│   └── README_*.md
├── i18n/                    # Překladové soubory
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Sestavený spustitelný soubor
```

## Konfigurační soubor

Soubor `config.json` se ukládá ve stejném adresáři jako EXE a obsahuje všechna nastavitelná nastavení. Nastavení se automaticky ukládají při změně.

## Licence

MIT License

## Vývojář

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL projektu: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Poděkování

- LibreHardwareMonitor - Knihovna pro monitorování hardwaru
- psutil - Monitorování systému napříč platformami
- PyInstaller - Nástroj pro balení programů v Pythonu
