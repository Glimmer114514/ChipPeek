# ChipPeek

Un widget flotant lleuger de monitoratge de maquinari per a Windows. Monitoratge en temps real de la freqüència CPU/GPU, temperatura, VRAM i ús de memòria, sempre a la part superior, incloses les aplicacions a pantalla completa.

> **Altres idiomes**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | **Català** | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Característiques

- **Monitoratge en temps real**: freqüència CPU, temperatura CPU, freqüència GPU, temperatura GPU, ús VRAM, ús de memòria
- **Dos modes de visualització**: widget de cantonada / barra superior, canvi amb un sol clic
- **Visualització personalitzable**: trieu lliurement quines mètriques mostrar, canvi entre percentatge/valors reals
- **Sempre a la part superior**: roman per sobre de totes les finestres, funciona en jocs a pantalla completa
- **Mida automàtica**: l'ample de la finestra s'ajusta automàticament al contingut
- **Estil ajustable**: opacitat de la finestra, transparència del fons, mida de la font - tot ajustable
- **Suport multilingüe**: 20+ idiomes, detecta automàticament l'idioma del sistema
- **Operació convenient**: arrossega amb clic esquerre per moure, menú de clic dret per a configuracions ràpides, ajust automàtic als marges de la pantalla
- **Freqüència de mostreig configurable**: 200ms - 3000ms ajustable
- **Inici automàtic**: s'inicia automàticament en iniciar sessió a Windows
- **Ús baix de recursos**: empremta mínima en segon pla

## Inici ràpid

### Ús directe

Descarregueu `ChipPeek.exe` i feu doble clic per executar-lo (demanarà automàticament privilegis d'administrador per a la temperatura CPU i la lectura precisa de la freqüència).

### Executar des del codi font

```bash
# Clona el repositori
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Instal·la les dependències
pip install -r requirements.txt

# Executa
python main.py
```

## Requisits del sistema

- Windows 10 / Windows 11
- Privilegis d'administrador (recomanat), sinó la temperatura CPU i la freqüència precisa podrien no estar disponibles
- .NET Framework 4.7.2 o superior (requerit per LibreHardwareMonitor)

## Compilar com EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Després de compilar, l'arxiu EXE es troba a `dist/ChipPeek.exe`.

## Ús

### Operacions bàsiques

| Operació | Descripció |
|------|------|
| Arrossegar amb clic esquerre | Moure la posició de la finestra |
| Clic dret | Obrir menú (canviar mode / configuració / sortir) |
| Ajust automàtic | S'ajusta automàticament dins de 20px dels marges de la pantalla |

### Modes de visualització

- **Widget de cantonada**: totes les mètriques disposades verticalment, es poden col·locar a qualsevol cantonada de la pantalla
- **Barra superior**: totes les mètriques disposades horitzontalment, per defecte centrades a la part superior de la pantalla

### Configuració

- **Mode de visualització**: widget de cantonada / barra superior
- **Posició del widget**: baix a la dreta / baix a l'esquerra / dalt a la dreta / dalt a l'esquerra
- **Opacitat de la finestra**: 30% - 100% de transparència total de la finestra
- **Transparència del fons**: 0% - 100% de fons transparent (el text es manté nítid)
- **Interval de mostreig**: 200ms - 3000ms de taxa d'actualització de dades
- **Mida de la font**: 8 - 20 punts
- **Idioma**: 20+ idiomes, detecta automàticament l'idioma del sistema
- **Mètriques de visualització**: activeu/desactiveu cada mètrica independentment
- **Format de visualització**: VRAM / Memòria poden canviar entre percentatge o valors reals
- **Inici automàtic**: executar automàticament en iniciar sessió a Windows

## Pila tecnològica

- **GUI**：Tkinter
- **Dades de maquinari**：LibreHardwareMonitorLib (mitjançant pythonnet), psutil, pynvml (alternativa per a GPU NVIDIA)
- **Integració del sistema**：pywin32 (finestra sempre a la part superior, registre d'inici automàtic)
- **Empaquetat**：PyInstaller

## Estructura del projecte

```
ChipPeek/
├── main.py                  # Punt d'entrada
├── monitor_window.py        # UI de la finestra i lògica d'interacció
├── hardware_monitor.py      # Recopilació de dades de maquinari
├── config.py                # Gestió de la configuració
├── i18n.py                  # Internacionalització
├── generate_icon.py         # Script de generació d'icones
├── admin.manifest           # Manifest de privilegis d'administrador UAC
├── app.ico                  # Icona de l'aplicació
├── app.png                  # Vista prèvia de la icona
├── requirements.txt         # Dependències de Python
├── docs/                    # Documentació multilingüe
│   └── README_*.md
├── i18n/                    # Fitxers de traducció
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Fitxer executable compilat
```

## Fitxer de configuració

El fitxer `config.json` es desa al mateix directori que l'EXE i conté totes les configuracions ajustables. Les configuracions es desen automàticament en modificar-les.

## Llicència

MIT License

## Desenvolupador

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL del projecte: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Crèdits

- LibreHardwareMonitor - Biblioteca de monitoratge de maquinari
- psutil - Monitoratge del sistema multiplataforma
- PyInstaller - Eina d'empaquetat de Python
