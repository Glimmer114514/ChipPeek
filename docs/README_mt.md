# ChipPeek

Widget liġġi ħafifa ta' monitoring tal-hardware ta' Windows. Monitoring f'ħin reali tal-frekwenza tal-CPU/GPU, temperatura, VRAM, u l-użu tal-memorja, dejjem fuq kollox inklużi applikazzjonijiet fullscreen.

> **Lingwi Oħra**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | **Malti** | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Karatatteristiċi

- **Monitoring f'ħin reali**: Frekwenza tal-CPU, temperatura tal-CPU, frekwenza tal-GPU, temperatura tal-GPU, użu tal-VRAM, użu tal-memorja
- **Żewġ modi ta' wiri**: Widget tar-rokna / Barra tat-tieqa, bidla b'klikka waħda
- **Wiri li jista' jiġi ppersonalizzat**: Agħżel liberament liema metriki turi, ibdel bejn persentwal/valuri attwali
- **Dejjem fuq kollox**: Jibqa' fuq l-istess ħin ma' l-pjanċieri kollha, jaħdem f'logħob fullscreen
- **Daqs awtomatiku**: L-wiesa' tat-tieqa taġġa awtomatikament biex tqabbad ma' l-kontenut
- **Stil li jista' jiġi aġġustat**: Opacità tat-tieqa, trasparenza tal-background, daqs tal-font kollha jistgħu jiġu aġġustati
- **Appoġġ b'ħafna lingwi**: 20+ lingwi, jiskopri awtomatikament il-lingwa tas-sistema
- **Operazzjoni konvenjenti**: Iġbid ix-xellug biex timxi, ikklikkja dritt menu għal settings mgħaġġla, awto-mqabbd mal-ġnub tal-iskrin
- **Kampjun li jista' jiġi aġġustat**: 200ms - 3000ms li jista' jiġi aġġustat
- **Awto-bidu**: Nedi awtomatikament meta tidħol f'Windows
- **Użu baxx tar-riżorsi**: Tlietx baxx fl-isfond

## Bidu Mgħaġġel

### Użu Dirett

Niżżel `ChipPeek.exe` u ikklikkja darbtejn biex tmexxi (se jitlob awtomatikament privileġġi ta' amministratur għat-temperatura tal-CPU u qari preċiż tal-frekwenza).

### Mexxi mis-Sors

```bash
# Ikkjona r-repository
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Installa d-dipendenzi
pip install -r requirements.txt

# Mexxi
python main.py
```

## Rekwiżiti tas-Sistema

- Windows 10 / Windows 11
- Privileġġi ta' amministratur (rakkomandati), inkella t-temperatura tal-CPU u l-frekwenza preċiża jistgħu ma jkunux disponibbli
- .NET Framework 4.7.2 jew ogħla (meħtieġ minn LibreHardwareMonitor)

## Ibni bħala EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Wara l-bini, il-fajl EXE jinsab f'`dist/ChipPeek.exe`.

## Użu

### Operazzjonijiet Bażiċi

| Azzjoni | Deskrizzjoni |
|------|------|
| Iġbid ix-xellug | Imxi l-pożizzjoni tat-tieqa |
| Ikklikkja dritt | Iftaħ il-menu (ibdel il-modalità / settings / ħruġ) |
| Auto snap | Awtomatikament jinżammu f'ħin 20px mill-ġnub tal-iskrin |

### Modi ta' Wiri

- **Widget tar-Rokna**: Il-metriki kollha imranġati vertikalment, jistgħu jitqiegħdu f'kull rokna tal-iskrin
- **Barra tat-Top**: Il-metriki kollha imranġati orizzontalment, ċċentrati fil-parti ta' fuq tal-iskrin bħala default

### Settings

- **Modalità ta' wiri**: Widget tar-rokna / Barra tat-tieqa
- **Pożizzjoni tal-widget**: Bidwi tal-lemin / Bidwi tax-xellug / Fuq tal-lemin / Fuq tax-xellug
- **Opacità tat-tieqa**: 30% - 100% trasparenza totali tat-tieqa
- **Trasparenza tal-background**: 0% - 100% background trasparenti (it-test jibqa' ċar)
- **Intervall tal-kampjunar**: 200ms - 3000ms rata ta' rifreż tar-data
- **Daqs tal-font**: 8 - 20 punt font
- **Lingwa**: 20+ lingwi, jiskopri awtomatikament il-lingwa tas-sistema
- **Metriki tas-sam**: Ibdel kull metru indipendentement
- **Format ta' wiri**: VRAM / Memorja jistgħu jibdlu bejn persentwal jew valuri attwali
- **Awto-bidu**: Mexxi awtomatikament meta tidħol f'Windows

## Teknoloġija

- **GUI**：Tkinter
- **Data tal-hardware**：LibreHardwareMonitorLib (per mezz ta' pythonnet), psutil, pynvml (NVIDIA GPU fallback)
- **Integrazzjoni tas-sistema**：pywin32 (tieqa fuq kollox, awto-bidu reġistru)
- **Ippakkjar**：PyInstaller

## Struttura tal-Proġett

```
ChipPeek/
├── main.py                  # Punt ta' daħla
├── monitor_window.py        # UI tat-tieqa u loġika ta' interazzjoni
├── hardware_monitor.py      # Ġbir ta' data tal-hardware
├── config.py                # Ġestjoni tal-konfigurazzjoni
├── i18n.py                  # Internazzjonalizzazzjoni
├── generate_icon.py         # Script ta' ġenerazzjoni tal-ikona
├── admin.manifest           # Manifest tal-privileġġ ta' amministratur UAC
├── app.ico                  # Ikona tal-applikazzjoni
├── app.png                  # Prevedi tal-ikona
├── requirements.txt         # Dipendenzi ta' Python
├── docs/                    # Dokumenti b'ħafna lingwi
│   └── README_*.md
├── i18n/                    # Fajls ta' traduzzjoni
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Esegwibbli kompilati
```

## Fajl tal-Konfigurazzjoni

Il-fajl `config.json` jinħażen fl-istess direttorju bħall-EXE, u fih l-settings kollha li jistgħu jiġu aġġustati. L-settings jinħażnu awtomatikament meta jiġu mibdula.

## Liċenzja

MIT License

## Żviluppatur

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL tal-Proġett: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Rikonnašċimenti

- LibreHardwareMonitor - Librerija ta' monitoring tal-hardware
- psutil - Monitoring tas-sistema cross-platform
- PyInstaller - Għodda ta' pakkjar ta' Python
