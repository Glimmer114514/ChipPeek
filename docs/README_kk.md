# ChipPeek

Windows үшін жеңіл қозғалтқыштық аппараттық қамтама мониторингі виджеті. CPU/GPU жиілігі, температурасы, VRAM және жадтың пайдаланылуының нақты уақыт мониторингі, толық экран қолданбаларында да әрқашан жоғарыда болады.

> **Басқа тілдер**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | **Қазақша** | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Ерекшеліктер

- **Нақты уақыт мониторингі**: CPU жиілігі, CPU температурасы, GPU жиілігі, GPU температурасы, VRAM пайдаланылуы, жадтың пайдаланылуы
- **Екі дисплей режимі**: Бұрыш виджеті / Төменгі панель, бір шертумен ауыстыру
- **Бапталған дисплей**: Қандай метриктерді көрсету керектігін еркін таңдаңыз, пайыздық/нақты мәндер арасында ауыстыру
- **Әрқашан жоғарыда**: Барлық терезелердің жоғарыда болады, толық экран ойындарында жұмыс істейді
- **Автоматты өлшем**: Мазмұнға сәйкес терезенің ені автоматты түрде бапталады
- **Бапталған стиль**: Терезе көріністігі, фон көріністігі, қаріп өлшемі - бәрі де бапталады
- **Көп тілді қолдау**: 20+ тіл, автоматты түрде жүйе тілін анықтайды
- **Оңай операция**: Сол шертумен сүйреп жылжытыңыз, оң шерту мәзірінде тез баптаулар, экран жиегінде автоматты бекіту
- **Үлгілеу жиілігінің баптауы**: 200ms - 3000ms бапталады
- **Авто бастау**: Windows ішкі кіргенде автоматты түрде басталады
- **Аз ресурс пайдаланылуы**: Фонда минималды орын

## Тез бастау

### Тікелей қолдану

`ChipPeek.exe` жүктеп алыңыз және іске қосу үшін қос шертумен басыңыз (CPU температурасы мен дәл жиілікті оқу үшін автоматты түрде әкімшілік құқық сұрайды).

### Бастапқы кодтан іске қосу

```bash
# Репозиторийді клондаңыз
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Тәуелділіктерді орнатыңыз
pip install -r requirements.txt

# Іске қосыңыз
python main.py
```

## Жүйе талаптары

- Windows 10 / Windows 11
- Әкімшілік құқық (Ұсынылады), әйтпесе CPU температурасы мен дәл жиілік жеткіліксіз болуы мүмкін
- .NET Framework 4.7.2 немесе жоғары (LibreHardwareMonitor үшін қажет)

## EXE ретінде құру

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Құрылғаннан кейін, EXE файлы `dist/ChipPeek.exe` орналасады.

## Қолдану

### Негізгі операциялар

| Операция | Сипаттама |
|------|------|
| Сол шертумен сүйрету | Терезенің орналасуын жылжыту |
| Оң шерту | Мәзірді ашу (режимді ауыстыру / баптаулар / шығу) |
| Авто бекіту | Экран жиегінен 20px ішінде автоматты түрде бекітіледі |

### Дисплей режимдері

- **Бұрыш виджеті**: Барлық метриктер тік келесідей қойылған, экранның кез-келген бұрышында қойға болады
- **Төменгі панель**: Барлық метриктер көлденең қойылған, күйінде экранның жоғарғы бөлігінде ортада орналасқан

### Баптаулар

- **Дисплей режимі**: Бұрыш виджеті / Төменгі панель
- **Виджет орналасуы**: Төмен оң / Төмен сол / Жоғары оң / Жоғары сол
- **Терезе көріністігі**: 30% - 100% жалпы терезе көріністігі
- **Фон көріністігі**: 0% - 100% фон көріністігі (мәтін түсінікті болады)
- **Үлгілеу аралығы**: 200ms - 3000ms деректі жаңарту жылдамдығы
- **Қаріп өлшемі**: 8 - 20 нүктелер
- **Тіл**: 20+ тіл, автоматты түрде жүйе тілін анықтайды
- **Дисплей метриктері**: Әр метрикті өздігінен қосу/өшіру
- **Дисплей форматы**: VRAM / жад пайыздық немесе нақты мәндер арасында ауыстыруға болады
- **Авто бастау**: Windows ішкі кіргенде автоматты түрде іске қосу

## Техникалық стек

- **GUI**：Tkinter
- **Аппараттық деректер**：LibreHardwareMonitorLib (pythonnet арқылы), psutil, pynvml (NVIDIA GPU үшін резервтік)
- **Жүйе интеграциясы**：pywin32 (терезе әрқашан жоғарыда, авто бастау тізімі)
- **Тапсыру**：PyInstaller

## Жобаның құрылымы

```
ChipPeek/
├── main.py                  # кіріс нүктесі
├── monitor_window.py        # терезе UI және өзара әрекеттесу логикасы
├── hardware_monitor.py      # аппараттық деректерді жинау
├── config.py                # конфигурацияны басқару
├── i18n.py                  # халықаралық және
├── generate_icon.py         # белгіну құру скрипті
├── admin.manifest           # UAC әкімшілік құқық Manifest
├── app.ico                  # қолданбасы иконкасы
├── app.png                  # иконкасының алдын ала көру
├── requirements.txt         # Python тәуелділіктері
├── docs/                    # көп тілді құжаттама
│   └── README_*.md
├── i18n/                    # тәржімә файлдары
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # құрылған орындалатын файл
```

## Конфигурация файлы

`config.json` файлы EXE бірге бір каталогта сақталады және барлық бапталатын баптауларды қамтиды. Баптаулар өзгертілгенде автоматты түрде сақталады.

## Лицензия

MIT License

## Дағдыландырушы

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- Жоба URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Алғыс айтулар

- LibreHardwareMonitor - аппараттық қамтама мониторингі кітапханасы
- psutil - кросс-платформалық жүйе мониторингі
- PyInstaller - Python тапсыру құралы
