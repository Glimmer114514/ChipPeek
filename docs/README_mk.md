# ChipPeek

Лесен Windows хардверски монитор лебдечки виџет. Мониторинг во реално време на CPU/GPU фреквенција, температура, VRAM и употреба на меморија, секогаш на врв вклучувајќи ги и целите екрански апликации.

> **Други јазици**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | **Македонски** | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Карактеристики

- **Мониторинг во реално време**: CPU фреквенција, CPU температура, GPU фреквенција, GPU температура, VRAM употреба, употреба на меморија
- **Два режима на приказ**: Аголен виџет / Горна лента, промена со едно кликнување
- **Прилагодлив приказ**: Слободно изберете кои метрики да се прикажат, префрлување помеѓу процент / реални вредности
- **Секогаш на врв**: Останува над сите прозорци, работи и при цели екрански игри
- **Автоматска големина**: Ширината на прозорецот се прилагодува автоматски на содржината
- **Прилагодлив стил**: Непрозирност на прозорецот, прозирност на позадината, големина на фонтот - сите се подесливи
- **Поддршка за повеќе јазици**: 20+ јазици, автоматски детектира јазициот на системот
- **Удобна операција**: Преместување со влечење на лево, брзи поставки со десно кликнување мени, автоматско закачување на работите на екранот
- **Подеслив семплинг**: 200ms - 3000ms подесливо
- **Автоматско стартување**: Автоматски се стартува при логирање на Windows
- **Ниска потрошувачка на ресурси**: Минимална зафатност во позадина

## Брз почеток

### Директна употреба

Преземете го `ChipPeek.exe` и стартувате со двојно кликнување (автоматски ќе побара администраторски привилегии за CPU температура и точно читање на фреквенцијата).

### Стартување од изворен код

```bash
# Клонирај го репозиториумот
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Инсталирај ги зависностите
pip install -r requirements.txt

# Стартувај
python main.py
```

## Системски барања

- Windows 10 / Windows 11
- Администраторски привилегии (препорачано), инаку CPU температура и точна фреквенција може да не се достапни
- .NET Framework 4.7.2 или повисоко (потребно од LibreHardwareMonitor)

## Изградба како EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

По изградбата, EXE датотеката се наоѓа на `dist/ChipPeek.exe`.

## Употреба

### Основни операции

| Акција | Опис |
|------|------|
| Лево влечење | Промена на позицијата на прозорецот |
| Десен клик | Отвори мени (промени режим / поставки / излез) |
| Автоматско закачување | Автоматски се закачува на 20px од работите на екранот |

### Режими на приказ

- **Аголен виџет**: Сите метрики се подредени вертикално, можат да се постават во било кој агол на екранот
- **Горна лента**: Сите метрики се подредени хоризонтално, стандардно се наоѓаат на горниот дел од екранот центрирано

### Поставки

- **Режим на приказ**: Аголен виџет / Горна лента
- **Позиција на виџетот**: Долу десно / Долу лево / Горе десно / Горе лево
- **Непрозирност на прозорецот**: 30% - 100% вкупна непрозирност на прозорецот
- **Прозирност на позадината**: 0% - 100% прозирна позадина (текстот останува јасен)
- **Интервал на земање примероци**: 200ms - 3000мс брзина на освежување на податоци
- **Големина на фонтот**: 8 - 20 точки фонт
- **Јазик**: 20+ јазици, автоматски детектира јазициот на системот
- **Метрики за приказ**: Секој метрички се вклучува/исклучува независно
- **Формат на приказ**: VRAM / Меморија може да се префрлува помеѓу процент или реални вредности
- **Автоматско стартување**: Автоматски се стартува при логирање на Windows

## Технолошки стек

- **GUI**：Tkinter
- **Хардверски податоци**：LibreHardwareMonitorLib (преку pythonnet), psutil, pynvml (резервна за NVIDIA GPU)
- **Системска интеграција**：pywin32 (прозорец на врв, регистар за автоматско стартување)
- **Пакетирање**：PyInstaller

## Структура на проектот

```
ChipPeek/
├── main.py                  # Влезна точка
├── monitor_window.py        # UI на прозорецот и логика за интеракција
├── hardware_monitor.py      # Собирање на хардверски податоци
├── config.py                # Управување со конфигурација
├── i18n.py                  # Интернационализација
├── generate_icon.py         # Скрипта за генерирање на икона
├── admin.manifest           # Манифест за UAC администраторски привилегии
├── app.ico                  # Икона на апликацијата
├── app.png                  # Преглед на иконата
├── requirements.txt         # Python зависности
├── docs/                    # Многојазична документација
│   └── README_*.md
├── i18n/                    # Преводни датотеки
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Компајлирана извршна датотека
```

## Конфигурациска датотека

`config.json` датотеката е зачувана во истиот директориум како и EXE, содржи сите подесливи поставки. Поставките се зачувуваат автоматски кога се менуваат.

## Лиценца

MIT License

## Развојник

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL на проектот: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Забележки

- LibreHardwareMonitor - Библиотека за хардверски мониторинг
- psutil - Крос-платформен системски мониторинг
- PyInstaller - Алатка за пакетирање на Python
