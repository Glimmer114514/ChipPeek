# ChipPeek

Kevyt kelluva laitteiston valvontawidget Windowsille. Reaaliaikainen CPU/GPU-nopeuden, lämpötilan, VRAM:n ja muistin käytön valvonta, aina päällikköä myös kokoruututilassa.

> **Muut kielet**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | **Suomi** | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Ominaisuudet

- **Reaaliaikainen valvonta**: CPU-nopeus, CPU-lämpötila, GPU-nopeus, GPU-lämpötila, VRAM-käyttö, muistin käyttö
- **Kaksi näyttötilaa**: Nurkkawidget / Yläpalkki, yhdellä klikkauksella vaihto
- **Mukautettava näyttö**: Valitse vapaasti mitkä mittarit näytetään, vaihda prosentti-/todellisten arvojen välillä
- **Aina päällä**: Pysyy kaikkien ikkunoiden yläpuolella, toimii kokoruutupeleissä
- **Automaattinen koko**: Ikkunan leveys säätyy automaattisesti sisällön mukaan
- **Säädettävä tyyli**: Ikkunan läpinäkyvyys, taustan läpinäkyvyys, fontin koko - kaikki säädettävissä
- **Monikielinen tuki**: 20+ kieltä, tunnistaa automaattisesti järjestelmän kielen
- **Mukava käyttö**: Siirrä vetämällä vasemmalla näppäimellä, oikean painikkeen valikko nopeisiin asetuksiin, automaattinen snap ruudun reunoille
- **Määritettävissä oleva näytteenottotaajuus**: 200ms - 3000ms säädettävissä
- **Automaattinen käynnistys**: Käynnistyy automaattisesti Windows-kirjautumisessa
- **Alhainen resurssin käyttö**: Vähän muistia taustalla

## Pika-aloitus

### Suora käyttö

Lataa `ChipPeek.exe` ja kaksoisklikkaa suorittaaksesi (pyytää automaattisesti järjestelmänvalvojan oikeuksia CPU-lämpötilan ja tarkan nopeuden lukemiseksi).

### Suorita lähdekoodista

```bash
# Kloonaa arkisto
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Asenna riippuvuudet
pip install -r requirements.txt

# Suorita
python main.py
```

## Järjestelmävaatimukset

- Windows 10 / Windows 11
- Järjestelmänvalvojan oikeudet (suositeltu), muuten CPU-lämpötila ja tarkka nopeus eivät ehkä ole saatavilla
- .NET Framework 4.7.2 tai uudempi (vaaditaan LibreHardwareMonitor toimesta)

## Rakenna EXE:ksi

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Rakennuksen jälkeen EXE-tiedosto on sijainnissa `dist/ChipPeek.exe`.

## Käyttö

### Perustoiminnot

| Toiminto | Kuvaus |
|------|------|
| Vasemmalla vetäminen | Siirrä ikkunaa |
| Oikea painike | Avaa valikko (vaihda tilaa / asetukset / poistu) |
| Automaattinen snap | Liittyy automaattisesti 20px säteellä ruudun reunoista |

### Näyttötilat

- **Nurkkawidget**: Kaikki mittarit pystyssä, voidaan sijoittaa mihin tahansa ruudun nurkkaan
- **Yläpalkki**: Kaikki mittarit vaakasuunnassa, oletuksena keskitettynä ruudun yläreunaan

### Asetukset

- **Näyttötila**: Nurkkawidget / Yläpalkki
- **Widgetin sijainti**: Alhaalla oikealla / Alhaalla vasemmalla / Ylhäällä oikealla / Ylhäällä vasemmalla
- **Ikkunan läpinäkyvyys**: 30% - 100% koko ikkunan läpinäkyvyys
- **Taustan läpinäkyvyys**: 0% - 100% taustan läpinäkyvyys (teksti pysyy terävänä)
- **Näytteentottoväli**: 200ms - 3000ms datan päivitysnopeus
- **Fontin koko**: 8 - 20 pistettä
- **Kieli**: 20+ kieltä, tunnistaa automaattisesti järjestelmän kielen
- **Näyttömittarit**: Kytke kunkin mittarin päälle/pois itsenäisesti
- **Näyttömuoto**: VRAM / Muisti voidaan vaihtaa prosentiksi tai todellisiksi arvoiksi
- **Automaattinen käynnistys**: Suorita automaattisesti kirjautuessa Windowsiin

## Tekninen pino

- **GUI**：Tkinter
- **Laitteisto data**：LibreHardwareMonitorLib (pythonnet kautta), psutil, pynvml (NVIDIA GPU vara)
- **Järjestelmäintegraatio**：pywin32 (ikkuna aina päällä, automaattinen käynnistys rekisteri)
- **Paketointi**：PyInstaller

## Projektin rakenne

```
ChipPeek/
├── main.py                  # Ohjelman aloituspiste
├── monitor_window.py        # Ikkuna UI ja vuorovaikutuslogiikka
├── hardware_monitor.py      # Laitteisto datan keruu
├── config.py                # Asetusten hallinta
├── i18n.py                  # Kansainvälistyminen
├── generate_icon.py         # Kuvakkeen luontiskripti
├── admin.manifest           # UAC järjestelmänvalvojan oikeus manifesti
├── app.ico                  # Sovelluksen kuvake
├── app.png                  # Kuvakkeen esikatselu
├── requirements.txt         # Python riippuvuudet
├── docs/                    # Monikielinen dokumentaatio
│   └── README_*.md
├── i18n/                    # Käännöstiedostot
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Käännetty suoritettava tiedosto
```

## Asetustiedosto

`config.json` tiedosto tallennetaan samaan kansioon kuin EXE ja se sisältää kaikki säädettävät asetukset. Asetukset tallennetaan automaattisesti, kun niitä muutetaan.

## Lisenssi

MIT License

## Kehittäjä

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- Projektin URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Kiitokset

- LibreHardwareMonitor - Laitteiston valvontakirjasto
- psutil - Alustariippumaton järjestelmän valvonta
- PyInstaller - Python paketoinnin työkalu
