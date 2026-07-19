# ChipPeek

Un widget fluttuante leggero per il monitoraggio hardware su Windows. Monitoraggio in tempo reale di frequenza CPU/GPU, temperatura, VRAM e utilizzo della memoria, sempre in primo piano incluse le app a schermo intero.

> **Altre lingue**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | **Italiano** | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Funzionalità

- **Monitoraggio in tempo reale**: frequenza CPU, temperatura CPU, frequenza GPU, temperatura GPU, utilizzo VRAM, utilizzo memoria
- **Doppia modalità di visualizzazione**: widget angolare / barra superiore, passaggio con un clic
- **Visualizzazione personalizzabile**: scegli liberamente quali metriche mostrare, passa tra percentuali/valori effettivi
- **Sempre in primo piano**: rimane sopra tutte le finestre, funziona nei giochi a schermo intero
- **Dimensionamento automatico**: la larghezza della finestra si adatta automaticamente al contenuto
- **Stile regolabile**: opacità della finestra, trasparenza dello sfondo, dimensione del font - tutto regolabile
- **Supporto multilingue**: 20+ lingue, rileva automaticamente la lingua di sistema
- **Funzionamento conveniente**: trascina con clic sinistro per spostare, menu clic destro per impostazioni rapide, aggancio automatico ai bordi dello schermo
- **Campionamento configurabile**: 200ms - 3000ms regolabile
- **Avvio automatico**: si avvia automaticamente all'accesso a Windows
- **Basso utilizzo delle risorse**: ingombro minimo in background

## Avvio rapido

### Uso diretto

Scarica `ChipPeek.exe` e fai doppio clic per eseguirlo (richiederà automaticamente i privilegi di amministratore per la temperatura della CPU e la lettura accurata della frequenza).

### Esegui dal sorgente

```bash
# Clona il repository
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Installa le dipendenze
pip install -r requirements.txt

# Esegui
python main.py
```

## Requisiti di sistema

- Windows 10 / Windows 11
- Privilegi di amministratore (consigliati), altrimenti la temperatura della CPU e la frequenza accurata potrebbero non essere disponibili
- .NET Framework 4.7.2 o superiore (richiesto da LibreHardwareMonitor)

## Compila come EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Dopo la compilazione, il file EXE si trova in `dist/ChipPeek.exe`.

## Utilizzo

### Operazioni di base

| Azione | Descrizione |
|------|------|
| Trascina clic sinistro | Sposta la posizione della finestra |
| Clic destro | Apri menu (cambia modalità / impostazioni / esci) |
| Aggancio automatico | Si aggancia automaticamente entro 20px dai bordi dello schermo |

### Modalità di visualizzazione

- **Widget angolare**: tutte le metriche disposte verticalmente, possono essere posizionate in qualsiasi angolo dello schermo
- **Barra superiore**: tutte le metriche disposte orizzontalmente, per impostazione predefinita centrate nella parte superiore dello schermo

### Impostazioni

- **Modalità di visualizzazione**: widget angolare / barra superiore
- **Posizione widget**: in basso a destra / in basso a sinistra / in alto a destra / in alto a sinistra
- **Opacità finestra**: 30% - 100% trasparenza generale della finestra
- **Trasparenza sfondo**: 0% - 100% sfondo trasparente (il testo rimane nitido)
- **Intervallo di campionamento**: 200ms - 3000ms frequenza di aggiornamento dati
- **Dimensione font**: font da 8 a 20 punti
- **Lingua**: 20+ lingue, rileva automaticamente la lingua di sistema
- **Metriche di visualizzazione**: attiva/disattiva ogni metrica indipendentemente
- **Formato di visualizzazione**: VRAM / Memoria possono passare tra percentuali o valori effettivi
- **Avvio automatico**: esegui automaticamente all'accesso a Windows

## Stack tecnologico

- **GUI**：Tkinter
- **Dati hardware**：LibreHardwareMonitorLib (tramite pythonnet), psutil, pynvml (alternativa per GPU NVIDIA)
- **Integrazione sistema**：pywin32 (finestra sempre in primo piano, registro di avvio automatico)
- **Confezionamento**：PyInstaller

## Struttura del progetto

```
ChipPeek/
├── main.py                  # Punto di ingresso
├── monitor_window.py        # UI della finestra e logica di interazione
├── hardware_monitor.py      # Raccolta dati hardware
├── config.py                # Gestione configurazione
├── i18n.py                  # Internazionalizzazione
├── generate_icon.py         # Script di generazione icone
├── admin.manifest           # Manifesto privilegi admin UAC
├── app.ico                  # Icona dell'applicazione
├── app.png                  # Anteprima icona
├── requirements.txt         # Dipendenze Python
├── docs/                    # Documentazione multilingue
│   └── README_*.md
├── i18n/                    # File di traduzione
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Eseguibile compilato
```

## File di configurazione

Il file `config.json` viene salvato nella stessa directory dell'EXE e contiene tutte le impostazioni regolabili. Le impostazioni vengono salvate automaticamente quando vengono modificate.

## Licenza

MIT License

## Sviluppatore

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL del progetto: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Ringraziamenti

- LibreHardwareMonitor - Libreria di monitoraggio hardware
- psutil - Monitoraggio sistema multipiattaforma
- PyInstaller - Strumento di confezionamento Python
