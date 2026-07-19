# ChipPeek

Egy könnyű súlyú lebegő hardvermonitorozó widget Windowshez. Valós idejű CPU/GPU frekvencia, hőmérséklet, VRAM és memória használat figyelése, mindig felül, beleértve a teljes képernyős alkalmazásokat is.

> **Egyéb nyelvek**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | **Magyar** | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Jellemzők

- **Valós idejű monitorozás**: CPU frekvencia, CPU hőmérséklet, GPU frekvencia, GPU hőmérséklet, VRAM használat, memória használat
- **Két megjelenítési mód**: sarok widget / felső sáv, egy kattintással váltás
- **Testreszabható megjelenítés**: szabadon választhatja, melyik metrikát jelenítse meg, százalék/tényleges értékek közötti váltás
- **Mindig felül**: minden ablak felett marad, teljes képernyős játékokban is működik
- **Automatikus méret**: az ablak szélessége automatikusan igazodik a tartalomhoz
- **Beállítható stílus**: ablak átlátszóság, háttér átlátszóság, betűméret - mind beállítható
- **Többnyelvű támogatás**: 20+ nyelv, automatikusan felismeri a rendszer nyelvét
- **Kényelmes kezelés**: bal gombbal húzva mozgatás, jobb klikk menü gyors beállításokhoz, automatikus rögzítés a képernyő szélére
- **Beállítható mintavételi gyakoriság**: 200ms - 3000ms beállítható
- **Automatikus indítás**: automatikusan elindul a Windows bejelentkezéskor
- **Alacsony erőforrás-használat**: minimális terhelés a háttérben

## Gyors kezdés

### Közvetlen használat

Töltse le a `ChipPeek.exe` fájlt, és kattintson duplán a futtatáshoz (automatikusan rendszergazdai engedélyt kér a CPU hőmérséklethez és a pontos frekvenciaolvasáshoz).

### Futtatás forráskódból

```bash
# Tároló klónozása
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Függőségek telepítése
pip install -r requirements.txt

# Futtatás
python main.py
```

## Rendszerkövetelmények

- Windows 10 / Windows 11
- Rendszergazdai engedélyek (ajánlott), egyébként a CPU hőmérséklet és a pontos frekvencia nem lehet elérhető
- .NET Framework 4.7.2 vagy magasabb (a LibreHardwareMonitor igényli)

## Összeállítás EXE-ként

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Az összeállítás után az EXE fájl a `dist/ChipPeek.exe` helyen található.

## Használat

### Alapvető műveletek

| Művelet | Leírás |
|------|------|
| Bal klikk húzás | Ablak helyzetének mozgatása |
| Jobb klikk | Menü megnyitása (mód váltás / beállítások / kilépés) |
| Automatikus rögzítés | Automatikusan rögzül a képernyő szélétől 20px távolságon belül |

### Megjelenítési módok

- **Sarok widget**: összes metrika függőlegesen rendezve, elhelyezhető a képernyő bármelyik sarkában
- **Felső sáv**: összes metrika vízszintesen rendezve, alapértelmezésben középen a képernyő tetején

### Beállítások

- **Megjelenítési mód**: sarok widget / felső sáv
- **Widget helye**: jobb alsó / bal alsó / jobb felső / bal felső
- **Ablak átlátszóság**: 30% - 100% teljes ablak átlátszóság
- **Háttér átlátszóság**: 0% - 100% háttér átlátszó (a szöveg éles marad)
- **Mintavételi intervallum**: 200ms - 3000ms adatfrissítési gyakoriság
- **Betűméret**: 8 - 20 pont
- **Nyelv**: 20+ nyelv, automatikusan felismeri a rendszer nyelvét
- **Megjelenítendő metrikák**: minden metrika külön kapcsolható be/ki
- **Megjelenítési formátum**: VRAM / Memória váltás százalék vagy tényleges értékek között
- **Automatikus indítás**: automatikus futtatás Windows bejelentkezéskor

## Technológiai verem

- **GUI**：Tkinter
- **Hardver adatok**：LibreHardwareMonitorLib (pythonnet segítségével), psutil, pynvml (NVIDIA GPU tartalék)
- **Rendszerintegráció**：pywin32 (ablak mindig felül, automatikus indítási beállításjegyzék)
- **Csomagolás**：PyInstaller

## Projekt szerkezete

```
ChipPeek/
├── main.py                  # Belépési pont
├── monitor_window.py        # Ablak UI és interakciós logika
├── hardware_monitor.py      # Hardver adatgyűjtés
├── config.py                # Konfiguráció kezelése
├── i18n.py                  # Nemzetközivé tétel
├── generate_icon.py         # Ikon generáló szkript
├── admin.manifest           # UAC rendszergazdai engedély manifest
├── app.ico                  # Alkalmazás ikon
├── app.png                  # Ikon előnézet
├── requirements.txt         # Python függőségek
├── docs/                    # Többnyelvű dokumentáció
│   └── README_*.md
├── i18n/                    # Fordítási fájlok
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Összeállított futtatható fájl
```

## Konfigurációs fájl

A `config.json` fájl az EXE-hez hasonló mappában kerül mentésre, és tartalmazza az összes beállítható beállítást. A beállítások automatikusan mentésre kerülnek módosításkor.

## Licenc

MIT License

## Fejlesztő

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- Projekt URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Köszönet

- LibreHardwareMonitor - Hardver monitorozó könyvtár
- psutil - Platformfüggetlen rendszer monitorozás
- PyInstaller - Python csomagoló eszköz
