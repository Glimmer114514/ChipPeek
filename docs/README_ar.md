# ChipPeek

أداة عائمة خفيفة لمراقبة الأجهزة على Windows. مراقبة في الوقت الفعلي لتردد CPU/GPU، ودرجة الحرارة، وVRAM، واستخدام الذاكرة، دائمًا في المقدمة بما في ذلك التطبيقات ملء الشاشة.

> **لغات أخرى**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | **العربية** | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## الميزات

- **مراقبة في الوقت الفعلي**: تردد CPU، درجة حرارة CPU، تردد GPU، درجة حرارة GPU، استخدام VRAM، استخدام الذاكرة
- **وضعي عرض**: ويدجت الزاوية / الشريط العلوي، تبدأ بنقرة واحدة
- **عرض قابل للتخصيص**: اختر بحرية المقاييس التي تريد عرضها، تبدأ بين النسب المئوية/القيم الفعلية
- **دائمًا في المقدمة**: يبقى فوق جميع النوافذ، يعمل في ألعاب ملء الشاشة
- **حجم تلقائي**: عرض النافذة يتكيف تلقائيًا مع المحتوى
- **نمط قابل للتعديل**: شفافية النافذة، شفافية الخلفية، حجم الخط - كلها قابلة للتعديل
- **دعم متعدد اللغات**: أكثر من 20 لغة، يكتشف لغة النظام تلقائيًا
- **عملية مريحة**: اسحب بالنقر الأيسر للنقل، قائمة النقر الأيمن للإعدادات السريعة، الالتصاق التلقائي بحواف الشاشة
- **أخذ عينات قابل للتكوين**: 200ms - 3000ms قابل للتعديل
- **بدء تلقائي**: يتم التشغيل تلقائيًا عند تسجيل الدخول إلى Windows
- **استخدام منخفض للموارد**: أثر ضئيل في الخلفية

## بداية سريعة

### استخدام مباشر

قم بتنزيل `ChipPeek.exe` وانقر نقرًا مزدوجًا للتشغيل (سيطلب صلاحيات المسؤول تلقائيًا لدرجة حرارة CPU وقراءة التردد الدقيق).

### التشغيل من الكود المصدري

```bash
# استنساخ المستودع
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# تثبيت التبعيات
pip install -r requirements.txt

# تشغيل
python main.py
```

## متطلبات النظام

- Windows 10 / Windows 11
- صلاحيات المسؤول (موصى به)، وإلا قد لا تتوفر درجة حرارة CPU والتردد الدقيق
- .NET Framework 4.7.2 أو أعلى (مطلوب من قبل LibreHardwareMonitor)

## البناء كـ EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

بعد البناء، يوجد ملف EXE في `dist/ChipPeek.exe`.

## الاستخدام

### العمليات الأساسية

| الإجراء | الوصف |
|------|------|
| السحب بالنقر الأيسر | نقل موضع النافذة |
| النقر الأيمن | فتح القائمة (تبديل الوضع / الإعدادات / الخروج) |
| الالتصاق التلقائي | يلتصق تلقائيًا ضمن 20px من حواف الشاشة |

### أوضاع العرض

- **ويدجت الزاوية**: جميع المقاييس مرتبة عموديًا، يمكن وضعها في أي زاوية من الشاشة
- **الشريط العلوي**: جميع المقاييس مرتبة أفقيًا، تتمركز في أعلى الشاشة افتراضيًا

### الإعدادات

- **وضع العرض**: ويدجت الزاوية / الشريط العلوي
- **موضع الودجت**: أسفل اليمين / أسفل اليسار / أعلى اليمين / أعلى اليسار
- **شفافية النافذة**: 30% - 100% شفافية النافذة العامة
- **شفافية الخلفية**: 0% - 100% خلفية شفافة (النص يظل واضحًا)
- **فاصل أخذ العينات**: 200ms - 3000ms معدل تحديث البيانات
- **حجم الخط**: خط 8 - 20 نقطة
- **اللغة**: أكثر من 20 لغة، يكتشف لغة النظام تلقائيًا
- **مقاييس العرض**: قم بتشغيل/إيقاف كل مقياس بشكل مستقل
- **تنسيق العرض**: VRAM / الذاكرة يمكنها التبديل بين النسب المئوية أو القيم الفعلية
- **بدء تلقائي**: التشغيل تلقائيًا عند تسجيل الدخول إلى Windows

## مكدس التكنولوجيا

- **GUI**：Tkinter
- **بيانات الأجهزة**：LibreHardwareMonitorLib (عبر pythonnet)، psutil، pynvml (حل بديل لـ GPU NVIDIA)
- **تكامل النظام**：pywin32 (نافذة في المقدمة، تسجيل البدء التلقائي)
- **التعبئة**：PyInstaller

## هيكل المشروع

```
ChipPeek/
├── main.py                  # نقطة الدخول
├── monitor_window.py        # واجهة المستخدم للنافذة ومنطق التفاعل
├── hardware_monitor.py      # جمع بيانات الأجهزة
├── config.py                # إدارة التكوين
├── i18n.py                  # التدويل
├── generate_icon.py         # نص إنشاء الأيقونات
├── admin.manifest           # بيان صلاحيات المسؤول UAC
├── app.ico                  # أيقونة التطبيق
├── app.png                  # معاينة الأيقونة
├── requirements.txt         # تبعيات Python
├── docs/                    # وثائق متعددة اللغات
│   └── README_*.md
├── i18n/                    # ملفات الترجمة
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # الملف التنفيذي المترجم
```

## ملف التكوين

يتم حفظ ملف `config.json` في نفس الدليل مثل EXE، ويحتوي على جميع الإعدادات القابلة للتعديل. يتم حفظ الإعدادات تلقائيًا عند تعديلها.

## الترخيص

MIT License

## المطور

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- رابط المشروع: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## الشكر والتقدير

- LibreHardwareMonitor - مكتبة مراقبة الأجهزة
- psutil - مراقبة النظام متعدد المنصات
- PyInstaller - أداة تعبئة Python
