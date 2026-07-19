# ChipPeek

א לייטווייט פלאָוטינג ווידגעט פֿאַר Windows האַרדוואַרע מאָניטאָרינג. פאַקטיש-צייט מאָניטאָרינג פון CPU/GPU אָפטקייַט, טעמפּעראַטור, VRAM און זכּרון באַניץ, שטענדיק אויבן אַרייַנגערעכנט פולשטענדיק אַפּס.

> **אנדערע שפּראַכן**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | **ייִדיש** | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## פֿעיִקייטן

- **פאַקטיש-צייט מאָניטאָרינג**: CPU אָפטקייַט, CPU טעמפּעראַטור, GPU אָפטקייַט, GPU טעמפּעראַטור, VRAM באַניץ, זכּרון באַניץ
- **צוויי אָנווייַז מאָדעס**: קאָרנער ווידגעט / אויבן באַר, איין-קליק בייגל
- **קוסטאָמיזאַבלע אָנווייַז**: פרײַ קלייַבן וואָס מעטריקס צו ווייַזן, בייגל צווישן פּראָצענט / פאַקטיש וואַלועס
- **שטענדיק אויבן**: בלייבט אויבן אַלע פֿענצטער, אַרבעט אין פולשטענדיק שפילן
- **אויטאָ גרייס**: פֿענצטער ברייט אַוטאָ-אַדזשאַסץ צו פּאַסיק צופרידן
- **אַדזשאַסטאַבלע נוסח**: פֿענצטער אָופּאַסיטי, הינטערגרונט טראַנספּעראַנסי, שריפט גרייס אַלע אַדזשאַסטאַבאַל
- **מולטי-שפּראַך שטיצן**: 20+ שפּראַכן, אַוטאָ-דיטעקט סיסטעם שפּראַך
- **באַקוועם אָפּעראַציע**: לינקס-ציען צו רירן, רעכט-קליק מעניו פֿאַר שנעל סעטטינגס, אַוטאָ קנייַפּ צו עקראַן עדגעס
- **קאַנפיגיעראַבאַל סאַמפּלינג**: 200ms - 3000ms אַדזשאַסטאַבאַל
- **אויטאָ סטאַרט**: לאָנטש אויטאָמאַטיש אויף Windows לאָגין
- **נידעריק רעסורסן נוצן**: מינימאַל פאָוטפּרינט אין הינטערגרונט

## שנעל סטאַרט

### דירעקט נוצן

עפֿנטלעך `ChipPeek.exe` און טאָפּל-קליק צו לויפן (וועט אויטאָמאַטיש בעטן אַדמין פּריוואַלאַדזשאַז פֿאַר CPU טעמפּעראַטור און פּינטלעך אָפטקייַט לייענען).

### לויפֿן פון מקור

```bash
# קלאָן דעם רעפּאָזיטאָרי
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# ינסטאַלירן דעפּענדענסיעס
pip install -r requirements.txt

# לויפֿן
python main.py
```

## סיסטעם רעקווירעמענץ

- Windows 10 / Windows 11
- אַדמיניסטראַטאָר פּריוואַלאַדזשאַז (רעקאַמענדיד), אַנדערש CPU טעמפּעראַטור און פּינטלעך אָפטקייַט זאל ניט בנימצא זיין
- .NET Framework 4.7.2 אָדער העכער (פארלאנגט דורך LibreHardwareMonitor)

## בויען ווי EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

נאָך בויען, די EXE טעקע איז אין `dist/ChipPeek.exe`.

## נויצן

### גרונט אָפּעראַטיאָנס

| אַקציע | באַשרייַבונג |
|------|------|
| לינקס ציען | רירן פֿענצטער שטעלע |
| רעכט גיט | עפענען מעניו (ביסל מאָדע / סעטטינגס / ויסגאַנג) |
| אויטאָ קנייַפּ | אויטאָמאַטיש קנייַפּס ין 20פּקס פון עקראַן עדגעס |

