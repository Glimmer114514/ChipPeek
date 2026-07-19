# ChipPeek

Malpeza ŝveba fenestreto por Windows aparatmonitorado. Realtempa monitorado de CPU/GPU frekvenco, temperaturo, VRAM kaj memoro uzado, ĉiam supre, eĉ ĉe plenekranaj programoj.

> **Aliaj Lingvoj**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | **Esperanto**

## Trajtoj

- **Realtempa monitorado**: CPU frekvenco, CPU temperaturo, GPU frekvenco, GPU temperaturo, VRAM uzado, memoro uzado
- **Du ekranreĝimoj**: Angula fenestreto / Supra breto, unu-klaka ŝanĝo
- **Agordebla ekrano**: Libere elektu kiujn metrikojn montri, ŝanĝu inter procentoj / realaj valoroj
- **Ĉiam supre**: Restas super ĉiuj fenestroj, funkcias en plenekranaj ludoj
- **Aŭtomata grandeco**: Fenestro larĝo aŭtomate adaptas al enhavo
- **Alĝustigebla stilo**: Fenestro opakeco, fono travideco, tipara grandezo ĉio alĝustigebla
- **Multlingva subteno**: 20+ lingvoj, aŭtomate detektas sisteman lingvon
- **Opertura funkciado**: Maldekstre movi por ŝovi, dekstra klaka menuo por rapidaj agordoj, aŭtomata altiro al ekranaj randoj
- **Konfigurebla provado**: 200ms - 3000ms alĝustigebla
- **Aŭtomata lanĉo**: Lanĉi aŭtomate ĉe Windows ensaluto
- **Malalta rimeduzo**: Minimuma spuraĵo en fono

## Rapida Komenco

### Rekta Uzo

Elŝutu `ChipPeek.exe` kaj duoble klaku por ruli (aŭtomate petos administrajn rajtojn por CPU temperaturo kaj preciza frekvenca legado).

### Ruli de Fonto

```bash
# Klonu la deponejon
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Instalu dependojn
pip install -r requirements.txt

# Ruli
python main.py
```

## Sistemaj Postuloj

- Windows 10 / Windows 11
- Administraj rajtoj (rekomenditaj), alie CPU temperaturo kaj preciza frekvenco eble ne haveblos
- .NET Framework 4.7.2 aŭ pli alta (postulata de LibreHardwareMonitor)

## Konstrui kiel EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Post konstruado, la EXE dosiero troviĝas ĉe `dist/ChipPeek.exe`.

## Uzado

### Bazaj Operacioj

| Ago | Priskribo |
|------|------|
| Maldekstre movi | Ŝovi fenestran pozicion |
| Dekstre klaki | Malfermi menuon (ŝanĝi reĝimon / agordojn / eliri) |
| Aŭtomata altiro | Aŭtomate altiras ene de 20px de ekranaj randoj |

### Ekranreĝimoj

- **Angula Fenestreto**: Ĉiuj metrikoj aranĝitaj vertikale, povas esti metitaj en ajnan ekranan angulon
- **Supra Breto**: Ĉiuj metrikoj aranĝitaj horizontale, defaŭlte centrita supre de la ekrano

### Agordoj

- **Ekranreĝimo**: Angula fenestreto / Supra breto
- **Pozicio de fenestreto**: Malsupra dekstra / Malsupra maldekstra / Supra dekstra / Supra maldekstra
- **Opakeco de fenestro**: 30% - 100% ĝenerala fenestro travideco
- **Travideco de fono**: 0% - 100% fono travidebla (teksto restas akra)
- **Prova intervalo**: 200ms - 3000ms datumajn ĝisdatigotan rapidecon
- **Tipara grandezo**: 8 - 20 punktoj tiparo
- **Lingvo**: 20+ lingvoj, aŭtomate detektas sisteman lingvon
- **Montri metrikojn**: Ŝalti ĉian metrikon sendepende
- **Ekranformato**: VRAM / Memoro povas ŝanĝi inter procentoj aŭ realaj valoroj
- **Aŭtomata lanĉo**: Ruli aŭtomate kiam ensalutas en Windows

## Teknika Staplo

- **GUI**：Tkinter
- **Aparataj datenoj**：LibreHardwareMonitorLib (per pythonnet), psutil, pynvml (NVIDIA GPU rezervo)
- **Sistema integriĝo**：pywin32 (fenestro plej supra, aŭtomata-lanĉa registrejo)
- **Pakado**：PyInstaller

## Projekta Strukturo

```
ChipPeek/
├── main.py                  # Enirejo
├── monitor_window.py        # Fenestro UI kaj interaga logiko
├── hardware_monitor.py      # Aparataj datumoj kolektado
├── config.py                # Agorda administrado
├── i18n.py                  # Internaciigo
├── generate_icon.py         # Skripto por ikono generado
├── admin.manifest           # UAC administra rajto manifesto
├── app.ico                  # Aplika ikono
├── app.png                  # Ikona antaŭrigardo
├── requirements.txt         # Python dependoj
├── docs/                    # Multlingvaj dokumentoj
│   └── README_*.md
├── i18n/                    # Tradukaj dosieroj
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Kompilita ekzekuteblo
```

## Agorda Dosiero

La `config.json` dosiero estas konservita en la sama dosierujo kiel la EXE, enhavante ĉiujn alĝustigeblajn agordojn. Agordoj estas konservitaj aŭtomate kiam ŝanĝitaj.

## Licenco

MIT License

## Programisto

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- Projekta URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Dankoj

- LibreHardwareMonitor - Aparatmonitora biblioteko
- psutil - Transplata sistemmonitorado
- PyInstaller - Python paka ilo
