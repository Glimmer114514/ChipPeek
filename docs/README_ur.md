# ChipPeek

ونڈوز کے لیے ایک ہلکا پھلکا فلوٹنگ ہارڈویئر مانیٹرنگ وجیٹ۔ CPU/GPU فریکوئنسی، درجہ حرارت، VRAM اور میموری کے استعمال کی ریئل ٹائم مانیٹرنگ، ہمیشہ اوپر رہتا ہے، بشمول فل اسکرین ایپس۔

> **دیگر زبانیں**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | **اردو** | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## خصوصیات

- **ریئل ٹائم مانیٹرنگ**: CPU فریکوئنسی، CPU درجہ حرارت، GPU فریکوئنسی، GPU درجہ حرارت، VRAM استعمال، میموری استعمال
- **دو ڈسپلے موڈز**: کارنر وجیٹ / ٹاپ بار، ایک کلک میں سوئچ
- **قابل اپنی مرضی کے مطابق ڈسپلے**: آزادانہ منتخب کریں کہ کن میٹرکس کو دکھانا ہے، فیصد/اصل اقدار کے درمیان سوئچ کریں
- **ہمیشہ اوپر**: تمام ونڈوز کے اوپر رہتا ہے، فل اسکرین گیمز میں کام کرتا ہے
- **خودکار سائز**: ونڈو کی چوڑائی مواد کے مطابق خود بخود ایڈجسٹ ہو جاتی ہے
- **ایڈجسٹ ایبل اسٹائل**: ونڈو کی شفافیت، پس منظر کی شفافیت، فونٹ سائز - سب ایڈجسٹ کے قابل
- **متعدد زبانوں میں معاونت**: 20+ زبانیں، خود بخود سسٹم کی زبان کا پتہ لگاتی ہے
- **آسان آپریشن**: بائیں کلک سے گھسیٹ کر منتقل کریں، دائیں کلک مینو سے فوری ترتیبات، اسکرین کے کناروں سے خودکار دستک
- **قابل ترتیب سیمپلنگ فریکوئنسی**: 200ms - 3000ms ایڈجسٹ کے قابل
- **آٹو اسٹارٹ**: Windows میں لاگ ان پر خود بخود شروع ہوتا ہے
- **کم وسائل کا استعمال**: پس منظر میں کم سے کم جگہ

## فوری شروعات

### براہ راست استعمال

`ChipPeek.exe` ڈاؤن لوڈ کریں اور چلانے کے لیے ڈبل کلک کریں (سی پی یو کے درجہ حرارت اور درست فریکوئنسی پڑھنے کے لیے خود بخود منتظم کے مراعات کا درخواست دے گا)۔

### سورس سے چلائیں

```bash
# ریپوزٹری کلون کریں
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# انحصار انسٹال کریں
pip install -r requirements.txt

# چلائیں
python main.py
```

## سسٹم کی ضروریات

- Windows 10 / Windows 11
- منتظم کے مراعات (تجویز کردہ)، بصورت دیگر CPU درجہ حرارت اور درست فریکوئنسی دستیاب نہیں ہو سکتی
- .NET Framework 4.7.2 یا اس سے اوپر (LibreHardwareMonitor کے لیے درکار)

## EXE کے طور پر بنائیں

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

بنانے کے بعد، EXE فائل `dist/ChipPeek.exe` میں موجود ہے۔

## استعمال

### بنیادی آپریشنز

| آپریشن | تفصیل |
|------|------|
| بائیں کلک گھسیٹنا | ونڈو کی پوزیشن منتقل کریں |
| دائیں کلک | مینو کھولیں (موڈ تبدیل کریں / ترتیبات / باہر نکلیں) |
| آٹو سنیپ | اسکرین کے کناروں سے 20px کے اندر خود بخود سنیپ ہو جاتا ہے |

### ڈسپلے موڈز

- **کونے کا وجیٹ**: تمام میٹرکس عمودی طور پر ترتیب دیے گئے ہیں، اسکرین کے کسی بھی کونے میں رکھے جا سکتے ہیں
- **ٹاپ بار**: تمام میٹرکس افقی طور پر ترتیب دیے گئے ہیں، ڈیفالٹ طور پر اسکرین کے اوپری حصے میں درمیان میں ہیں

### ترتیبات

- **ڈسپلے موڈ**: کونے کا وجیٹ / ٹاپ بار
- **وجیٹ کی پوزیشن**: نیچے دائیں / نیچے بائیں / اوپر دائیں / اوپر بائیں
- **ونڈو کی شفافیت**: 30% - 100% مجموعی ونڈو شفافیت
- **پس منظر کی شفافیت**: 0% - 100% پس منظر شفاف (ٹیکسٹ واضح رہتا ہے)
- **سیمپلنگ وقفہ**: 200ms - 3000ms ڈیٹا ریفریشر کی شرح
- **فونٹ سائز**: 8 - 20 پوائنٹس
- **زبان**: 20+ زبانیں، خود بخود سسٹم کی زبان کا پتہ لگاتی ہے
- **ڈسپلے میٹرکس**: ہر میٹرک کو آزادانہ طور پر آن/بند کریں
- **ڈسپلے فارمیٹ**: VRAM / میموری فیصد یا اصل اقدار کے درمیان سوئچ کر سکتی ہے
- **آٹو اسٹارٹ**: Windows میں لاگ ان پر خود بخود چلائیں

## ٹیک اسٹیک

- **GUI**：Tkinter
- **ہارڈویئر ڈیٹا**：LibreHardwareMonitorLib (pythonnet کے ذریعے)، psutil، pynvml (NVIDIA GPU کے لیے بیک اپ)
- **سسٹم انٹیگریشن**：pywin32 (ونڈو ہمیشہ اوپر، آٹو اسٹارٹ رجسٹری)
- **پیکیجنگ**：PyInstaller

## پروجیکٹ کا ڈھانچہ

```
ChipPeek/
├── main.py                  # انٹری پوائنٹ
├── monitor_window.py        # ونڈو UI اور تعامل کی منطق
├── hardware_monitor.py      # ہارڈویئر ڈیٹا اکٹھا کرنا
├── config.py                # کنفیگریشن کا انتظام
├── i18n.py                  # بین الاقوامی کاری
├── generate_icon.py         # آئکن جنریشن اسکرپٹ
├── admin.manifest           # UAC منتظم کے مراعات کا مینی فیسٹ
├── app.ico                  # ایپلیکیشن آئکن
├── app.png                  # آئکن کا پیش نظارہ
├── requirements.txt         # Python انحصار
├── docs/                    # کثیر اللسان دستاویزات
│   └── README_*.md
├── i18n/                    # ترجمے کی فائلیں
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # مرتب شدہ قابل عمل فائل
```

## کنفیگریشن فائل

`config.json` فائل EXE کے ایک ہی ڈائرکٹری میں محفوظ ہوتی ہے اور تمام قابل ایڈجسٹ ترتیبات پر مشتمل ہوتی ہے۔ ترتیبات میں تبدیلی پر خود بخود محفوظ ہو جاتی ہیں۔

## لائسنس

MIT License

## ڈویلپر

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- پروجیکٹ کا یوار ایل: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## اعتراف

- LibreHardwareMonitor - ہارڈویئر مانیٹرنگ لائبریری
- psutil - کراس پلیٹ فارم سسٹم مانیٹرنگ
- PyInstaller - Python پیکیجنگ ٹول
