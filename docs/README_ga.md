# ChipPeek

Giúirléid shnámhach éadrom do mhonatóireacht crua-earraí Windows. Déanann sé monatóireacht i bhfíor-am ar mhinicíocht CPU/GPU, teocht, VRAM, agus úsáid cuimhne, agus bíonn sé i gcónaí ar barr fiú in aicearráidí iomlána.

> **Teangacha Eile**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | **Gaeilge** | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Gnéithe

- **Monatóireacht i bhfíor-am**: Minicíocht CPU, teocht CPU, minicíocht GPU, teocht GPU, úsáid VRAM, úsáid cuimhne
- **Dhá mhodh taispeána**: Giúirléid coirnéil / Barra barr, aistriú le cliceáil amháin
- **Taispeán inoiriúnaithe**: Roghnaigh go saor cé na méadrachtaí atá le taispeáint, malartaigh idir céatadán agus luachanna iarbhír
- **Ar barr i gcónaí**: Fanann sé os cionn na bhfuinneog go léir, oibríonn sé i gcluichí iomlána
- **Auto-méid**: Choigeartaíonn leithead na fuinneoige go huathoibríoch d'oirfeas a bhfuil inti
- **Stíl inchoigeartaithe**: Teimhneacht na bhfuinneog, trédhearcacht an chúlra, méid an chló - is féidir iad go léir a choigeartú
- **Tacaíocht ilteangach**: 20+ teanga, braitheadh uathoibríoch ar theanga an chórais
- **Oibríocht áisiúil**: Tarraingt ar chlé le bogadh, roghchlár cliceáil ar dheis le haghaidh socruithe tapa, greamaigh go huathoibríoch le hedges an scáileáin
- **Sampláil inchoigeartaithe**: 200ms - 3000ms inchoigeartaithe
- **Auto-thosú**: Seol go huathoibríoch nuair a logálann tú isteach i Windows
- **Úsáid íseal acmhainní**: Lorg íosta sa chúlra

## Tús Tapa

### Úsáid Dhíreach

Íoslódáil `ChipPeek.exe` agus cliceáil faoi dhó le rith (iarrfaidh sé pribhléidí riarthóra go huathoibríoch le haghaidh teocht CPU agus léamh cruinn minicíochta).

### Rith ón bhFoinse

```bash
# Clónáil an stór
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Suiteáil na spleáchas
pip install -r requirements.txt

# Rith
python main.py
```

## Ceanglais Chórais

- Windows 10 / Windows 11
- Pribhléidí riarthóra (molta), murach sin seans nach mbeidh teocht CPU agus minicíocht chruinn ar fáil
- .NET Framework 4.7.2 nó níos airde (de dhíth ar LibreHardwareMonitor)

## Tóg mar EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Tar éis an tógála, tá an comhad EXE suite ag `dist/ChipPeek.exe`.

## Úsáid

### Oibríochtaí Bunúsacha

| Gníomh | Cur síos |
|------|------|
| Tarraingt ar chlé | Bog suíomh na fuinneoige |
| Cliceáil ar dheis | Oscail roghchlár (athraigh mód / socruithe / scaoil) |
| Auto snap | Greamaíonn go huathoibríoch laistigh de 20px de hedges an scáileáin |

### Móid Taispeána

- **Giúirléid Coirnéil**: Gach méadracht eagraithe go hingearach, is féidir a chur in aon chorner den scáileán
- **Barra Barr**: Gach méadracht eagraithe go cothrománach, lárnaithe ag barr an scáileáin de réir réamhshocraithe

### Socruithe

- **Modh taispeána**: Giúirléid coirnéil / Barra barr
- **Suíomh na giúirléide**: Íochtar deis / Íochtar clé / Barr deis / Barr clé
- **Teimhneacht na bhfuinneog**: 30% - 100% trédhearcacht iomlán na bhfuinneog
- **Trédhearcacht an chúlra**: 0% - 100% cúlra trédhearcach (fanann an téacs soiléir)
- **Eatramh samplála**: 200ms - 3000ms ráta athnuachana sonraí
- **Méid an chló**: 8 - 20 pointí cló
- **Teanga**: 20+ teanga, braitheadh uathoibríoch ar theanga an chórais
- **Méadrachtaí taispeána**: Cas gach méadracht ar siúl/as go neamhspleách
- **Formáid taispeána**: Is féidir le VRAM / Cuimhne a bheith idir céatadán nó luachanna iarbhír
- **Auto-thosú**: Rith go huathoibríoch nuair a logálann tú isteach i Windows

## Teicneolaíocht

- **GUI**：Tkinter
- **Sonraí crua-earraí**：LibreHardwareMonitorLib (trí pythonnet), psutil, pynvml (NVIDIA GPU fallback)
- **Comhtháthú córais**：pywin32 (window topmost, auto-start registry)
- **Pacáistiú**：PyInstaller

## Struchtúr an Tionscadail

```
ChipPeek/
├── main.py                  # Pointí iontrála
├── monitor_window.py        # UI fuinneoige agus lóigic idirghníomhaíochta
├── hardware_monitor.py      # Bailiú sonraí crua-earraí
├── config.py                # Bainistíocht cumraíochta
├── i18n.py                  # Idirnáisiúnú
├── generate_icon.py         # Script giniúint íocón
├── admin.manifest           # Manifest pribhléide riarthóra UAC
├── app.ico                  # Íocán na feidhmchláir
├── app.png                  # Réamhamharc íocón
├── requirements.txt         # Spleáchas Python
├── docs/                    # Doiciméid ilteangacha
│   └── README_*.md
├── i18n/                    # Comhaid aistriúcháin
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Inrite tiomsaithe
```

## Comhad Cumraíochta

Tá an comhad `config.json` sábháilte san eolaire céanna leis an EXE, agus tá na socruithe go léir inchoigeartaithe ann. Sábháiltear na socruithe go huathoibríoch nuair a athraítear iad.

## Ceadúnas

MIT License

## Forbróir

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL an Tionscadail: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Creidmhigh

- LibreHardwareMonitor - Leabharlann monatóireachta crua-earraí
- psutil - Monatóireacht chóras tras-ardán
- PyInstaller - Uirlis phacáistiú Python
