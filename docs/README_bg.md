# ChipPeek

Лек плаващ уиджет за мониторинг на хардуер за Windows. Мониторинг в реално време на честотата на CPU/GPU, температура, VRAM и използване на памет, винаги най-отгоре, включително и на приложения на цял екран.

> **Други езици**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | **Български** | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Функции

- **Мониторинг в реално време**: честота на CPU, температура на CPU, честота на GPU, температура на GPU, използване на VRAM, използване на памет
- **Два режима на показване**: ъглов уиджет / горна лента, превключване с едно кликване
- **Персонализирано показване**: свободно избирайте кои показатели да се показват, превключване между проценти/реални стойности
- **Винаги най-отгоре**: остава над всички прозорци, работи и в игри на цял екран
- **Автоматичен размер**: ширината на прозореца се регулира автоматично съгласно съдържанието
- **Регулируем стил**: непрозрачност на прозореца, прозрачност на фона, размер на шрифта - всичко е регулируемо
- **Поддръжка на много езици**: 20+ езика, автоматично разпознава езика на системата
- **Удобно управление**: премествайте с ляв бутон, меню с десен бутон за бързи настройки, автоматично прилепяне към ръбовете на екрана
- **Конфигурируема честота на дискретизация**: 200ms - 3000ms регулируема
- **Автоматично стартиране**: стартира автоматично при влизане в Windows
- **Ниска консумация на ресурси**: минимална натоварване във фонов режим

## Бърз старт

### Директна употреба

Изтеглете `ChipPeek.exe` и кликнете два пъти за стартиране (автоматично ще поиска администраторски права за температура на CPU и точно четене на честотата).

### Стартиране от изходен код

```bash
# Клонирайте хранилището
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Инсталирайте зависимости
pip install -r requirements.txt

# Стартирайте
python main.py
```

## Системни изисквания

- Windows 10 / Windows 11
- Администраторски права (препоръчително), в противен случай температурата на CPU и точната честота може да не са налични
- .NET Framework 4.7.2 или по-нов (изисква се от LibreHardwareMonitor)

## Изграждане като EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

След изграждането, EXE файлът се намира на `dist/ChipPeek.exe`.

## Употреба

### Основни операции

| Операция | Описание |
|------|------|
| Плащане с ляв бутон | Преместване на прозореца |
| Десен бутон | Отваряне на меню (промяна на режим / настройки / изход) |
| Автоматично прилепяне | Автоматично се прилепя в рамките на 20px от ръбовете на екрана |

### Режими на показване

- **Ъглов уиджет**: всички показатели подредени вертикално, могат да се поставят във всеки ъгъл на екрана
- **Горна лента**: всички показатели подредени хоризонтално, по подразбиране центрирани в горната част на екрана

### Настройки

- **Режим на показване**: ъглов уиджет / горна лента
- **Позиция на уиджета**: вдясно отдолу / вляво отдолу / вдясно отгоре / вляво отгоре
- **Непрозрачност на прозореца**: 30% - 100% обща прозрачност на прозореца
- **Прозрачност на фона**: 0% - 100% прозрачен фон (текстът остава ясен)
- **Интервал на дискретизация**: 200ms - 3000ms честота на опресняване на данни
- **Размер на шрифта**: 8 - 20 точки
- **Език**: 20+ езика, автоматично разпознава езика на системата
- **Показатели**: всеки показател може да се включи/изключи независимо
- **Формат на показване**: VRAM / Памет могат да се превключват между проценти или реални стойности
- **Автоматично стартиране**: стартиране автоматично при влизане в Windows

## Технологичен стек

- **GUI**：Tkinter
- **Хардуерни данни**：LibreHardwareMonitorLib (чрез pythonnet), psutil, pynvml (резервно решение за NVIDIA GPU)
- **Системна интеграция**：pywin32 (прозорец винаги най-отгоре, регистър за автоматично стартиране)
- **Опаковане**：PyInstaller

## Структура на проекта

```
ChipPeek/
├── main.py                  # Входна точка
├── monitor_window.py        # UI на прозореца и логика за взаимодействие
├── hardware_monitor.py      # Събиране на хардуерни данни
├── config.py                # Управление на конфигурацията
├── i18n.py                  # Интернационализация
├── generate_icon.py         # Скрипт за генериране на икони
├── admin.manifest           # Манифест за администраторски права UAC
├── app.ico                  # Икона на приложението
├── app.png                  # Преглед на иконата
├── requirements.txt         # Python зависимости
├── docs/                    # Многоезикова документация
│   └── README_*.md
├── i18n/                    # Преводни файлове
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Компилиран изпълним файл
```

## Конфигурационен файл

Файлът `config.json` се запазва в същата директория като EXE и съдържа всички регулируеми настройки. Настройките се запазват автоматично при промяна.

## Лиценз

MIT License

## Разработчик

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL на проекта: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Благодарности

- LibreHardwareMonitor - Библиотека за мониторинг на хардуер
- psutil - Междуплатформено мониторинг на системата
- PyInstaller - Инструмент за опаковане на Python
