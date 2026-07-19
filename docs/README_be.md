# ChipPeek

Лёгкі плаваючы віджэт для маніторынга абсталявання Windows. У рэальным часі кантралюе частату CPU/GPU, тэмпературу, VRAM і выкарыстанне памяці, заўсёды знаходзіцца зверху, у тым ліку ў поўнаэкранных прыкладаннях.

> **Іншыя мовы**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | **Беларуская** | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## магчымасці

- **Маніторынг у рэальным часі**: частата CPU, тэмпература CPU, частата GPU, тэмпература GPU, выкарыстанне VRAM, выкарыстанне памяці
- **Два рэжымы адлюстравання**: вуглавы віджэт / верхняя панэль, пераключэнне ў адзін клік
- **Наладжваемы дысплей**: свабодна выбірайце, якія метрыкі паказваць, пераключэнне паміж працэнтамі / фактычнымі значэннямі
- **Заўсёды зверху**: застаецца над усімі вокнамі, працуе ў поўнаэкранных гульнях
- **Аўтаматычны размер**: шырыня акна аўтаматычна падганяецца пад змест
- **Наладжвальны стыль**: празрыстасць акна, празрыстасць фону, памер шрыфта — усё можна наладзіць
- **Падтрымка многіх моў**: больш за 20 моў, аўтаматычнае вызначэнне мовы сістэмы
- **Зручная праца**: перацягванне левай кнопкай для перамяшчэння, меню правага кліка для хуткіх наладаў, аўтаматычнае прыцягванне да краяў экрана
- **Наладжваемая выборка**: 200 мс - 3000 мс з магчымасцю налады
- **Аўтазапуск**: аўтаматычны запуск пры уваходзе ў Windows
- **Нізкае спажыванне рэсурсаў**: мінімальнае нагрузка ў фонавым рэжыме

## Хуткі старт

### Непасрэднае выкарыстанне

Загрузіце `ChipPeek.exe` і двойчы клікіце для запуску (аўтаматычна запытае права адміністратара для зчытвання тэмпературы CPU і дакладнай частаты).

### Запуск з зыходнага коду

```bash
# Кланаваць рэпазітар
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Усталяваць залежнасці
pip install -r requirements.txt

# Запуск
python main.py
```

## Сістэмныя патрабаванні

- Windows 10 / Windows 11
- Правы адміністратара (рэкамендуецца), у адваротным выпадку тэмпература CPU і дакладная частата могуць быць недаступныя
- .NET Framework 4.7.2 або вышэй (патрабуецца LibreHardwareMonitor)

## Зборка ў EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Пасля зборкі EXE-файл знаходзіцца па шляху `dist/ChipPeek.exe`.

## Выкарыстанне

### Основныя аперацыі

| Дзеянне | Апісанне |
|------|------|
| Левае перацягванне | Перамясціць пазіцыю акна |
| Правы клік | Адкрыць меню (перамкнуць рэжым / налады / выхад) |
| Аўтаматычнае прыцягванне | Аўтаматычна прыцягваецца ў межах 20 пікселяў ад краяў экрана |

### Рэжымы адлюстравання

- **Вуглавы віджэт**: усе метрыкі размяшчаюцца вертикальна, можна размясціць у любым куце экрана
- **Верхняя панэль**: усе метрыкі размяшчаюцца гарызантальна, па змаўчанні цэнтруюцца ўверху экрана

### Налады

- **Рэжым адлюстравання**: вуглавы віджэт / верхняя панэль
- **Пазіцыя віджэта**: ніжні правы / ніжні левы / верхні правы / верхні левы кут
- **Празрыстасць акна**: 30% - 100% агульная празрыстасць акна
- **Празрыстасць фону**: 0% - 100% празрыстасць фону (тэкст застаецца чыткім)
- **Інтэрвал выборкі**: 200 мс - 3000 мс часта абнаўлення дадзеных
- **Памер шрыфта**: 8 - 20 пунктоў шрыфта
- **Мова**: больш за 20 моў, аўтаматычнае вызначэнне мовы сістэмы
- **Метрыкі для адлюстравання**: пераключэнне кожнай метрыкі незалежна
- **Фармат адлюстравання**: VRAM / памяць могуць пераключацца паміж працэнтамі або фактычнымі значэннямі
- **Аўтазапуск**: аўтаматычны запуск пры уваходзе ў Windows

## Тэхналагічны стек

- **GUI**：Tkinter
- **Дадзеныя абсталявання**：LibreHardwareMonitorLib (праз pythonnet), psutil, pynvml (рэзервны для GPU NVIDIA)
- **Сістэмная інтэграцыя**：pywin32 (акна зверху, рэестр аўтазапуску)
- **Упакоўка**：PyInstaller

## Структура праекта

```
ChipPeek/
├── main.py                  # Точка ўходу
├── monitor_window.py        # UI акна і логіка ўзаемадзеяння
├── hardware_monitor.py      # Збор дадзеных абсталявання
├── config.py                # Кіраванне канфігурацыяй
├── i18n.py                  # Інтэрнацыяналізацыя
├── generate_icon.py         # Скрыпт генерацыі значкі
├── admin.manifest           # Маніфест прав адміністратара UAC
├── app.ico                  # Значка прыкладання
├── app.png                  # Папярэдні прагляд значкі
├── requirements.txt         # Залежнасці Python
├── docs/                    # Шматмоўная дакументацыя
│   └── README_*.md
├── i18n/                    # Файлы перакладу
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Скампіляваны выконваемы файл
```

## Канфігурацыйны файл

Файл `config.json` захоўваецца ў тым жа каталозе, што і EXE, і ўтрымлівае усе наладжваемыя параметры. Налады захоўваюцца аўтаматычна пры змене.

## Ліцэнзія

MIT License

## Распрацоўшчык

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL праекта: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Падзякі

- LibreHardwareMonitor - Бібліятэка маніторынга абсталявання
- psutil - Красплатформенны сістэмны маніторынг
- PyInstaller - Інструмент упакоўкі Python
