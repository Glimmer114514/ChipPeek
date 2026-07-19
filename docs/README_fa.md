# ChipPeek

یک ویجت شناور سبک برای مانیتورینگ سخت‌افزار در ویندوز. مانیتورینگ لحظه‌ای فرکانس CPU/GPU، دما، VRAM و استفاده از حافظه، همیشه در بالای صفحه، حتی در برنامه‌های تمام صفحه.

> **سایر زبان‌ها**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | **فارسی** | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## ویژگی‌ها

- **مانیتورینگ لحظه‌ای**: فرکانس CPU، دمای CPU، فرکانس GPU، دمای GPU، استفاده از VRAM، استفاده از حافظه
- **دو حالت نمایش**: ویجت گوشه / نوار بالا، تغییر با یک کلیک
- **نمایش قابل سفارشی**: انتخاب آزادانه معیارهای قابل نمایش، جابجایی بین درصد/مقادیر واقعی
- **همیشه در بالا**: همیشه در بالای تمام پنجره‌ها باقی می‌ماند، در بازی‌های تمام صفحه هم کار می‌کند
- **اندازه خودکار**: عرض پنجره به طور خودکار با محتوا تطبیق داده می‌شود
- **استایل قابل تنظیم**: شفافیت پنجره، شفافیت پس‌زمینه، اندازه فونت - همه قابل تنظیم هستند
- **پشتیبانی چندزبانه**: 20+ زبان، تشخیص خودکار زبان سیستم
- **عملیات راحت**: جابجایی با کشیدن با کلیک چپ، منوی کلیک راست برای تنظیمات سریع، چسبیدن خودکار به لبه‌های صفحه
- **فرکانس نمونه‌برداری قابل پیکربندی**: 200ms - 3000ms قابل تنظیم
- **شروع خودکار**: به طور خودکار در زمان ورود به ویندوز راه اندازی می‌شود
- **استفاده کم از منابع**: کمترین حجم در پس‌زمینه

## شروع سریع

### استفاده مستقیم

`ChipPeek.exe` را دانلود کنید و برای اجرا دوبار کلیک کنید (به طور خودکار دسترسی ادمین را برای دمای CPU و خواندن دقیق فرکانس درخواست می‌کند).

### اجرا از کد منبع

```bash
# کلون کردن مخزن
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# نصب وابستگی‌ها
pip install -r requirements.txt

# اجرا
python main.py
```

## سیستم مورد نیاز

- Windows 10 / Windows 11
- دسترسی ادمین (توصیه می‌شود)، در غیر این صورت دمای CPU و فرکانس دقیق ممکن است در دسترس نباشد
- .NET Framework 4.7.2 یا بالاتر (مورد نیاز توسط LibreHardwareMonitor)

## ساخت به عنوان EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

پس از ساخت، فایل EXE در `dist/ChipPeek.exe` قرار دارد.

## نحوه استفاده

### عملیات پایه

| عملیات | توضیحات |
|------|------|
| کشیدن با کلیک چپ | جابجایی موقعیت پنجره |
| کلیک راست | باز کردن منو (تغییر حالت / تنظیمات / خروج) |
| چسبیدن خودکار | به طور خودکار در فاصله 20px از لبه‌های صفحه می‌چسبد |

### حالت‌های نمایش

- **ویجت گوشه**: تمام معیارها به صورت عمودی چیده شده‌اند، می‌توانند در هر گوشه صفحه قرار گیرند
- **نوار بالا**: تمام معیارها به صورت افقی چیده شده‌اند، به طور پیش‌فرض در بالای صفحه مرکزی هستند

### تنظیمات

- **حالت نمایش**: ویجت گوشه / نوار بالا
- **موقعیت ویجت**: پایین سمت راست / پایین سمت چپ / بالا سمت راست / بالا سمت چپ
- **شفافیت پنجره**: 30% - 100% شفافیت کلی پنجره
- **شفافیت پس‌زمینه**: 0% - 100% پس‌زمینه شفاف (متن واضح می‌ماند)
- **فاصله نمونه‌برداری**: 200ms - 3000ms نرخ به‌روزرسانی داده‌ها
- **اندازه فونت**: 8 - 20 پوینت
- **زبان**: 20+ زبان، تشخیص خودکار زبان سیستم
- **معیارهای نمایش**: هر معیار را می‌توان به صورت مستقل روشن/خاموش کرد
- **فرمت نمایش**: VRAM / حافظه می‌تواند بین درصد یا مقادیر واقعی جابجا شود
- **شروع خودکار**: اجرای خودکار هنگام ورود به ویندوز

## استک فناوری

- **GUI**：Tkinter
- **داده‌های سخت‌افزار**：LibreHardwareMonitorLib (از طریق pythonnet)، psutil، pynvml (راه حل جایگزین برای NVIDIA GPU)
- **یکپارچه‌سازی سیستم**：pywin32 (پنجره همیشه بالا، رجیستری شروع خودکار)
- **بسته‌بندی**：PyInstaller

## ساختار پروژه

```
ChipPeek/
├── main.py                  # نقطه ورود
├── monitor_window.py        # رابط کاربری پنجره و منطق تعامل
├── hardware_monitor.py      # جمع‌آوری داده‌های سخت‌افزار
├── config.py                # مدیریت پیکربندی
├── i18n.py                  # بین‌المللی‌سازی
├── generate_icon.py         # اسکریپت تولید آیکون
├── admin.manifest           # مانیفست دسترسی ادمین UAC
├── app.ico                  # آیکون برنامه
├── app.png                  # پیش‌نمایش آیکون
├── requirements.txt         # وابستگی‌های Python
├── docs/                    # مستندات چندزبانه
│   └── README_*.md
├── i18n/                    # فایل‌های ترجمه
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # فایل اجرایی کامپایل شده
```

## فایل پیکربندی

فایل `config.json` در همان دایرکتوری EXE ذخیره می‌شود و شامل تمام تنظیمات قابل تنظیم است. تنظیمات به طور خودکار هنگام تغییر ذخیره می‌شوند.

## مجوز

MIT License

## توسعه‌دهنده

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- آدرس پروژه: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## قدردانی

- LibreHardwareMonitor - کتابخانه مانیتورینگ سخت‌افزار
- psutil - مانیتورینگ سیستم چند پلتفرمی
- PyInstaller - ابزار بسته‌بندی Python
