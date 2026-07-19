# ChipPeek

Erfaun monitro caledn Windows ysgafn. Mae'n monitro amlder CPU/GPU, tymheredd, VRAM, a defnydd cof mewn real-amser, yn aros ar frig pob ffenestr gan gynnwys appiau llawnsgrin.

> **Ieithoedd Eraill**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | **Cymraeg** | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Nodweddion

- **Monitro real-amser**: Amlder CPU, tymheredd CPU, amlder GPU, tymheredd GPU, defnydd VRAM, defnydd cof
- **Dau fodddangos**: Widget cornel / Bar brig, newid gydag un cliciad
- **Dangos addasadwy**: Dewiswch yn rhydd pa fesurau i'w dangos, newid rhwng canran/gwerthoedd gwirioneddol
- **Ar bob tro ar frig**: Yn aros uwchben pob ffenestr, yn gweithio mewn gemau llawnsgrin
- **Maint awtomatig**: Lled y ffenestr yn addasu'n awtomatig i gyd-fynd â'r cynnwys
- **Arddull addasadwy**: Tryloywder ffenestr, tryloywder cefndir, maint ffont i gyd yn addasadwy
- **Cefnogaeth amlieithog**: 20+ iaith, yn canfod iaith y system yn awtomatig
- **Gweithred hudol**: Llusgo chwith i symud, dewislen clic dde ar gyfer gosodiadau cyflym, cysgodi'n awtomatig i gyrion y sgrin
- **Samplu addasadwy**: 200ms - 3000ms yn addasadwy
- **Cychwyn gyda'r system**: Cychwyn'n awtomatig wrth fewngofnodi i Windows
- **Defnydd adnoddau isaf**: Troedfedd lleiaf yn y cefndir

## Cychwyn Cyflym

### Defnyddio'n Uniongyrchol

Lawrlwythwch `ChipPeek.exe` a chlicio dwbl i'w redeg (bydd yn gofyn am hawliau gweinyddol yn awtomatig ar gyfer darllen tymheredd CPU ac amlder gywir).

### Redeg o'r Ffynhonnell

```bash
# Clonio'r storfa
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Gosod dibenniadau
pip install -r requirements.txt

# Rhedeg
python main.py
```

## Gofynion System

- Windows 10 / Windows 11
- Hawliau gweinyddol (argymhorol), fel arall gall tymheredd CPU ac amlder gywir ddim bod ar gael
- .NET Framework 4.7.2 neu uwch (angen gan LibreHardwareMonitor)

## Begu'n EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Ar ôl i'r adeilad gwblhau, mae'r ffeil EXE yn `dist/ChipPeek.exe`.

## Defnydd

### Gweithrediadau Sylfaenol

| Gweithred | Disgrifiad |
|------|------|
| Llusgo chwith | Symud safle'r ffenestr |
| Clic dde | Agor dewislen (newid modd / gosodiadau / gadael) |
| Cysgodi awtomatig | Yn cysgodi'n awtomatig o fewn 20px o gyrion y sgrin |

### Moddau Dangos

- **Widget Cornel**: Pob mesur wedi'i threfnu'n fertigol, gellir ei roi mewn unrhyw gornel o'r sgrin
- **Bar Brig**: Pob mesur wedi'i threfnu'n lorweddol, wedi'i ganolbrychu ar frig y sgrin yn ddiofyn

### Gosodiadau

- **Modd dangos**: Widget cornel / Bar brig
- **Lleoliad y widget**: Dde'r gwaelod / Chwith y gwaelod / Dde'r brig / Chwith y brig
- **Tryloywder y ffenestr**: 30% - 100% tryloywder cyffredinol y ffenestr
- **Tryloywder y cefndir**: 0% - 100% tryloywder cefndir (mae'r testun yn aros clir)
- **Ymweliad samplu**: 200ms - 3000ms cyflymder adnewyddu data
- **Maint y ffont**: 8 - 20 pwynt ffont
- **Iaith**: 20+ iaith, yn canfod iaith y system yn awtomatig
- **Mesurau dangos**: Toglo pob mesur yn annibynnol
- **Fformat dangos**: VRAM / Cof gall newid rhwng canran neu werthoedd gwirioneddol
- **Cychwyn gyda'r system**: Rhedeg yn awtomatig wrth fewngofnodi i Windows

## Tech Stack

- **GUI**：Tkinter
- **Data caledn**：LibreHardwareMonitorLib (trwy pythonnet), psutil, pynvml (GPU NVIDIA wrth gefn)
- **Integreiddio system**：pywin32 (ffenestr ar frig, cofrestriad cychwyn awtomatig)
- **Pecynnu**：PyInstaller

## Strwythur y Prosiect

```
ChipPeek/
├── main.py                  # Pwynt mynediad
├── monitor_window.py        # UI ffenestr a rhesymeg rhyngweithio
├── hardware_monitor.py      # Casglu data caledn
├── config.py                # Rheoli gosodiadau
├── i18n.py                  # Rhyngwladoli
├── generate_icon.py         # Sgript cynhyrchu eicon
├── admin.manifest           # Maniffest hawliau gweinyddol UAC
├── app.ico                  # Eicon y rhaglen
├── app.png                  # Rhagolwg eicon
├── requirements.txt         # Dibenniadau Python
├── docs/                    # Dogfennau amlieithog
│   └── README_*.md
├── i18n/                    # Ffeiliau cyfieithu
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # DLL LibreHardwareMonitorLib
└── dist/
    └── ChipPeek.exe         # Gweithrediad wedi'i grynhoi
```

## Ffeil Ffurfwedd

Mae'r ffeil `config.json` wedi'i chadw yn yr un cyfeiriadur â'r EXE, gan gynnwys pob gosodiad addasadwy. Mae gosodiadau'n cael eu cadw'n awtomatig pan fyddant yn cael eu newid.

## Trwydded

MIT License

## Datblygydd

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL y Prosiect: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Diolchiadau

- LibreHardwareMonitor - Llyfrgell monitro caledn
- psutil - Monitro system draws-ffurflen
- PyInstaller - Erfyn pecynnu Python
