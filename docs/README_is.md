# ChipPeek

Léttur Windows vélbúnaðaeftirlitsflutningsforritshluti. Rauntímamat á CPU/GPU tíðni, hita, VRAM og minnisnotkun, alltaf á efstinu með fullskjársforritum.

> **Aðrar tungumál**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | **Íslenska** | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Eiginleikar

- **Rauntímamat**: CPU tíðni, CPU hiti, GPU tíðni, GPU hiti, VRAM notkun, minnisnotkun
- **Tvö sýningarmáti**: Hornaforritshluti / Efnistika, skiptum með einum smelli
- **Sérsníðanleg sýning**: Veldu frjálslega hvaða mælingar á að birta, skiptu milli prósenta/raun gilda
- **Alltaf á efstinu**: Verður ofan öllum gluggum, virkar í fullskjársleikjum
- **Sjálfvirkt stærð**: Breidd gluggans aðlagast sjálfkrafa innihaldi
- **Laganlegur stíll**: Gegnsæi glugga, gegnsæi bakgrunns, leturstærð alls hægt að breyta
- **Fjöltyngisstuðningur**: 20+ tungumál, greinir sjálfkrafa tungumál kerfis
- **þægilegur notkun**: Vinstri dræing til að færa, hægri smella valmynd fyrir hraðar stillingar, sjálfvirkt festist við skjárbrúnir
- **Sýnilegt samplingsbil**: 200ms - 3000ms hægt að breyta
- **Sjálfvirk ræsing**: Ræsir sjálfkrafa við Windows innskráningu
- **Lág auðlindanotkun**: Lágmarksáhrif í bakgrunni

## Fljótur byrjun

### Bein notkun

Sæktu `ChipPeek.exe` og tvísmelltu til að keyra (mun sjálfkrafa biðja um stjórnandarréttindi fyrir CPU hita og nákvæma tíðninlæsingu).

### Keyra af kóða

```bash
# Afrita geymsluna
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Settu upp ferla
pip install -r requirements.txt

# Keyra
python main.py
```

## Kerfiskröfur

- Windows 10 / Windows 11
- Stjórnandarréttindi (mælt með), annars getur CPU hiti og nákvæm tíðni ekki verið til staðar
- .NET Framework 4.7.2 eða nýrra (krafist af LibreHardwareMonitor)

## Byggja sem EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Eftir byggingu er EXE skráin staðsett á `dist/ChipPeek.exe`.

## Notkun

### Grundvallaraðgerðir

| Aðgerð | Lýsing |
|------|------|
| Vinstri dræing | Færa stöðu gluggans |
| Hægri smella | Opna valmynd (skipta um máta / stillingar / hætta) |
| Auto snap | Sjálfvirkt festist innan 20px frá skjárbrúnum |

### Sýningarmáti

- **Hornaforritshluti**: Allar mælingar raðar lóðrétt, hægt að setja í hvaða horni sem er af skjánum
- **Efnistika**: Allar mælingar raðar lárétt, miðjuð efst á skjánum sjálfgefið

### Stillingar

- **Sýningarmáti**: Hornaforritshluti / Efnistika
- **Staðsetning forritshluta**: Neðst til hægri / Neðst til vinstri / Efst til hægri / Efst til vinstri
- **Gegnsæi glugga**: 30% - 100% heildar gegnsæi gluggans
- **Gegnsæi bakgrunns**: 0% - 100% gegnsær bakgrunnur (texti verður skærur)
- **Samplingsbil**: 200ms - 3000ms data endurnýjunarhraði
- **Leturstærð**: 8 - 20 punkta letur
- **Tungumál**: 20+ tungumál, greinir sjálfkrafa tungumál kerfis
- **Sýnilegar mælingar**: Settu hvert mælingu á/annarð vegur
- **Sýningarform**: VRAM / Minni getur verið á milli prósenta eða raun gilda
- **Sjálfvirk ræsing**: Keyra sjálfkrafa þegar innskráð er í Windows

## Tækni

- **GUI**：Tkinter
- **Vélbúnaðargögn**：LibreHardwareMonitorLib (með pythonnet), psutil, pynvml (NVIDIA GPU backup)
- **Kerfisþáttun**：pywin32 (gluggi á efstinu, sjálfvirknis í skráningarsafni)
- **Pökkun**：PyInstaller

## Verkefnisuppbygging

```
ChipPeek/
├── main.py                  # Inngangspunktur
├── monitor_window.py        # UI gluggans og samskiptalógik
├── hardware_monitor.py      # Vélbúnaðargagnaöflun
├── config.py                # Stillingastjórnun
├── i18n.py                  # Þjóðvísun
├── generate_icon.py         # Táknmyndargerðarskript
├── admin.manifest           # UAC stjórnandarréttindaskýringarskjöl
├── app.ico                  # Forritstáknmynd
├── app.png                  # Táknmyndarforskoðun
├── requirements.txt         # Python ferlar
├── docs/                    # Fjöltyngis skjöl
│   └── README_*.md
├── i18n/                    # Þýðingarskrár
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # þýðanleg keyrsla
```

## Stillingarskrá

`config.json` skráin er vistuð í sömu möppu og EXE, sem inniheldur allar stillanlegar stillingar. Stillingarnar eru vistaðar sjálfkrafa þegar þær eru breyttar.

## Leyfi

MIT License

## Þróunarmaður

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- Verkefnisveffang: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Þakkir

- LibreHardwareMonitor - Vélbúnaðareftirlitsbókasafn
- psutil - Kerfiseftirlit yfir marga vettvanga
- PyInstaller - Python pakkunarverkfæri
