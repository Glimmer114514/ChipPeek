# ChipPeek

Windows साठी एक हलके वजनाचे फ्लोटिंग हार्डवेअर मॉनिटरिंग विजेट. CPU/GPU फ्रिक्वेन्सी, तापमान, VRAM आणि मेमरी वापराचे रिअल-टाइम मॉनिटरिंग, पूर्ण-स्क्रीन अॅप्ससह नेहमी वर राहते.

> **इतर भाषा**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | **मराठी** | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## वैशिष्ट्ये

- **रिअल-टाइम मॉनिटरिंग**: CPU फ्रिक्वेन्सी, CPU तापमान, GPU फ्रिक्वेन्सी, GPU तापमान, VRAM वापर, मेमरी वापर
- **दोन डिस्प्ले मोड**: कॉर्नर विजेट / टॉप बार, एका क्लिकवर स्विच करा
- **सानुकूलित डिस्प्ले**: कोणती मेट्रिक्स दर्शवायची ते मुक्तपणे निवडा, टक्केवारी/वास्तविक मूल्ये यांच्यात स्विच करा
- **नेहमी वर**: सर्व विंडोच्या वर राहते, पूर्ण-स्क्रीन गेममध्ये कार्य करते
- **स्वयंचलित आकार**: सामग्रीवर आधारित विंडो रुंदी स्वयंचलितपणे समायोजित केली जाते
- **समायोज्य शैली**: विंडो पारदर्शकता, पार्श्वभूमी पारदर्शकता, फॉन्ट आकार - सर्व समायोज्य
- **बहुभाषी समर्थन**: 20+ भाषा, स्वयंचलितपणे सिस्टम भाषा शोधते
- **सोपे ऑपरेशन**: डाव्या क्लिकने ड्रॅग करा आणि हलवा, उजव्या क्लिक मेनू द्रुत सेटिंग्जसाठी, स्क्रीन कडा येथे स्वयंचलित स्नॅप
- **सॅम्पलिंग फ्रिक्वेन्सी समायोजन**: 200ms - 3000ms समायोज्य
- **ऑटो स्टार्ट**: Windows मध्ये लॉगिन वर स्वयंचलितपणे सुरू होते
- **कमी संसाधन वापर**: पार्श्वभूमीमध्ये किमान जागा

## जलद प्रारंभ

### थेट वापर

`ChipPeek.exe` डाउनलोड करा आणि चालवण्यासाठी डबल-क्लिक करा (CPU तापमान आणि अचूक फ्रिक्वेन्सी वाचण्यासाठी स्वयंचलितपणे प्रशासकीय परवानगी मागेल).

### स्त्रोतावरून चालवा

```bash
# रिपॉझिटरी क्लोन करा
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# अवलंबने स्थापित करा
pip install -r requirements.txt

# चालवा
python main.py
```

## सिस्टम आवश्यकता

- Windows 10 / Windows 11
- प्रशासकीय परवानगी (शिफारसी), अन्यथा CPU तापमान आणि अचूक फ्रिक्वेन्सी उपलब्ध असू शकत नाही
- .NET Framework 4.7.2 किंवा उच्च (LibreHardwareMonitor साठी आवश्यक)

## EXE म्हणून बिल्ड करा

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

बिल्ड केल्यानंतर, EXE फाइल `dist/ChipPeek.exe` मध्ये आहे.

## वापर

### मूलभूत ऑपरेशन्स

| ऑपरेशन | विवरण |
|------|------|
| डावा क्लिक ड्रॅगिंग | विंडो स्थिती हलवा |
| उजवा क्लिक | मेनू उघडा (मोड स्विच करा / सेटिंग्ज / बाहेर पडा) |
| ऑटो स्नॅप | स्क्रीन कडा पासून 20px आत स्वयंचलितपणे स्नॅप होते |

### डिस्प्ले मोड

- **कॉर्नर विजेट**: सर्व मेट्रिक्स अनुलंब क्रमाने मांडलेले आहेत, स्क्रीनच्या कोणत्याही कोप्यात ठेवता येतात
- **टॉप बार**: सर्व मेट्रिक्स आडव्या क्रमाने मांडलेले आहेत, डीफॉल्टनुसार स्क्रीनच्या शीर्षस्थानी मध्यभागी आहेत

### सेटिंग्ज

- **डिस्प्ले मोड**: कॉर्नर विजेट / टॉप बार
- **विजेट स्थिती**: खाली उजवीकडे / खाली डावीकडे / वर उजवीकडे / वर डावीकडे
- **विंडो पारदर्शकता**: 30% - 100% एकूण विंडो पारदर्शकता
- **पार्श्वभूमी पारदर्शकता**: 0% - 100% पार्श्वभूमी पारदर्शकता (मजकूर स्पष्ट राहतो)
- **सॅम्पलिंग मध्यांतर**: 200ms - 3000ms डेटा रिफ्रेश दर
- **फॉन्ट आकार**: 8 - 20 पॉइंट्स
- **भाषा**: 20+ भाषा, स्वयंचलितपणे सिस्टम भाषा शोधते
- **डिस्प्ले मेट्रिक्स**: प्रत्येक मेट्रिक्स स्वतंत्रपणे ऑन/ऑफ करा
- **डिस्प्ले फॉरमॅट**: VRAM / मेमरी टक्केवारी किंवा वास्तविक मूल्ये यांच्यात स्विच करू शकते
- **ऑटो स्टार्ट**: Windows मध्ये लॉगिन वर स्वयंचलितपणे चालवा

## टेक स्टॅक

- **GUI**：Tkinter
- **हार्डवेअर डेटा**：LibreHardwareMonitorLib (pythonnet द्वारे), psutil, pynvml (NVIDIA GPU साठी बॅकअप)
- **सिस्टम इंटिग्रेशन**：pywin32 (विंडो नेहमी वर, ऑटो स्टार्ट रजिस्ट्री)
- **पॅकेजिंग**：PyInstaller

## प्रकल्प रचना

```
ChipPeek/
├── main.py                  # प्रवेश बिंदू
├── monitor_window.py        # विंडो UI आणि परस्परसंवाद तर्कशास्त्र
├── hardware_monitor.py      # हार्डवेअर डेटा संकलन
├── config.py                # कॉन्फिगरेशन व्यवस्थापन
├── i18n.py                  # आंतरराष्ट्रीयीकरण
├── generate_icon.py         # आयकन निर्मिती स्क्रिप्ट
├── admin.manifest           # UAC प्रशासकीय परवानगी मॅनिफेस्ट
├── app.ico                  # अनुप्रयोग आयकन
├── app.png                  # आयकन पूर्वावलोकन
├── requirements.txt         # Python अवलंबने
├── docs/                    # बहुभाषी दस्तऐवजीकरण
│   └── README_*.md
├── i18n/                    # भाषांतर फाईल्स
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # बिल्ड केलेले एक्झिक्युटेबल
```

## कॉन्फिगरेशन फाइल

`config.json` फाइल EXE च्या त्याच डिरेक्टरीमध्ये सेव्ह केली जाते आणि सर्व समायोज्य सेटिंग्ज असतात. सेटिंग्ज बदलल्यावर स्वयंचलितपणे सेव्ह होतात.

## परवाना

MIT License

## डेव्हलपर

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- प्रकल्प URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## क्रेडिट्स

- LibreHardwareMonitor - हार्डवेअर मॉनिटरिंग लायब्ररी
- psutil - क्रॉस-प्लॅटफॉर्म सिस्टम मॉनिटरिंग
- PyInstaller - Python पॅकेजिंग टूल