### אָנווייַז מאָדעס

- **קאָרנער ווידגעט**: אַלע מעטריקס עריינדזשד ווערטיקאַלי, קענען זיין געוועזן אין קיין עקראַן קאָרנער
- **אויבן באַר**: אַלע מעטריקס עריינדזשד כאָריזאַנטאַלי, סענטערד אויבן עקראַן בי דיפאָלט

### סעטטינגס

- **אָנווייַז מאָדע**: קאָרנער ווידגעט / אויבן באַר
- **ווידגעט שטעלע**: לאַנד רעכט / לאַנד לינקס / אויבן רעכט / אויבן לינקס
- **פֿענצטער אָופּאַסיטי**: 30% - 100% קוילעלדיק פֿענצטער טראַנספּעראַנסי
- **הינטערגרונט טראַנספּעראַנסי**: 0% - 100% הינטערגרונט טראַנספּעראַנט (טעקסט בלייבט קריספּ)
- **סאַמפּלינג אינטערוואַל**: 200ms - 3000ms דאַטע דערפרישן קורס
- **שריפט גרייס**: 8 - 20 פונט שריפט
- **שפּראַך**: 20+ שפּראַכן, אַוטאָ-דיטעקט סיסטעם שפּראַך
- **אָנווייַז מעטריקס**: טאָגגל יעדעט מעטריק ינדיפּענדאַנטלי
- **אָנווייַז פֿאָרמאַט**: VRAM / זכּרון קענען בייגל צווישן פּראָצענט אָדער פאַקטיש וואַלועס
- **אויטאָ סטאַרט**: לויפֿן אויטאָמאַטיש ווען לאָגינג אין Windows

## טעק סטאַק

- **GUI**：Tkinter
- **האַרדוואַרע דאַטע**：LibreHardwareMonitorLib (דורך pythonnet), psutil, pynvml (NVIDIA GPU פאַלבאַק)
- **סיסטעם ינטעגראַטיאָן**：pywin32 (פֿענצטער טאָפּמאָסט, אויטאָ-סטאַרט רעגיסטרי)
- **פּאַקאַדזשינג**：PyInstaller

## פּרויעקט סטרוקטור

```
ChipPeek/
├── main.py                  # אַרייַנגאַנג פונט
├── monitor_window.py        # פֿענצטער UI און ינטעראַקשאַן לאָגיק
├── hardware_monitor.py      # האַרדוואַרע דאַטע זאַמלונג
├── config.py                # קאַנפיגיעריישאַן פאַרוואַלטונג
├── i18n.py                  # ינטערנאַטיאָנאַליזאַטיאָן
├── generate_icon.py         # בילדל דור סקריפּט
├── admin.manifest           # UAC אַדמין פּריוואַלאַדזש מאַניפעסט
├── app.ico                  # אַפּלאַקיישאַן בילדל
├── app.png                  # בילדל פאָרויסיקע ווייַזונג
├── requirements.txt         # Python דעפּענדענסיעס
├── docs/                    # מאַלטי-שפּראַך דאָקס
│   └── README_*.md
├── i18n/                    # איבערזעצונג טעקעס
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # קאַמפּיילד עקסעקוטאַבלע
```

## קאָנפיגוראַטיאָן טעקע

די `config.json` טעקע איז אפגעהיט אין דער זעלביקער דירעקטורי ווי די EXE, מיט אַלע אַדזשאַסטאַבאַל סעטטינגס. סעטטינגס זענען אפגעהיט אויטאָמאַטיש ווען מאַדאַפייד.

## ליסענץ

MIT License

## דעוועלאָפּער

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- פּרויעקט URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## קרעדיץ

- LibreHardwareMonitor - האַרדוואַרע מאָניטאָרינג ביבליאָטעק
- psutil - קרויס-פּלאַטפאָרמע סיסטעם מאָניטאָרינג
- PyInstaller - Python פּאַקקאַגינג געצייַג
