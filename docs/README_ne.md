# ChipPeek

Windows को लागि हल्का हार्डवेयर मोनिटरिंग फ्लोटिंग विजेट। CPU/GPU फ्रिक्वेन्सी, तापक्रम, VRAM, र मेमोरी प्रयोगको वास्तविक-समय अनुगमन, पूर्ण-स्क्रिन एपहरू सहित सबैभन्दा माथि रहिरहन्छ।

> **अन्य भाषाहरू**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | **नेपाली** | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## विशेषताहरू

- **वास्तविक-समय अनुगमन**: CPU फ्रिक्वेन्सी, CPU तापक्रम, GPU फ्रिक्वेन्सी, GPU तापक्रम, VRAM प्रयोग, मेमोरी प्रयोग
- **दुई प्रदर्शन मोड**: कुने विजेट / शीर्ष बार, एक क्लिकमा स्विच
- **अनुकूलनयोग्य प्रदर्शन**: कुन मेट्रिकहरू देखाउने स्वतन्त्र रूपमा छनौट गर्नुहोस्, प्रतिशत/वास्तविक मानहरू बीच टगल गर्नुहोस्
- **सधैं माथि**: सबै विन्डोहरू भन्दा माथि रहिरहन्छ, पूर्ण-स्क्रिन खेलहरूमा काम गर्दछ
- **स्वचालित आकार**: विन्डोको चौडाइ सामग्रीसँग मिल्न स्वचालित रूपमा समायोजन हुन्छ
- **समायोजनयोग्य शैली**: विन्डो अपारदर्शिता, पृष्ठभूमि पारदर्शिता, फन्ट साइज सबै समायोजनयोग्य छन्
- **बहु-भाषा समर्थन**: 20+ भाषाहरू, सिस्टम भाषा स्वचालित रूपमा पत्ता लगाउँछ
- **सजिलो सञ्चालन**: सार्न बायाँ तान्नुहोस्, द्रुत सेटिङहरूको लागि दायाँ क्लिक मेनु, स्क्रिन किनारहरूमा स्वतः स्न्याप
- **कन्फिगरेबल नमूना**: 200ms - 3000ms समायोजनयोग्य
- **स्वतः सुरु**: Windows लगइनमा स्वचालित रूपमा सुरु हुनुहोस्
- **कम स्रोत प्रयोग**: पृष्ठभूमिमा न्यूनतम फुटप्रिन्ट

## द्रुत सुरुवात

### प्रत्यक्ष प्रयोग

`ChipPeek.exe` डाउनलोड गर्नुहोस् र चलाउन डबल क्लिक गर्नुहोस् (CPU तापक्रम र सटीक फ्रिक्वेन्सी पढ्नको लागि स्वचालित रूपमा व्यवस्थापक विशेषाधिकारहरू अनुरोध गर्नेछ)।

### स्रोतबाट चलाउनुहोस्

```bash
# रिपोजिटरी क्लोन गर्नुहोस्
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# निर्भरताहरू स्थापना गर्नुहोस्
pip install -r requirements.txt

# चलाउनुहोस्
python main.py
```

## प्रणाली आवश्यकताहरू

- Windows 10 / Windows 11
- व्यवस्थापक विशेषाधिकारहरू (सिफारिस गरिएको), अन्यथा CPU तापक्रम र सटीक फ्रिक्वेन्सी उपलब्ध नहुन सक्छ
- .NET Framework 4.7.2 वा उच्च (LibreHardwareMonitor ले आवश्यक पर्दछ)

## EXE को रूपमा निर्माण गर्नुहोस्

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

निर्माण पछि, EXE फाइल `dist/ChipPeek.exe` मा अवस्थित छ।

## प्रयोग

### आधारभूत सञ्चालनहरू

| कार्य | विवरण |
|------|------|
| बायाँ तान्नुहोस् | विन्डो स्थिति सार्नुहोस् |
| दायाँ क्लिक | मेनु खोल्नुहोस् (मोड स्विच गर्नुहोस् / सेटिङ्हरू / बाहिर निस्कनुहोस्) |
| स्वतः स्न्याप | स्क्रिन किनारहरूको 20px भित्र स्वचालित रूपमा स्न्याप हुन्छ |

