# ChipPeek

Lahek plavajoči pripomoček za nadzor strojne opreme za Windows. Nadzor v realnem času frekvence CPU/GPU, temperature, VRAM in porabe pomnilnika, vedno na vrhu, vključno z aplikacijami v celozaslonskem načinu.

> **Drugi jeziki**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | **Slovenščina** | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Funkcije

- **Nadzor v realnem času**: frekvenca CPU, temperatura CPU, frekvenca GPU, temperatura GPU, poraba VRAM, poraba pomnilnika
- **Dva načina prikaza**: kotni pripomoček / vršna vrstica, preklop z enim klikom
- **Prilagodljiv prikaz**: prosto izberite, katere metrike želite prikazati, preklop med odstotki/dejanskimi vrednostmi
- **Vedno na vrhu**: ostaja nad vsemi okni, deluje tudi v igrah v celozaslonskem načinu
- **Samodejna velikost**: širina okna se samodejno prilagodi vsebini
- **Prilagodljiv slog**: prosojnost okna, prosojnost ozadja, velikost pisave - vse je prilagodljivo
- **Večjezična podpora**: 20+ jezikov, samodejno zazna jezik sistema
- **Priročno upravljanje**: premaknite s povlekom z levim gumbom, meni z desnim gumbom za hitre nastavitve, samodejno prileganje robovom zaslona
- **Prilagodljiva frekvenca vzorčenja**: 200ms - 3000ms prilagodljivo
- **Samodejni zagon**: zažene se samodejno ob prijavi v Windows
- **Nizka poraba virov**: minimalno breme v ozadju

## Hiter začetek

### Neposredna uporaba

Prenesite `ChipPeek.exe` in dvakrat kliknite za zagon (samodejno bo zahteval skrbniške dovoljenja za temperaturo CPU in točno branje frekvence).

### Zagon iz izvorne kode

```bash
# Klonirajte repozitorij
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Namestite odvisnosti
pip install -r requirements.txt

# Zaženite
python main.py
```

## Sistemski zahtevi

- Windows 10 / Windows 11
- Skrbniška dovoljenja (priporočljivo), sicer temperatura CPU in točna frekvenca morda ne bosta na voljo
- .NET Framework 4.7.2 ali novejša (zahteva LibreHardwareMonitor)

## Izgradnja kot EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Po izgradnji je EXE datoteka na lokaciji `dist/ChipPeek.exe`.

## Uporaba

### Osnovne operacije

| Operacija | Opis |
|------|------|
| Povlek z levim gumbom | Premik položaja okna |
| Desni gumb | Odpiranje menija (sprememba načina / nastavitve / izhod) |
| Samodejno prileganje | Samodejno se prileže znotraj 20px od robov zaslona |

### Načini prikaza

- **Kotni pripomoček**: vse metrike razporejene navpično, jih je možno postaviti v katerikoli kot zaslona
- **Vršna vrstica**: vse metrike razporejene vodoravno, privzeto sredinsko poravnane na vrhu zaslona

### Nastavitve

- **Način prikaza**: kotni pripomoček / vršna vrstica
- **Položaj pripomočka**: desno spodaj / levo spodaj / desno zgoraj / levo zgoraj
- **Prosojnost okna**: 30% - 100% skupna prosojnost okna
- **Prosojnost ozadja**: 0% - 100% prozorno ozadje (besedilo ostane ožje)
- **Interval vzorčenja**: 200ms - 3000ms frekvenca osveževanja podatkov
- **Velikost pisave**: 8 - 20 točk
- **Jezik**: 20+ jezikov, samodejno zazna jezik sistema
- **Metrike prikaza**: vsako metriko je mogoče neodvisno vklopiti/izklopiti
- **Oblika prikaza**: VRAM / Pomnilnik se lahko preklopijo med odstotki ali dejanskimi vrednostmi
- **Samodejni zagon**: samodejni zagon ob prijavi v Windows

## Tehnološki sklad

- **GUI**：Tkinter
- **Podatki o strojni opremi**：LibreHardwareMonitorLib (preko pythonnet), psutil, pynvml (nadomestni način za NVIDIA GPU)
- **Sistemska integracija**：pywin32 (okno vedno na vrhu, register za samodejni zagon)
- **Pakiranje**：PyInstaller

## Struktura projekta

```
ChipPeek/
├── main.py                  # Vhodna točka
├── monitor_window.py        # UI okna in logika interakcije
├── hardware_monitor.py      # Zbiranje podatkov o strojni opremi
├── config.py                # Upravljanje konfiguracije
├── i18n.py                  # Mednarodna podpora
├── generate_icon.py         # Skripta za generiranje ikon
├── admin.manifest           # Manifest skrbniških dovoljenj UAC
├── app.ico                  # Ikona aplikacije
├── app.png                  # Predogled ikone
├── requirements.txt         # Python odvisnosti
├── docs/                    # Večjezična dokumentacija
│   └── README_*.md
├── i18n/                    # Prevodne datoteke
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Prevedena izvršljiva datoteka
```

## Konfiguracijska datoteka

Datoteka `config.json` se shrani v istem imeniku kot EXE in vsebuje vse prilagodljive nastavitve. Nastavitve se samodejno shranijo ob spremembi.

## Licenca

MIT License

## Razvijalec

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL projekta: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Zahvale

- LibreHardwareMonitor - Knjižnica za nadzor strojne opreme
- psutil - Večplatformski nadzor sistema
- PyInstaller - Orodje za pakiranje Pythona
