# ChipPeek

Isithonzi sokulungisa izinhlelo ezibekwa ezintathini ze-Windows ezisendlala. Ukulungiswa kwesikhathi sangempela kwamandla we-CPU/GPU, izinga lokushisa, i-VRAM nokusetshenziswa kwememori,ihlala ngaphezulu njalo, kuhlanganise namahhala wesikrini esigcwele.

> **Ezinye izilimi**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | **isiZulu** | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Izici

- **Ukulungiswa kwesikhathi sangempela**: Isilinganiso se-CPU, izinga lokushisa se-CPU, isilinganiso se-GPU, izinga lokushisa se-GPU, ukusetshenziswa kwe-VRAM, ukusetshenziswa kwememori
- **Izimo zobukaziswa ezimbili**: I-widget engekheni / Ibhadi elingaphezulu, shintsha ngokuchofoza okukodwa
- **Umbukiso oqanjwe ngokuzimela**: Khetha ngokukhululwa yiziphi izilinganiso ezingasetshenziswa, shintsha phakathi kwephesenti/amanani angqobo
- **Hlala ngaphezulu njalo**: Ihlale phezu kwomngcele wonke, isebenza emidlalweni yesikrini esigcwele
- **Usayizi ozenzekelayo**: Ububanzi bomngcele buhlelwa ngokuzimela ngokusekelwe ekumkatfweni
- **Isitayela esingalungiswa**: Ukuvuma ngokwengqondo komngcele, ukuvuma ngokwengqondo kwemvelaphanda, ubungakanani befonthi - konke kungalungiswa
- **Ukusekelwa kwezilimi eziningi**: 20+ izilimi, ithola ulimi lohlelo ngokuzimela
- **Ukusebenza ngokulula**: Yonsa ngokuchofoza kwesobunxele ukuhamba, imenyu yokuchofoza kwesokudla nezilungiselelo zokushesha, ukuzibophezelwa ngokuzimela emaphephetheni esikrini
- **Ukulungiswa kwamandla okusampula**: 200ms - 3000ms ingalungiswa
- **Ukuqalwa ngokuzimela**: Iqala ngokuzimela lapho kungeniswa ku-Windows
- **Ukusetshenziswa kwesisekelo esiphansi**: Ithatha indawo encane kakhulu emvelaphanda

## Ukuqala okusheshayo

### Ukusetshenziswa okuqondile

Landa i-`ChipPeek.exe` bese uchofoza kabili ukuze isebenze (izocela imvume yemlawuli ngokuzimela ukuze ifunde izinga lokushisa se-CPU namandla afanele).

### Sebenzisa osuka kukhodi yomthombo

```bash
# Klon indawo yokugcina
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Faka izidingo
pip install -r requirements.txt

# Sebenza
python main.py
```

## Izidingo zesistimu

- Windows 10 / Windows 11
- Imvume yemlawuli (iqunyiwe), kungaba khona izinga lokushisa se-CPU namandla afanele
- .NET Framework 4.7.2 noma okuphezulu (kudingeka i-LibreHardwareMonitor)

## Yakha njenge-EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Ngemva kokwakhiwa, ifayela le-EXE likhona ku-`dist/ChipPeek.exe`.

## Ukusetshenziswa

### Imisebenzi eyisisekelo

| Umsebenzi | Incazelo |
|------|------|
| Ukuthuthwa ngokuchofoza kwesobunxele | Susisa indawo yomngcele |
| Ukuchofoza kwesokudla | Vula imenyu (shintsha isimo / izilungiselelo / phuma) |
| Ukuzibophezelwa ngokuzimela | Izingena ngokuzimela ngaphakathi kwe-20px kusuka emaphephetheni esikrini |

### Izimo zobukaziswa

- **I-widget engekheni**: Zonke izilinganiso zihlelwe ngokumile, zingabekwa enganeni yikuphi na lesikrini
- **Ibhadi elingaphezulu**: Zonke izilinganiso zihlelwe ngokumizala, ngokujwayelekile ziphakathi nesigaba sesikrini esingaphezulu

### Izilungiselelo

- **Isimo sokubukisa**: I-widget engekheni / Ibhadi elingaphezulu
- **Indawo ye-widget**: Ngangasobunxele phansi / Ngangasobunxele phezulu / Ngangasokudla phansi / Ngangasokudla phezulu
- **Ukuvuma ngokwengqondo komngcele**: 30% - 100% ukuvuma ngokwengqondo okuphelele komngcele
- **Ukuvuma ngokwengqondo kwemvelaphanda**: 0% - 100% ukuvuma ngokwengqondo kwemvelaphanda (umbhalo uhlala ucebekile)
- **Isikhashana sokusampula**: 200ms - 3000ms izinga lokuvuselela idatha
- **Ubungakanani befonthi**: 8 - 20 amaphuzu
- **Ulimi**: 20+ izilimi, ithola ulimi lohlelo ngokuzimela
- **Izilinganiso zobukaziswa**: Yenza / cisha isilinganiso ngasinye ngokuzimela
- **Ifomethi yokubukisa**: I-VRAM / imemori ingashintsha phakathi kwephesenti noma amanani angqobo
- **Ukuqalwa ngokuzimela**: Sebenza ngokuzimela lapho kungeniswa ku-Windows

## Iqoqo lezobuchwepheshe

- **GUI**：Tkinter
- **Idatha ye-hardware**：LibreHardwareMonitorLib (ngokusebenzisa i-pythonnet), psutil, pynvml (isekelo sesiwe se-NVIDIA GPU)
- **Ukuhlanganiswa kwezinhlelo**：pywin32 (umngcele uhlala ngaphezulu njalo, irejitha yokuqala ngokuzimela)
- **Ukupakatwa**：PyInstaller

## Ukwakheka kohlelo

```
ChipPeek/
├── main.py                  # Phoyinti lokungena
├── monitor_window.py        # Umngcele we-UI kanye nengqondo yokusebenzisana
├── hardware_monitor.py      # Ukuqoqwa kwedatha ye-hardware
├── config.py                # Ukuphathwa kokulungisa
├── i18n.py                  # Okwembethe
├── generate_icon.py         # Iskripthi yokwakha uphawu
├── admin.manifest           # Uvunyiso lwemvume yemlawuli ye-UAC
├── app.ico                  # Uphawu lwesicelo
├── app.png                  # Ukujwayela kwephawu
├── requirements.txt         # Izidingo ze-Python
├── docs/                    # Umanikwelo wezilimi eziningi
│   └── README_*.md
├── i18n/                    # Amafayela okuhumusha
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Ifayeli elisebenzisekayo eliyakhiwe
```

## Ifayela lokulungisa

Ifayela le-`config.json` ligciniwa esigabeni esifanayo ne-EXE futhi linakonke konke okulungiswa. Izilungiselelo zigcinwa ngokuzimela lapho ziguqukwa.

## Ilayisense

MIT License

## Umklami

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- I-URL yohlelo: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Amakrhidi

- LibreHardwareMonitor - Ibhande lezinhlelo zokulungisa izinhlelo
- psutil - Ukulungiswa kwesistimu esezinye izindlela
- PyInstaller - Ithuluzi lokupakatwa kwe-Python
