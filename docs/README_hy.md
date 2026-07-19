# ChipPeek

Թեժ Windows պրոգրամական մոնիտորի լողացող վիջեթ: CPU/GPU հաճախականության, ջերմաստիճանի, VRAM-ի և հիշողության օգտագործման իրական ժամանակի մոնիտորինգ, միշտ վերևում է՝ ներառյալ լրիվ էկրանի հավելվածները:

> **Այլ լեզուներ**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | **Հայերեն** | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Հատկություններ

- **Իրական ժամանակի մոնիտորինգ**: CPU հաճախականություն, CPU ջերմաստիճան, GPU հաճախականություն, GPU ջերմաստիճան, VRAM օգտագործում, հիշողության օգտագործում
- **Երկու ցուցադրման ռեժիմ**: Անկյունի վիջեթ / Վերին սյուն, մեկ կտրումով փոփոխում
- **Պարբերաձև ցուցադրում**: Ազատորեն ընտրեք, թե որ մարմինները ցույց տալ, տոկոս/իրական արժեքի փոփոխում
- **Միշտ վերևում**: Պահպանվում է բոլոր պատուհանների վրա, աշխատում է լրիվ էկրանի խաղերում էլ
- **Ինքնաշխատ չափ**: Պատուհանի լայնությունն ինքնաշխարհականորեն հարմարանում է բովանդակությանը
- **Կարգավորվող ոճ**: Պատուհանի թափանցիկություն, խավիրի թափանցիկություն, տառի չափը բոլորը կարգավորվում են
- **Բազմալեզու աջակցություն**: 20+ լեզու, ինքնաշխատորեն ճանաչում է համակարգի լեզուն
- **Հարմար գործողություն**: Ձախ քաշմով տեղափոխել, աջ կտրումով մենյուի արագ կարգավորումներ, էկրանի եզրերին ինքնաշխատ կպցնել
- **Կարգավորվող հետազոտություն**: 200ms - 3000ms կարգավորվում է
- **Ինքնաշխատում**: Windows-ը մուտք գործելիս ինքնաշխատորեն մեկնարկում է
- **Ցածր ռեսուրսների օգտագործում**: Ֆոնի նվազագույն ծավալ

## Արագ սկիզբ

### Ուղիղ օգտագործում

Բեռնեք `ChipPeek.exe` և կտրեք երկու անգամ գործարկելու համար (CPU ջերմաստիճանի և ճիշտ հաճախականության ընթերցման համար ինքնաշխատորեն պահանջում է ադմինիստրատորի իրավունքներ):

### Աղբյուրից գործարկում

```bash
# Պահոցի կլոնավորում
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Կախվածությունների տեղադրում
pip install -r requirements.txt

# Գործարկում
python main.py
```

## Համակարգի պահանջներ

- Windows 10 / Windows 11
- Ադմինիստրատորի իրավունքներ (առաջարկվում է), հակառակ դեպքում CPU ջերմաստիճանը և ճիշտ հաճախականությունը կարող են մատչելի չլինել
- .NET Framework 4.7.2 կամ ավելի բարձր (անհրաժեշտ է LibreHardwareMonitor-ի կողմից)

## Ստեղծել որպես EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Ստեղծումից հետո EXE ֆայլը գտնվում է `dist/ChipPeek.exe`-ում:

## Օգտագործում

### Հիմնական գործողություններ

| Գործողություն | Նկարագրություն |
|------|------|
| Ձախ քաշում | Պատուհանի դիրքի տեղափոխում |
| Աջ կտրում | Մենյուի բացում (ռեժիմի փոփոխում / կարգավորումներ / ելք) |
| Ինքնաշխատ կպցնել | Էկրանի եզրերից 20px ներսում ինքնաշխատորեն կպչում է |

### Ցուցադրման ռեժիմներ

- **Անկյունի վիջեթ**: Բոլոր մարմինները ուղղահայաց են դասավորված, կարող է տեղադրվել էկրանի ցանկացած անկյունում
- **Վերին սյուն**: Բոլոր մարմինները հորիզոնական են դասավորված, լռությամբ էկրանի վերևում կենտրոնում է

### Կարգավորումներ

- **Ցուցադրման ռեժիմ**: Անկյունի վիջեթ / Վերին սյուն
- **Վիջեթի դիրք**: Ստորին աջ / Ստորին ձախ / Վերին աջ / Վերին ձախ
- **Պատուհանի թափանցիկություն**: 30% - 100% ընդհանուր պատուհանի թափանցիկություն
- **Խավիրի թափանցիկություն**: 0% - 100% խավիրի թափանցիկ (տեքստը մնում է հստակ)
- **Հետազոտության ինտերվալ**: 200ms - 3000ms տվյալների թարմացման արագություն
- **Տառի չափ**: 8 - 20 կետ տառ
- **Լեզու**: 20+ լեզու, ինքնաշխատորեն ճանաչում է համակարգի լեզուն
- **Ցուցադրման մարմիններ**: յուրաքանչյուր մարմնի անկախ միացում/անջատում
- **Ցուցադրման ֆորմատ**: VRAM / հիշողությունը կարող է տոկոս կամ իրական արժեքներ միջև փոխվել
- **Ինքնաշխատում**: Windows-ը մուտք գործելիս ինքնաշխատորեն գործարկում է

## Տեխնիկական կիրառում

- **GUI**：Tkinter
- **Պրոգրամական տվյալներ**：LibreHardwareMonitorLib (pythonnet-ի միջոցով), psutil, pynvml (NVIDIA GPU պահեստային)
- **Համակարգի ինտեգրում**：pywin32 (պատուհանի վերևում, ինքնաշխատ-մեկնարկի ռեեստր)
- **Փաթեթավորում**：PyInstaller

## Նախագծի կառուցվածք

```
ChipPeek/
├── main.py                  # Մուտքի կետ
├── monitor_window.py        # Պատուհանի UI և փոխազդեցության տրամաբանություն
├── hardware_monitor.py      # Պրոգրամական տվյալների հավաքում
├── config.py                # Կարգավորման կառավարում
├── i18n.py                  # Միջազգայնացում
├── generate_icon.py         # Պատկերի ստեղծման սկրիպտ
├── admin.manifest           # UAC ադմինիստրատորի իրավունքների մանիպեստ
├── app.ico                  # Հավելվածի պատկեր
├── app.png                  # Պատկերի նախադիտում
├── requirements.txt         # Python կախվածություններ
├── docs/                    # Բազմալեզու փաստաթղթեր
│   └── README_*.md
├── i18n/                    # Թարգմանության ֆայլեր
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Հավաքված կատարված ֆայլ
```

## Կարգավորման ֆայլ

`config.json` ֆայլը պահվում է EXE-ի հետ նույն գրացուցակում, պարունակում է բոլոր կարգավորվող կարգավորումները: Կարգավորումները փոփոխվելիս ինքնաշխատորեն պահվում են:

## Լիցենզիա

MIT License

## Մշակիչ

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- Նախագծի URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Շնորհակալություն

- LibreHardwareMonitor - Պրոգրամական մոնիտորի գրադարան
- psutil - Խաչփլատֆորմ համակարգի մոնիտորինգ
- PyInstaller - Python փաթեթավորման գործիք
