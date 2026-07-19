# ChipPeek

כלי ניטור חומרה צף קל ל-Windows. ניטור בזמן אמת של תדר CPU/GPU, טמפרטורה, VRAM ושימוש בזיכרון, תמיד נמצא למעלה כולל באפליקציות מסך מלא.

> **שפות אחרות**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | **עברית** | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## תכונות

- **ניטור בזמן אמת**: תדר CPU, טמפרטורת CPU, תדר GPU, טמפרטורת GPU, שימוש ב-VRAM, שימוש בזיכרון
- **שני מצבי תצוגה**: וידג'ט פינתי / סרגל עליון, מעבר בלחיצה אחת
- **תצוגה מותאמת אישית**: בחרו בחופשיות אילו מדדים להציג, עברו בין אחוזים/ערכים ממשיים
- **תמיד למעלה**: נשאר מעל כל החלונות, עובד במשחקי מסך מלא
- **גודל אוטומטי**: רוחב החלון מותאם אוטומטית לפי התוכן
- **סגנון הניתן לכיוון**: שקיפות חלון, שקיפות רקע, גודל גופן - הכל ניתן לכיוון
- **תמיכה מרובת שפות**: 20+ שפות, מזהה אוטומטית את שפת המערכת
- **פעולה פשוטה**: גררו עם לחיצה שמאלית כדי להזיז, תפריט לחיצה ימנית להגדרות מהירות, הצמדה אוטומטית לשולי המסך
- **כיוון תדר דגימה**: 200ms - 3000ms ניתן לכיוון
- **הפעלה אוטומטית**: מופעל אוטומטית עם כניסה ל-Windows
- **שימוש נמוך במשאבים**: משתמש במקום מינימלי ברקע

## התחלה מהירה

### שימוש ישיר

הורידו את `ChipPeek.exe` ולחצו פעמיים כדי להפעיל (יבקש באופן אוטומטי הרשאות מנהל לקריאת טמפרטורת CPU ותדר מדויקת).

### הפעלה מקוד מקור

```bash
# שיבוט המאגר
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# התקנת תלותיות
pip install -r requirements.txt

# הפעלה
python main.py
```

## דרישות מערכת

- Windows 10 / Windows 11
- הרשאות מנהל (מומלץ), אחרת טמפרטורת CPU ותדר מדויקת עשויים שלא להיות זמינים
- .NET Framework 4.7.2 ומעלה (נדרש עבור LibreHardwareMonitor)

## בנייה כ-EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

לאחר הבנייה, קובץ ה-EXE נמצא ב-`dist/ChipPeek.exe`.

## שימוש

### פעולות בסיסיות

| פעולה | תיאור |
|------|------|
| גרירה בלחיצה שמאלית | הזזת מיקום החלון |
| לחיצה ימנית | פתיחת תפריט (החלפת מצב / הגדרות / יציאה) |
| הצמדה אוטומטית | נצמד אוטומטית בטווח של 20px משולי המסך |

### מצבי תצוגה

- **וידג'ט פינתי**: כל המדדים מסודרים אנכית, ניתן למקם בכל פינת המסך
- **סרגל עליון**: כל המדדים מסודרים אופקית, כברירת מחדל ממוקם במרכז החלק העליון של המסך

### הגדרות

- **מצב תצוגה**: וידג'ט פינתי / סרגל עליון
- **מיקום וידג'ט**: ימינה למטה / שמאלה למטה / ימינה למעלה / שמאלה למעלה
- **שקיפות חלון**: 30% - 100% שקיפות חלון כללית
- **שקיפות רקע**: 0% - 100% שקיפות רקע (הטקסט נשאר ברור)
- **מרווח דגימה**: 200ms - 3000ms קצב רענון נתונים
- **גודל גופן**: 8 - 20 נקודות
- **שפה**: 20+ שפות, מזהה אוטומטית את שפת המערכת
- **מדדי תצוגה**: ניתן להפעיל/לכבות כל מדד בצורה עצמאית
- **פורמט תצוגה**: VRAM / זיכרון ניתן לעבור בין אחוזים לערכים ממשיים
- **הפעלה אוטומטית**: הפעלה אוטומטית עם כניסה ל-Windows

## ערימת טכנולוגיה

- **GUI**：Tkinter
- **נתוני חומרה**：LibreHardwareMonitorLib (באמצעות pythonnet), psutil, pynvml (גיבוי עבור NVIDIA GPU)
- **אינטגרציה עם מערכת**：pywin32 (חלון תמיד למעלה, רישום הפעלה אוטומטית)
- **אריזה**：PyInstaller

## מבנה הפרויקט

```
ChipPeek/
├── main.py                  # נקודת כניסה
├── monitor_window.py        # חלון UI ולוגיקת אינטראקציה
├── hardware_monitor.py      # איסוף נתוני חומרה
├── config.py                # ניהול תצורה
├── i18n.py                  # בינלאומיות
├── generate_icon.py         # סקריפט יצירת אייקון
├── admin.manifest           # מניפסט הרשאות מנהל UAC
├── app.ico                  # אייקון אפליקציה
├── app.png                  # תצוגה מקדימה של אייקון
├── requirements.txt         # תלותיות Python
├── docs/                    # תיעוד מרובה שפות
│   └── README_*.md
├── i18n/                    # קבצי תרגום
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # קובץ הפעלה בנוי
```

## קובץ תצורה

קובץ `config.json` נשמר באותה תיקיה של ה-EXE ומכיל את כל ההגדרות הניתנות לכיוון. ההגדרות נשמרות אוטומטית כשישתנו.

## רישיון

MIT License

## מפתח

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- כתובת הפרויקט: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## קרדיטים

- LibreHardwareMonitor - ספריית ניטור חומרה
- psutil - ניטור מערכת חוצה פלטפורמות
- PyInstaller - כלי אריזת Python
