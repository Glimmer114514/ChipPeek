# ChipPeek

Un widget flottant léger de surveillance matérielle pour Windows. Surveillance en temps réel de la fréquence CPU/GPU, de la température, de la VRAM et de l'utilisation de la mémoire, toujours au premier plan y compris dans les applications plein écran.

> **Autres langues**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | **Français** | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Fonctionnalités

- **Surveillance en temps réel** : fréquence CPU, température CPU, fréquence GPU, température GPU, utilisation VRAM, utilisation mémoire
- **Double mode d'affichage** : widget de coin / barre supérieure, basculement en un clic
- **Affichage personnalisable** : choisissez librement les métriques à afficher, basculez entre pourcentage/valeurs réelles
- **Toujours au premier plan** : reste au-dessus de toutes les fenêtres, fonctionne dans les jeux plein écran
- **Redimensionnement automatique** : la largeur de la fenêtre s'ajuste automatiquement au contenu
- **Style ajustable** : opacité de la fenêtre, transparence de l'arrière-plan, taille de police - tout est ajustable
- **Support multilingue** : plus de 20 langues, détecte automatiquement la langue du système
- **Fonctionnement pratique** : glisser-clic gauche pour déplacer, menu clic droit pour paramètres rapides, accroche automatique aux bords de l'écran
- **Échantillonnage configurable** : 200ms - 3000ms ajustable
- **Démarrage automatique** : se lance automatiquement à la connexion Windows
- **Faible utilisation des ressources** : empreinte minimale en arrière-plan

## Démarrage rapide

### Utilisation directe

Téléchargez `ChipPeek.exe` et double-cliquez pour l'exécuter (demandera automatiquement les privilèges administrateur pour la température CPU et la lecture précise de la fréquence).

### Exécuter à partir du code source

```bash
# Cloner le dépôt
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Installer les dépendances
pip install -r requirements.txt

# Exécuter
python main.py
```

## Configuration requise

- Windows 10 / Windows 11
- Privilèges administrateur (recommandé), sinon la température CPU et la fréquence précise peuvent ne pas être disponibles
- .NET Framework 4.7.2 ou supérieur (requis par LibreHardwareMonitor)

## Compiler en EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Après compilation, le fichier EXE se trouve dans `dist/ChipPeek.exe`.

## Utilisation

### Opérations de base

| Action | Description |
|------|------|
| Glisser clic gauche | Déplacer la fenêtre |
| Clic droit | Ouvrir le menu (changer de mode / paramètres / quitter) |
| Accroche automatique | S'accroche automatiquement à 20px des bords de l'écran |

### Modes d'affichage

- **Widget de coin** : toutes les métriques disposées verticalement, peut être placé dans n'importe quel coin de l'écran
- **Barre supérieure** : toutes les métriques disposées horizontalement, centrée en haut de l'écran par défaut

### Paramètres

- **Mode d'affichage** : widget de coin / barre supérieure
- **Position du widget** : bas droite / bas gauche / haut droite / haut gauche
- **Opacité de la fenêtre** : 30% - 100% de transparence globale de la fenêtre
- **Transparence de l'arrière-plan** : 0% - 100% de fond transparent (le texte reste net)
- **Intervalle d'échantillonnage** : 200ms - 3000ms taux de rafraîchissement des données
- **Taille de police** : police de 8 - 20 points
- **Langue** : plus de 20 langues, détecte automatiquement la langue du système
- **Métriques d'affichage** : activez/désactivez chaque métrique indépendamment
- **Format d'affichage** : VRAM / Mémoire peuvent basculer entre pourcentage ou valeurs réelles
- **Démarrage automatique** : s'exécute automatiquement à la connexion Windows

## Stack technologique

- **GUI**：Tkinter
- **Données matérielles**：LibreHardwareMonitorLib (via pythonnet), psutil, pynvml (solution de secours pour GPU NVIDIA)
- **Intégration système**：pywin32 (fenêtre au premier plan, registre de démarrage automatique)
- **Empaquetage**：PyInstaller

## Structure du projet

```
ChipPeek/
├── main.py                  # Point d'entrée
├── monitor_window.py        # UI de la fenêtre et logique d'interaction
├── hardware_monitor.py      # Collecte de données matérielles
├── config.py                # Gestion de la configuration
├── i18n.py                  # Internationalisation
├── generate_icon.py         # Script de génération d'icônes
├── admin.manifest           # Manifeste de privilèges admin UAC
├── app.ico                  # Icône de l'application
├── app.png                  # Aperçu de l'icône
├── requirements.txt         # Dépendances Python
├── docs/                    # Documentation multilingue
│   └── README_*.md
├── i18n/                    # Fichiers de traduction
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Exécutable compilé
```

## Fichier de configuration

Le fichier `config.json` est enregistré dans le même répertoire que l'EXE et contient tous les paramètres ajustables. Les paramètres sont sauvegardés automatiquement lors de leur modification.

## Licence

MIT License

## Développeur

**R41NH4RD**

- GitHub : [@R41NH4RD](https://github.com/Glimmer114514)
- URL du projet: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Remerciements

- LibreHardwareMonitor - Bibliothèque de surveillance matérielle
- psutil - Surveillance système multiplateforme
- PyInstaller - Outil d'empaquetage Python
