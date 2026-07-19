# ChipPeek

მსუბუქი Windows ტექნიკის მონიტორინგის მცურავი ვიჯეტი. რეალურ დროში CPU/GPU სიხშირის, ტემპერატურის, VRAM-ის და მეხსიერების მოხმარების მონიტორინგი, ყოველთვის ზედა ფანჯრების ზემოთ, მათ შორის სრულეკრანული აპლიკაციებშიც კი.

> **სხვა ენები**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | **ქართული** | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## მახასიათებლები

- **რეალურ დროში მონიტორინგი**: CPU სიხშირე, CPU ტემპერატურა, GPU სიხშირე, GPU ტემპერატურა, VRAM მოხმარება, მეხსიერების მოხმარება
- **ორი ჩვენების რეჟიმი**: კუთხის ვიჯეტი / ზედა ზოლი, ერთი კლიკით გადართვა
- **მორგებული ჩვენება**: თავისუფლად აირჩიეთ რომელი მაჩვენებლები გამოჩნდეს, პროცენტი/რეალური მნიშვნელობის გადართვა
- **ყოველთვის ზედა**: ყველა ფანჯრის ზემოთ ინახება, მუშაობს სრულეკრანულ თამაშებშიაც
- **ავტომატური ზომა**: ფანჯრის სიგანე ავტომატურად იცვლება შინაარსის მიხედვით
- **რეგულირებადი სტილი**: ფანჯრის გაჭირვება, ფონის გამჭვირვალობა, შრიფტის ზომა ყველა რეგულირდება
- **მრავალიენური მხარდაჭერა**: 20+ ენა, ავტომატურად ამოწმებს სისტემურ ენას
- **მოხერხberger ოპერაცია**: მარცხენა გადაადგილებით გადატანა, მარჯვენა დაკლიკებით მენიუ სწრაფი პარამეტრებისთვის, ეკრანის კიდეებისთვის ავტომატური შეწებება
- **რეგულირებადი სემპლირება**: 200ms - 3000ms რეგულირდება
- **ავტომატური გაშვება**: Windows-ზე შესვლისას ავტომატურად გაეშვება
- **დაბალი რესურსების მოხმარება**: ფონში მინიმალური ზომა

## სწრაფი დაწყება

### პირდაპირ გამოყენება

ჩამოტვირთეთ `ChipPeek.exe` და ორჯერ დაკლიკებით გაუშვით (CPU ტემპერატურის და ზუსტი სიხშირის კითხვისთვის ავტომატურად ითხოვს ადმინისტრატორის უფლებებს).

### წყაროდან გაშვება

```bash
# რეპოზიტორიის კლონირება
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# დამოკიდებულებების ინსტალაცია
pip install -r requirements.txt

# გაშვება
python main.py
```

## სისტემური მოთხოვნები

- Windows 10 / Windows 11
- ადმინისტრატორის უფლებები (რეკომენდებული), წინააღმდეგ შემთხვევაში CPU ტემპერატურა და ზუსტი სიხშირე შეიძლება არ იყოს ხელმისაწვდომი
- .NET Framework 4.7.2 ან მაღალი (საჭიროა LibreHardwareMonitor-ის მიერ)

## EXE-დ აგება

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

აგების შემდეგ EXE ფაილი მდებარეობს `dist/ChipPeek.exe`-ში.

## გამოყენება

### ძირითადი ოპერაციები

| ოპერაცია | აღწერა |
|------|------|
| მარცხენა გადაადგილება | ფანჯრის პოზიციის გადატანა |
| მარჯვენა დაკლიკება | მენიუს გახსნა (რეჟიმის შეცვლა / პარამეტრები / გამოსვლა) |
| ავტომატური შეწებება | ეკრანის კიდეებიდან 20px-მდე ავტომატურად იწებება |

### ჩვენების რეჟიმები

- **კუთხის ვიჯეტი**: ყველა მაჩვენებელი ვერტიკალურადაა განლაგებული, შეიძლება ეკრანის ნებისმიერ კუთხეში განთავსდეს
- **ზედა ზოლი**: ყველა მაჩვენებელი ჰორიზონტალურადაა განლაგებული, ნაგულისხმევად ეკრანის ზემოთ ცენტრშია განთავსებული

### პარამეტრები

- **ჩვენების რეჟიმი**: კუთხის ვიჯეტი / ზედა ზოლი
- **ვიჯეტის პოზიცია**: ქვემო მარჯვენა / ქვემო მარცხენა / ზემო მარჯვენა / ზემო მარცხენა
- **ფანჯრის გაჭირვება**: 30% - 100% საერთო ფანჯრის გამჭვირვალობა
- **ფონის გამჭვირვალობა**: 0% - 100% ფონის გამჭვირვალობა (ტექსტი რჩება მკაფიოდ)
- **სემპლირების ინტერვალი**: 200ms - 3000ms მონაცემების განახლების სიხშირე
- **შრიფტის ზომა**: 8 - 20 ქულა შრიფტი
- **ენა**: 20+ ენა, ავტომატურად ამოწმებს სისტემურ ენას
- **ჩვენების მაჩვენებლები**: თითოეული მაჩვენებლის დამოუკიდებლად ჩართვა/გამორთვა
- **ჩვენების ფორმატი**: VRAM / მეხსიერება შეუძლია პროცენტი ან რეალური მნიშვნელობები შორის გადართვა
- **ავტომატური გაშვება**: Windows-ზე შესვლისას ავტომატურად გაეშვება

## ტექნიკური სტეკი

- **GUI**：Tkinter
- **ტექნიკის მონაცემები**：LibreHardwareMonitorLib (pythonnet-ის მეშვეობით), psutil, pynvml (NVIDIA GPU სარეზერვო)
- **სისტემური ინტეგრაცია**：pywin32 (ფანჯრის ზედა პოზიცია, ავტოგაშვების რეესტრი)
- **შეფუთვა**：PyInstaller

## პროექტის სტრუქტურა

```
ChipPeek/
├── main.py                  # შესავალი წერტილი
├── monitor_window.py        # ფანჯრის UI და ურთიერთქმედების ლოგიკა
├── hardware_monitor.py      # ტექნიკის მონაცემთა შეგროვება
├── config.py                # კონფიგურაციის მართვა
├── i18n.py                  # ინტერნაციონალიზაცია
├── generate_icon.py         # ხატულის გენერაციის სკრიპტი
├── admin.manifest           # UAC ადმინისტრატორის უფლებების მანიფესტი
├── app.ico                  # აპლიკაციის ხატულა
├── app.png                  # ხატულის პრევიუ
├── requirements.txt         # Python დამოკიდებულებები
├── docs/                    # მრავალიენური დოკუმენტაცია
│   └── README_*.md
├── i18n/                    # თარგმანის ფაილები
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # კომპილირებული გამშვები ფაილი
```

## კონფიგურაციის ფაილი

`config.json` ფაილი ინახება EXE-ს იგივე დირექტორიაში, შეიცავს ყველა რეგულირებად პარამეტრს. პარამეტრების შეცვლისას ავტომატურად ინახება.

## ლიცენზია

MIT License

## დეველოპერი

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- პროექტის URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## მადლობა

- LibreHardwareMonitor - ტექნიკის მონიტორინგის ბიბლიოთეკა
- psutil - საფლათფორმიო სისტემური მონიტორინგი
- PyInstaller - Python შეფუთვის ხელსაწყო
