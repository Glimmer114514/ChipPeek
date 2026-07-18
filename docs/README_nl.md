# ChipPeek

Een lichtgewicht zwevend hardware monitoring widget voor Windows. Realtime monitoring van CPU/GPU frequentie, temperatuur, VRAM en geheugengebruik, altijd op de voorgrond inclusief fullscreen apps.

> **Andere talen**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | **Nederlands** | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md)

## Functies

- **Realtime monitoring**: CPU frequentie, CPU temperatuur, GPU frequentie, GPU temperatuur, VRAM gebruik, geheugengebruik
- **Twee weergavemodi**: hoekwidget / bovenste balk, schakelen met één klik
- **Aanpasbare weergave**: kies vrij welke statistieken u wilt weergeven, schakel tussen procenten/werkelijke waarden
- **Altijd op de voorgrond**: blijft boven alle vensters, werkt in fullscreen games
- **Automatische grootte**: vensterbreedte past zich automatisch aan de inhoud aan
- **Aanpasbare stijl**: vensterdoorzichtigheid, achtergrondtransparantie, lettergrootte - allemaal aanpasbaar
- **Meertalige ondersteuning**: 20+ talen, detecteert automatisch de systeemtaal
- **Handige bediening**: sleep met linksklik om te verplaatsen, rechtsklikmenu voor snelle instellingen, automatisch vastklikken aan schermranden
- **Configureerbare bemonstering**: 200ms - 3000ms aanpasbaar
- **Automatisch opstarten**: start automatisch bij Windows aanmelding
- **Laag bronnen gebruik**: minimale voetafdruk op de achtergrond

## Snelle start

### Direct gebruik

Download `ChipPeek.exe` en dubbelklik om uit te voeren (vraagt automatisch adminrechten aan voor CPU temperatuur en nauwkeurige frequentie lezing).

### Uitvoeren vanuit broncode

```bash
# Kloon de repository
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Installeer afhankelijkheden
pip install -r requirements.txt

# Uitvoeren
python main.py
```

## Systeemvereisten

- Windows 10 / Windows 11
- Beheerdersrechten (aanbevolen), anders is CPU temperatuur en nauwkeurige frequentie mogelijk niet beschikbaar
- .NET Framework 4.7.2 of hoger (vereist door LibreHardwareMonitor)

## Bouwen als EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Na het bouwen bevindt het EXE-bestand zich op `dist/ChipPeek.exe`.

## Gebruik

### Basisbewerkingen

| Actie | Beschrijving |
|------|------|
| Linksklik slepen | Vensterpositie verplaatsen |
| Rechtsklik | Menu openen (modus wijzigen / instellingen / afsluiten |
| Automatisch vastklikken | Klikt automatisch vast binnen 20px van schermranden |

### Weergavemodi

- **Hoekwidget**: alle statistieken verticaal gerangschikt, kunnen in elke schermhoek worden geplaatst
- **Bovenste balk**: alle statistieken horizontaal gerangschikt, standaard gecentreerd bovenaan het scherm

### Instellingen

- **Weergavemodus**: hoekwidget / bovenste balk
- **Widgetpositie**: rechtsonder / linksonder / rechtsboven / linksboven
- **Vensterdoorzichtigheid**: 30% - 100% algehele venstertransparantie
- **Achtergrondtransparantie**: 0% - 100% achtergrond transparant (tekst blijft scherp)
- **Bemonsteringsinterval**: 200ms - 3000ms gegevensvernieuwingssnelheid
- **Lettergrootte**: 8 - 20 punts lettertype
- **Taal**: 20+ talen, detecteert automatisch de systeemtaal
- **Weergavestatistieken**: elke statistiek onafhankelijk in- en uitschakelen
- **Weergaveformaat**: VRAM / Geheugen kunnen schakelen tussen procenten of werkelijke waarden
- **Automatisch opstarten**: automatisch uitvoeren bij aanmelden bij Windows

## Technologie stapel

- **GUI**：Tkinter
- **Hardwaregegevens**：LibreHardwareMonitorLib (via pythonnet), psutil, pynvml (back-up voor NVIDIA GPU)
- **Systeemintegratie**：pywin32 (venster altijd op voorgrond, automatisch opstarten register)
- **Verpakken**：PyInstaller

## Projectstructuur

```
ChipPeek/
├── main.py                  # Ingangspunt
├── monitor_window.py        # Venster UI en interactielogica
├── hardware_monitor.py      # Hardware gegevensverzameling
├── config.py                # Configuratiebeheer
├── i18n.py                  # Internationalisering
├── generate_icon.py         # Pictogram generatiescript
├── admin.manifest           # UAC adminrechten manifest
├── app.ico                  # Toepassingspictogram
├── app.png                  # Pictogram voorbeeld
├── requirements.txt         # Python afhankelijkheden
├── docs/                    # Meertalige documentatie
│   └── README_*.md
├── i18n/                    # Vertaling bestanden
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Gecompileerd uitvoerbaar bestand
```

## Configuratiebestand

Het `config.json` bestand wordt opgeslagen in dezelfde map als de EXE, bevat alle aanpasbare instellingen. Instellingen worden automatisch opgeslagen wanneer ze worden gewijzigd.

## Licentie

MIT License

## Ontwikkelaar

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- Project URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Credits

- LibreHardwareMonitor - Hardware monitoring bibliotheek
- psutil - Cross-platform systeem monitoring
- PyInstaller - Python verpakkingstool
