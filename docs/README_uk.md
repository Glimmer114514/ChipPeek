# ChipPeek

Легкий плаваючий віджет для моніторингу апаратного забезпечення для Windows. Моніторинг в реальному часі частоти CPU/GPU, температури, VRAM та використання пам'яті, завжди зверху, включаючи повноекранні програми.

> **Інші мови**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | **Українська** | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Особливості

- **Моніторинг в реальному часі**: частота CPU, температура CPU, частота GPU, температура GPU, використання VRAM, використання пам'яті
- **Два режими відображення**: віджет у куті / верхня панель, перемикання одним кліком
- **Налаштовуване відображення**: вільно вибирайте, які метрики показувати, перемикання між відсотками/фактичними значеннями
- **Завжди зверху**: залишається над усіма вікнами, працює в повноекранних іграх
- **Автоматичний розмір**: ширина вікна автоматично підлаштовується під вміст
- **Регульований стиль**: непрозорість вікна, прозорість фону, розмір шрифту - все можна налаштувати
- **Багатомовна підтримка**: 20+ мов, автоматично визначає мову системи
- **Зручне керування**: перетягування лівою кнопкою для переміщення, меню правої кнопки для швидких налаштувань, автоматичне прилипання до країв екрану
- **Налаштовувана частота дискретизації**: 200ms - 3000ms регульована
- **Автозапуск**: запускається автоматично при вході в Windows
- **Низьке споживання ресурсів**: мінімальне навантаження у фоновому режимі

## Швидкий старт

### Безпосереднє використання

Завантажте `ChipPeek.exe` і двічі клацніть для запуску (автоматично запитає права адміністратора для температури CPU та точного зчитування частоти).

### Запуск з вихідного коду

```bash
# Клонувати репозиторій
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Встановити залежності
pip install -r requirements.txt

# Запустити
python main.py
```

## Системні вимоги

- Windows 10 / Windows 11
- Права адміністратора (рекомендовано), інакше температура CPU та точна частота можуть бути недоступні
- .NET Framework 4.7.2 або вище (вимагається LibreHardwareMonitor)

## Збірка як EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Після збірки файл EXE знаходиться за адресою `dist/ChipPeek.exe`.

## Використання

### Основні операції

| Операція | Опис |
|------|------|
| Перетягування лівою кнопкою | Переміщення вікна |
| Права кнопка | Відкрити меню (зміна режиму / налаштування / вихід) |
| Автоматичне прилипання | Автоматично прилипає в межах 20px від країв екрану |

### Режими відображення

- **Віджет у куті**: усі метрики розташовані вертикально, можна розмістити у будь-якому куті екрану
- **Верхня панель**: усі метрики розташовані горизонтально, за замовчуванням зцентровані у верхній частині екрану

### Налаштування

- **Режим відображення**: віджет у куті / верхня панель
- **Положення віджета**: справа знизу / зліва знизу / справа вгорі / зліва вгорі
- **Непрозорість вікна**: 30% - 100% загальна прозорість вікна
- **Прозорість фону**: 0% - 100% прозорий фон (текст залишається чітким)
- **Інтервал дискретизації**: 200ms - 3000ms частота оновлення даних
- **Розмір шрифту**: 8 - 20 пунктів
- **Мова**: 20+ мов, автоматично визначає мову системи
- **Метрики відображення**: увімкнути/вимкнути кожну метрику незалежно
- **Формат відображення**: VRAM / Пам'ять можуть перемикатися між відсотками або фактичними значеннями
- **Автозапуск**: автоматичний запуск при вході в Windows

## Технологічний стек

- **GUI**：Tkinter
- **Дані апаратного забезпечення**：LibreHardwareMonitorLib (через pythonnet), psutil, pynvml (резервний варіант для NVIDIA GPU)
- **Системна інтеграція**：pywin32 (вікно завжди зверху, реєстр автозапуску)
- **Упаковка**：PyInstaller

## Структура проекту

```
ChipPeek/
├── main.py                  # Точка входу
├── monitor_window.py        # UI вікна та логіка взаємодії
├── hardware_monitor.py      # Збір даних апаратного забезпечення
├── config.py                # Управління конфігурацією
├── i18n.py                  # Інтернаціоналізація
├── generate_icon.py         # Скрипт генерації піктограм
├── admin.manifest           # Маніфест прав адміністратора UAC
├── app.ico                  # Піктограма програми
├── app.png                  # Перегляд піктограми
├── requirements.txt         # Залежності Python
├── docs/                    # Багатомовна документація
│   └── README_*.md
├── i18n/                    # Файли перекладів
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Скомпільований виконуваний файл
```

## Файл конфігурації

Файл `config.json` зберігається в тому ж каталозі, що й EXE, і містить усі налаштовувані налаштування. Налаштування зберігаються автоматично при зміні.

## Ліцензія

MIT License

## Розробник

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL проекту: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Подяки

- LibreHardwareMonitor - Бібліотека моніторингу апаратного забезпечення
- psutil - Міжплатформенний моніторинг системи
- PyInstaller - Інструмент упаковки Python
