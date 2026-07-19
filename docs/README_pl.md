# ChipPeek

Lekki widget monitorowania sprzętu dla Windows. Monitorowanie w czasie rzeczywistym częstotliwości CPU/GPU, temperatury, VRAM i zużycia pamięci, zawsze na wierzchu włącznie z aplikacjami pełnoekranowymi.

> **Inne języki**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | **Polski** | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Funkcje

- **Monitorowanie w czasie rzeczywistym**: częstotliwość CPU, temperatura CPU, częstotliwość GPU, temperatura GPU, zużycie VRAM, zużycie pamięci
- **Dwa tryby wyświetlania**: widget narożny / górny pasek, przełączanie jednym kliknięciem
- **Konfigurowalne wyświetlanie**: swobodnie wybierz które metryki pokazać, przełączaj między procentami/wartościami rzeczywistymi
- **Zawsze na wierzchu**: pozostaje nad wszystkimi oknami, działa w grach pełnoekranowych
- **Automatyczny rozmiar**: szerokość okna automatycznie dostosowuje się do zawartości
- **Regulowalny styl**: przezroczystość okna, przezroczystość tła, rozmiar czcionki - wszystko regulowalne
- **Wielojęzyczna obsługa**: 20+ języków, automatyczne wykrywanie języka systemowego
- **Wygodne obsługiwanie**: przeciągnij lewym przyciskiem aby przenieść, menu prawoklikowe do szybkich ustawień, automatyczne przyczepianie do krawędzi ekranu
- **Konfigurowalne próbkowanie**: 200ms - 3000ms regulowalne
- **Automatyczne uruchamianie**: uruchamia się automatycznie po zalogowaniu do Windows
- **Niskie zużycie zasobów**: minimalny ślad w tle

## Szybki start

### Bezpośrednie użycie

Pobierz `ChipPeek.exe` i kliknij dwukrotnie aby uruchomić (automatycznie poprosi o uprawnienia administratora dla temperatury CPU i dokładnego odczytu częstotliwości).

### Uruchom z kodu źródłowego

```bash
# Sklonuj repozytorium
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Zainstaluj zależności
pip install -r requirements.txt

# Uruchom
python main.py
```

## Wymagania systemowe

- Windows 10 / Windows 11
- Uprawnienia administratora (zalecane), w przeciwnym razie temperatura CPU i dokładna częstotliwość mogą być niedostępne
- .NET Framework 4.7.2 lub wyższy (wymagany przez LibreHardwareMonitor)

## Kompilacja jako EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Po kompilacji plik EXE znajduje się w `dist/ChipPeek.exe`.

## Użycie

### Podstawowe operacje

| Akcja | Opis |
|------|------|
| Przeciąganie lewym przyciskiem | Przenieś pozycję okna |
| Prawy przycisk | Otwórz menu (zmień tryb / ustawienia / wyjdź) |
| Automatyczne przyczepianie | Automatycznie przyczepia się w obrębie 20px od krawędzi ekranu |

### Tryby wyświetlania

- **Widget narożny**: wszystkie metryki ułożone pionowo, można umieścić w dowolnym rogu ekranu
- **Górny pasek**: wszystkie metryki ułożone poziomo, domyślnie wyśrodkowane na górze ekranu

### Ustawienia

- **Tryb wyświetlania**: widget narożny / górny pasek
- **Pozycja widgetu**: prawy dół / lewy dół / prawy górny / lewy górny
- **Przezroczystość okna**: 30% - 100% ogólna przezroczystość okna
- **Przezroczystość tła**: 0% - 100% przezroczyste tło (tekst pozostaje ostry)
- **Interwał próbkowania**: 200ms - 3000ms częstotliwość odświeżania danych
- **Rozmiar czcionki**: czcionka 8 - 20 punktów
- **Język**: 20+ języków, automatyczne wykrywanie języka systemowego
- **Metryki wyświetlania**: włącz/wyłącz każdą metrykę niezależnie
- **Format wyświetlania**: VRAM / Pamięć mogą przełączać się między procentami lub wartościami rzeczywistymi
- **Automatyczne uruchamianie**: uruchom automatycznie po zalogowaniu do Windows

## Stos technologiczny

- **GUI**：Tkinter
- **Dane sprzętowe**：LibreHardwareMonitorLib (przez pythonnet), psutil, pynvml (rozwiązanie zapasowe dla GPU NVIDIA)
- **Integracja systemowa**：pywin32 (okno zawsze na wierzchu, rejestr automatycznego uruchamiania)
- **Pakowanie**：PyInstaller

## Struktura projektu

```
ChipPeek/
├── main.py                  # Punkt wejścia
├── monitor_window.py        # UI okna i logika interakcji
├── hardware_monitor.py      # Zbieranie danych sprzętowych
├── config.py                # Zarządzanie konfiguracją
├── i18n.py                  # Internacjonalizacja
├── generate_icon.py         # Skrypt generowania ikon
├── admin.manifest           # Manifest uprawnień administratora UAC
├── app.ico                  # Ikona aplikacji
├── app.png                  # Podgląd ikony
├── requirements.txt         # Zależności Python
├── docs/                    # Wielojęzyczna dokumentacja
│   └── README_*.md
├── i18n/                    # Pliki tłumaczeń
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Skompilowany plik wykonywalny
```

## Plik konfiguracyjny

Plik `config.json` jest zapisywany w tym samym katalogu co EXE, zawiera wszystkie regulowalne ustawienia. Ustawienia są automatycznie zapisywane po modyfikacji.

## Licencja

MIT License

## Programista

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL projektu: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Podziękowania

- LibreHardwareMonitor - Biblioteka monitorowania sprzętu
- psutil - Wieloplatformowe monitorowanie systemu
- PyInstaller - Narzędzie do pakowania Python