### प्रदर्शन मोडहरू

- **कुने विजेट**: सबै मेट्रिकहरू ठाडो रूपमा व्यवस्थित, स्क्रिनको कुनै पनि कुनेमा राख्न सकिन्छ
- **शीर्ष बार**: सबै मेट्रिकहरू तेर्सो रूपमा व्यवस्थित, पूर्वनिर्धारित रूपमा स्क्रिनको शीर्षमा केन्द्रित

### सेटिङ्हरू

- **प्रदर्शन मोड**: कुने विजेट / शीर्ष बार
- **विजेट स्थिति**: तल दायाँ / तल बायाँ / माथि दायाँ / माथि बायाँ
- **विन्डो अपारदर्शिता**: 30% - 100% सम्पूर्ण विन्डो पारदर्शिता
- **पृष्ठभूमि पारदर्शिता**: 0% - 100% पृष्ठभूमि पारदर्शी (पाठ स्पष्ट रहन्छ)
- **नमूना अन्तराल**: 200ms - 3000ms डाटा रिफ्रेस दर
- **फन्ट साइज**: 8 - 20 पोइन्ट फन्ट
- **भाषा**: 20+ भाषाहरू, सिस्टम भाषा स्वचालित रूपमा पत्ता लगाउँछ
- **प्रदर्शन मेट्रिकहरू**: प्रत्येक मेट्रिकलाई स्वतन्त्र रूपमा टगल गर्नुहोस्
- **प्रदर्शन ढाँचा**: VRAM / मेमोरी प्रतिशत वा वास्तविक मानहरू बीच टगल गर्न सक्छ
- **स्वतः सुरु**: Windows मा लगइन गर्दा स्वचालित रूपमा चल्नुहोस्

## Tech Stack

- **GUI**：Tkinter
- **हार्डवेयर डाटा**：LibreHardwareMonitorLib (pythonnet मार्फत), psutil, pynvml (NVIDIA GPU फ्यालब्याक)
- **प्रणाली एकीकरण**：pywin32 (विन्डो टपमोस्ट, स्वतः सुरु रेजिस्ट्री)
- **प्याकेजिङ**：PyInstaller

## परियोजना संरचना

```
ChipPeek/
├── main.py                  # प्रवेश बिन्दु
├── monitor_window.py        # विन्डो UI र अन्तरक्रिया तर्क
├── hardware_monitor.py      # हार्डवेयर डाटा सङ्कलन
├── config.py                # कन्फिगरेसन व्यवस्थापन
├── i18n.py                  # अन्तर्राष्ट्रियकरण
├── generate_icon.py         # आइकन जेनरेशन स्क्रिप्ट
├── admin.manifest           # UAC व्यवस्थापक विशेषाधिकार घोषणापत्र
├── app.ico                  # अनुप्रयोग आइकन
├── app.png                  # आइकन पूर्वावलोकन
├── requirements.txt         # Python निर्भरताहरू
├── docs/                    # बहु-भाषा कागजातहरू
│   └── README_*.md
├── i18n/                    # अनुवाद फाइलहरू
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # कम्पाइल गरिएको निष्पादनयोग्य
```

## कन्फिगरेसन फाइल

`config.json` फाइल EXE जस्तै डाइरेक्टरीमा बचत गरिन्छ, सबै समायोजनयोग्य सेटिङ्हरू समावेश गर्दछ। सेटिङ्हरू संशोधन गर्दा स्वचालित रूपमा बचत गरिन्छ।

## इजाजतपत्र

MIT License

## विकासकर्ता

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- परियोजना URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## श्रेयहरू

- LibreHardwareMonitor - हार्डवेयर मोनिटरिंग लाइब्रेरी
- psutil - क्रस-प्लेटफर्म सिस्टम मोनिटरिंग
- PyInstaller - Python प्याकेजिङ उपकरण
