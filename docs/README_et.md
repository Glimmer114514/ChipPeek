# ChipPeek

Kerge liikuv riistvara monitooringu vidin Windowsile. Reaalses ajas CPU/GPU sageduse, temperatuuri, VRAM-i ja mälukasutuse monitooring, alati ekraani ees, sealhulgas täisekraani rakendustes.

> **Teised keeled**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | **Eesti** | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Funktsioonid

- **Reaegne monitooring**: CPU sagedus, CPU temperatuur, GPU sagedus, GPU temperatuur, VRAM kasutuse, mälukasutuse
- **Kuvamise režiimid**: nurgavidin / ülemine riba, ühe klõpsuga vahetamine
- **Kohandatav kuvamine**: valge vabalt, milliseid mõõtmeid kuvada, protsentide/tegelike väärtuste vahel vahetamine
- **Alati ees**: jääb kõige aknade ümber, töötab ka täisekraani mängudes
- **Automaatne suurus**: akna laius kohandub automaatselt sisu järgi
- **Reguleeritav stiil**: akna läbipaistmatus, taust läbipaistvus, fondi suurus - kõik saab reguleerida
- **Keeltoe**: 20+ keelt, tuvastab automaatselt süsteemi keelt
- **Mugav kasutamine**: vasaku nupuga vedades liigutamine, parema nupuga menüü kiiremate seadistuste jaoks, automaatne kinnitumine ekraani servadele
- **Seadistatav proovivõtu sagedus**: 200ms - 3000ms reguleeritav
- **Automaatne käivitamine**: käivitatakse automaatselt Windowsi sisselogimisel
- **Vähene ressursside tarbimine**: minimaalne taustal töötamise mälujalg

## Kiire algus

### Otsene kasutamine

Laadi alla `ChipPeek.exe` ja topeltselge seda käivitada (taotleb automaatselt administraatori õigusi CPU temperatuuri ja täpse sageduse lugemiseks).

### Käivita lähtekoodist

```bash
# Klooni hoidla
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Paigalda sõltuvused
pip install -r requirements.txt

# Käivita
python main.py
```

## Süsteeminõuded

- Windows 10 / Windows 11
- Administraatori õigused (soovitatavad), muidu CPU temperatuur ja täpne sagedus ei pruugi olla kättesaadavad
- .NET Framework 4.7.2 või uuem (vajalik LibreHardwareMonitor jaoks)

## Ehita EXE-ks

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Peale ehitamist asub EXE fail asukohas `dist/ChipPeek.exe`.

## Kasutamine

### Põhioperatsioonid

| Tegevus | Kirjeldus |
|------|------|
| Vasakuga vedamine | Akna asukoha muutmine |
| Parem klõps | Menüü avamine (režiimi vahetamine / seaded / väljumine) |
| Automaatne kinnitumine | Kinnitub automaatselt 20px kauguselt ekraani servadest |

### Kuvamise režiimid

- **Nurgavidin**: kõik mõõtmed järjestatud vertikaalselt, saab paigutada ükskõik millisesse ekraani nurka
- **Ülemine riba**: kõik mõõtmed järjestatud horisontaalselt, vaikimisi tsentreeritud ekraani ülaosasse

### Seaded

- **Kuvamise režiim**: nurgavidin / ülemine riba
- **Vidina asukoht**: paremal all / vasakul all / paremal ülal / vasakul ülal
- **Akna läbipaistmatus**: 30% - 100% kogu akna läbipaistvus
- **Tausta läbipaistvus**: 0% - 100% läbipaistev taust (tekst jääb selgeks)
- **Proovivõtu intervall**: 200ms - 3000ms andmete värskendussagedus
- **Fondi suurus**: 8 - 20 punkti
- **Keel**: 20+ keelt, tuvastab automaatselt süsteemi keelt
- **Kuvatavad mõõtmed**: iga mõõtme saab eraldi sisse/välja lülitada
- **Kuvamise vorming**: VRAM / Mälu saab vahetada protsentide või tegelike väärtuste vahel
- **Automaatne käivitamine**: käivita automaatselt Windowsi sisselogimisel

## Tehnoloogiapinu

- **GUI**：Tkinter
- **Riistvara andmed**：LibreHardwareMonitorLib (pythonnet kaudu), psutil, pynvml (NVIDIA GPU varuversioon)
- **Süsteemiintegraatsioon**：pywin32 (aken alati ees, automaatse käivituse register)
- **Pakkimine**：PyInstaller

## Projekti struktuur

```
ChipPeek/
├── main.py                  # Sisenemispunkt
├── monitor_window.py        # Akna UI ja interaktsiooniloogika
├── hardware_monitor.py      # Riistvara andmete kogumine
├── config.py                # Seadistuste haldamine
├── i18n.py                  # Rahvusvahelistamine
├── generate_icon.py         # Ikoonide genereerimise skript
├── admin.manifest           # UAC administraatori õiguste manifest
├── app.ico                  # Rakenduse ikoon
├── app.png                  # Ikoni eelvaade
├── requirements.txt         # Python sõltuvused
├── docs/                    # Keelne dokumentatsioon
│   └── README_*.md
├── i18n/                    # Tõlkefailid
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Kompilleeritud käivitatav fail
```

## Seadistusfail

Fail `config.json` salvestatakse samasse kataloogi nagu EXE ja sisaldab kõiki seadistatavaid seadeid. Seaded salvestatakse automaatselt muutmisel.

## Litsents

MIT License

## Arendaja

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- Projekti URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Tänud

- LibreHardwareMonitor - Riistvara monitooringu teek
- psutil - Platvormidevaheline süsteemi monitooring
- PyInstaller - Pythoni pakkimise tööriist
