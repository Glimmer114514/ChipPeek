# ChipPeek

Ein leichtes schwebendes Hardware-Überwachungs-Widget für Windows. Echtzeit-Überwachung von CPU/GPU-Frequenz, Temperatur, VRAM und Speichernutzung, immer im Vordergrund auch bei Vollbildanwendungen.

> **Andere Sprachen**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | **Deutsch** | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Funktionen

- **Echtzeit-Überwachung**: CPU-Frequenz, CPU-Temperatur, GPU-Frequenz, GPU-Temperatur, VRAM-Nutzung, Speichernutzung
- **Zwei Anzeigemodi**: Eck-Widget / obere Leiste, Umschaltung mit einem Klick
- **Anpassbare Anzeige**: Wählen Sie frei, welche Metriken angezeigt werden sollen, wechseln Sie zwischen Prozentwerten/tatsächlichen Werten
- **Immer im Vordergrund**: Bleibt über allen Fenstern, funktioniert auch in Vollbildspielen
- **Automatische Größenanpassung**: Die Fensterbreite passt sich automatisch dem Inhalt an
- **Anpassbarer Stil**: Fensteroberfläche, Hintergrundtransparenz, Schriftgröße - alles einstellbar
- **Mehrsprachige Unterstützung**: Über 20 Sprachen, erkennt automatisch die Systemsprache
- **Praktische Bedienung**: Linksklick-Ziehen zum Verschieben, Rechtsklick-Menü für Schnelleinstellungen, automatisches Einrasten an Bildschirmkanten
- **Konfigurierbare Abtastung**: 200ms - 3000ms einstellbar
- **Automatischer Start**: Startet automatisch bei der Windows-Anmeldung
- **Niedriger Ressourcenverbrauch**: Minimaler Fußabdruck im Hintergrund

## Schnellstart

### Direkte Verwendung

Laden Sie `ChipPeek.exe` herunter und doppelklicken Sie zum Ausführen (fordert automatisch Administratorrechte für CPU-Temperatur und genaue Frequenzablesung an).

### Aus Quellcode ausführen

```bash
# Repository klonen
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Abhängigkeiten installieren
pip install -r requirements.txt

# Ausführen
python main.py
```

## Systemanforderungen

- Windows 10 / Windows 11
- Administratorrechte (empfohlen), sonst sind CPU-Temperatur und genaue Frequenz möglicherweise nicht verfügbar
- .NET Framework 4.7.2 oder höher (erforderlich für LibreHardwareMonitor)

## Als EXE kompilieren

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Nach der Kompilierung befindet sich die EXE-Datei unter `dist/ChipPeek.exe`.

## Verwendung

### Grundlegende Operationen

| Aktion | Beschreibung |
|------|------|
| Linksklick ziehen | Fensterposition verschieben |
| Rechtsklick | Menü öffnen (Modus wechseln / Einstellungen / Beenden) |
| Automatisches Einrasten | Rastet automatisch innerhalb von 20px an den Bildschirmkanten ein |

### Anzeigemodi

- **Eck-Widget**: Alle Metriken vertikal angeordnet, können in jeder Bildschirmecke platziert werden
- **Obere Leiste**: Alle Metriken horizontal angeordnet, standardmäßig oben zentriert auf dem Bildschirm

### Einstellungen

- **Anzeigemodus**: Eck-Widget / obere Leiste
- **Widget-Position**: Unten rechts / unten links / oben rechts / oben links
- **Fenstertransparenz**: 30% - 100% allgemeine Fenstetransparenz
- **Hintergrundtransparenz**: 0% - 100% Hintergrund transparent (Text bleibt scharf)
- **Abtastintervall**: 200ms - 3000ms Datenaktualisierungsrate
- **Schriftgröße**: 8 - 20 Punkt Schrift
- **Sprache**: Über 20 Sprachen, erkennt automatisch die Systemsprache
- **Anzeigemetriken**: Jede Metrik kann unabhängig ein- und ausgeschaltet werden
- **Anzeigeformat**: VRAM / Speicher kann zwischen Prozentwerten oder tatsächlichen Werten wechseln
- **Automatischer Start**: Wird automatisch bei der Windows-Anmeldung ausgeführt

## Technologie-Stack

- **GUI**：Tkinter
- **Hardwaredaten**：LibreHardwareMonitorLib (via pythonnet), psutil, pynvml (NVIDIA GPU Fallback)
- **Systemintegration**：pywin32 (Fenster immer im Vordergrund, Autostart-Registry)
- **Verpackung**：PyInstaller

## Projektstruktur

```
ChipPeek/
├── main.py                  # Einstiegspunkt
├── monitor_window.py        # Fenster-UI und Interaktionslogik
├── hardware_monitor.py      # Hardwaredatenerfassung
├── config.py                # Konfigurationsverwaltung
├── i18n.py                  # Internationalisierung
├── generate_icon.py         # Skript zur Symbolgenerierung
├── admin.manifest           # UAC-Administratorrechte-Manifest
├── app.ico                  # Anwendungssymbol
├── app.png                  # Symbolvorschau
├── requirements.txt         # Python-Abhängigkeiten
├── docs/                    # Mehrsprachige Dokumentation
│   └── README_*.md
├── i18n/                    # Übersetzungsdateien
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Kompilierte ausführbare Datei
```

## Konfigurationsdatei

Die Datei `config.json` wird im selben Verzeichnis wie die EXE gespeichert und enthält alle einstellbaren Einstellungen. Einstellungen werden automatisch gespeichert, wenn sie geändert werden.

## Lizenz

MIT License

## Entwickler

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- Projekt-URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Danksagungen

- LibreHardwareMonitor - Hardware-Überwachungsbibliothek
- psutil - Plattformübergreifende Systemüberwachung
- PyInstaller - Python-Verpackungstool
