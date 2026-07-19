# ChipPeek

Windows के लिए एक हल्का फ्लोटिंग हार्डवेयर मॉनिटरिंग विजेट। CPU/GPU आवृत्ति, तापमान, VRAM और मेमोरी उपयोग की रियल-टाइम मॉनिटरिंग, फुलस्क्रीन ऐप्स सहित हमेशा सबसे ऊपर दिखाई देता है।

> **अन्य भाषाएं**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | **हिन्दी** | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## विशेषताएं

- **रियल-टाइम मॉनिटरिंग**: CPU आवृत्ति, CPU तापमान, GPU आवृत्ति, GPU तापमान, VRAM उपयोग, मेमोरी उपयोग
- **दो डिस्प्ले मोड**: कॉर्नर विजेट / टॉप बार, एक क्लिक में स्विच
- **अनुकूलन योग्य डिस्प्ले**: स्वतंत्र रूप से चुनें कि कौन से मेट्रिक दिखाने हैं, प्रतिशत/वास्तविक मानों के बीच स्विच करें
- **हमेशा सबसे ऊपर**: सभी विंडो के ऊपर रहता है, फुलस्क्रीन गेम्स में काम करता है
- **स्वचालित आकार**: विंडो चौड़ाई सामग्री के अनुसार स्वचालित रूप से समायोजित होती है
- **समायोज्य शैली**: विंडो अपारदर्शिता, पृष्ठभूमि पारदर्शिता, फॉन्ट आकार - सभी समायोज्य
- **बहुभाषी समर्थन**: 20+ भाषाएं, सिस्टम भाषा को स्वचालित रूप से पहचानता है
- **सुविधाजनक संचालन**: लेफ्ट-ड्रैग से स्थानांतरित करें, राइट-क्लिक मेनू से त्वरित सेटिंग्स, स्क्रीन किनारों पर स्वचालित स्नैप
- **विन्यास योग्य सैंपलिंग**: 200ms - 3000ms समायोज्य
- **ऑटो स्टार्ट**: Windows लॉगिन पर स्वचालित रूप से शुरू होता है
- **कम संसाधन उपयोग**: बैकग्राउंड में न्यूनतम पदचिह्न

## त्वरित आरंभ

### सीधा उपयोग

`ChipPeek.exe` डाउनलोड करें और चलाने के लिए डबल-क्लिक करें (CPU तापमान और सटीक आवृत्ति पढ़ने के लिए स्वचालित रूप से व्यवस्थापक विशेषाधिकारों का अनुरोध करेगा)।

### स्रोत से चलाएं

```bash
# रिपॉजिटरी क्लोन करें
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# निर्भरताएं स्थापित करें
pip install -r requirements.txt

# चलाएं
python main.py
```

## सिस्टम आवश्यकताएं

- Windows 10 / Windows 11
- व्यवस्थापक विशेषाधिकार (अनुशंसित), अन्यथा CPU तापमान और सटीक आवृत्ति उपलब्ध नहीं हो सकती
- .NET Framework 4.7.2 या उच्चतर (LibreHardwareMonitor द्वारा आवश्यक)

## EXE के रूप में बिल्ड करें

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

बिल्ड करने के बाद, EXE फ़ाइल `dist/ChipPeek.exe` में स्थित है।

## उपयोग

### मूल संचालन

| क्रिया | विवरण |
|------|------|
| लेफ्ट क्लिक ड्रैग | विंडो स्थिति स्थानांतरित करें |
| राइट क्लिक | मेनू खोलें (मोड बदलें / सेटिंग्स / बाहर निकलें) |
| ऑटो स्नैप | स्क्रीन किनारों के 20px के भीतर स्वचालित रूप से स्नैप होता है |

### प्रदर्शन मोड

- **कॉर्नर विजेट**: सभी मेट्रिक लंबवत रूप से व्यवस्थित, स्क्रीन के किसी भी कोने में रखा जा सकता है
- **टॉप बार**: सभी मेट्रिक क्षैतिज रूप से व्यवस्थित, डिफ़ॉल्ट रूप से स्क्रीन के शीर्ष पर केंद्रित

### सेटिंग्स

- **डिस्प्ले मोड**: कॉर्नर विजेट / टॉप बार
- **विजेट स्थिति**: नीचे दाईं ओर / नीचे बाईं ओर / ऊपर दाईं ओर / ऊपर बाईं ओर
- **विंडो अपारदर्शिता**: 30% - 100% समग्र विंडो पारदर्शिता
- **पृष्ठभूमि पारदर्शिता**: 0% - 100% पृष्ठभूमि पारदर्शी (पाठ स्पष्ट रहता है)
- **सैंपलिंग अंतराल**: 200ms - 3000ms डेटा रिफ्रेश दर
- **फॉन्ट आकार**: 8 - 20 पॉइंट फॉन्ट
- **भाषा**: 20+ भाषाएं, सिस्टम भाषा को स्वचालित रूप से पहचानता है
- **डिस्प्ले मेट्रिक**: प्रत्येक मेट्रिक को स्वतंत्र रूप से चालू/बंद करें
- **डिस्प्ले प्रारूप**: VRAM / मेमोरी प्रतिशत या वास्तविक मानों के बीच स्विच कर सकती है
- **ऑटो स्टार्ट**: Windows में लॉगिन करने पर स्वचालित रूप से चलाएं

## तकनीकी स्टैक

- **GUI**：Tkinter
- **हार्डवेयर डेटा**：LibreHardwareMonitorLib (pythonnet के माध्यम से), psutil, pynvml (NVIDIA GPU के लिए फॉलबैक)
- **सिस्टम एकीकरण**：pywin32 (विंडो हमेशा सबसे ऊपर, ऑटो-स्टार्ट रजिस्ट्री)
- **पैकेजिंग**：PyInstaller

## परियोजना संरचना

```
ChipPeek/
├── main.py                  # प्रवेश बिंदु
├── monitor_window.py        # विंडो UI और इंटरैक्शन लॉजिक
├── hardware_monitor.py      # हार्डवेयर डेटा संग्रह
├── config.py                # कॉन्फ़िगरेशन प्रबंधन
├── i18n.py                  # अंतर्राष्ट्रीयकरण
├── generate_icon.py         # आइकन जनरेशन स्क्रिप्ट
├── admin.manifest           # UAC व्यवस्थापक विशेषाधिकार मैनिफेस्ट
├── app.ico                  # एप्लिकेशन आइकन
├── app.png                  # आइकन पूर्वावलोकन
├── requirements.txt         # Python निर्भरताएं
├── docs/                    # बहुभाषी दस्तावेज़
│   └── README_*.md
├── i18n/                    # अनुवाद फ़ाइलें
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # संकलित निष्पादन योग्य फ़ाइल
```

## कॉन्फ़िगरेशन फ़ाइल

`config.json` फ़ाइल EXE के समान निर्देशिका में सहेजी जाती है, जिसमें सभी समायोज्य सेटिंग्स होती हैं। सेटिंग्स संशोधित होने पर स्वचालित रूप से सहेजी जाती हैं।

## लाइसेंस

MIT License

## डेवलपर

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- परियोजना URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## श्रेय

- LibreHardwareMonitor - हार्डवेयर मॉनिटरिंग लाइब्रेरी
- psutil - क्रॉस-प्लेटफ़ॉर्म सिस्टम मॉनिटरिंग
- PyInstaller - Python पैकेजिंग टूल
