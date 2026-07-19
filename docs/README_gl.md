# ChipPeek

Un widget flotante lixeiro de monitorización hardware para Windows. Monitoreo en tempo real da frecuencia CPU/GPU, temperatura, VRAM e uso de memoria, sempre en primeiro plano incluíndo aplicacións de pantalla completa.

> **Outros Idiomas**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | **Galego** | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Características

- **Monitorización en tempo real**: Frecuencia CPU, temperatura CPU, frecuencia GPU, temperatura GPU, uso de VRAM, uso de memoria
- **Dous modos de visualización**: Widget de esquina / Barra superior, cambio cun só clic
- **Visualización personalizable**: Escolla libremente que métricas mostrar, alternar entre porcentaxe/valores reais
- **Sempre en primeiro plano**: Mantense por riba de todas as xanelas, funciona en xogos de pantalla completa
- **Tamaño automático**: A largura da xanela axústase automaticamente para axustarse ao contido
- **Estilo axustable**: A opacidade da xanela, a transparencia do fondo e o tamaño da fonte son axustables
- **Soporte multi-idioma**: 20+ idiomas, detecta automaticamente o idioma do sistema
- **Operación cómoda**: Arrastrar coa esquerda para mover, menú de clic dereito para axustes rápidas, axuste automático aos bordos da pantalla
- **Amostraxo configurábel**: 200ms - 3000ms axustable
- **Inicio automático**: Iniciar automaticamente ao iniciar sesión en Windows
- **Baixo consumo de recursos**: Pegada mínima en segundo plano

## Inicio Rápido

### Uso Directo

Descargue `ChipPeek.exe` e faga dobre clic para executalo (solicitará privilexios de administrador automaticamente para a temperatura da CPU e a lectura precisa da frecuencia).

### Executar desde a Fonte

```bash
# Clonar o repositorio
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Instalar dependencias
pip install -r requirements.txt

# Executar
python main.py
```

## Requisitos do Sistema

- Windows 10 / Windows 11
- Privilexios de administrador (recomendado), senón a temperatura da CPU e a frecuencia precisa poden non estar dispoñibles
- .NET Framework 4.7.2 ou superior (requirido por LibreHardwareMonitor)

## Construír coma EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Despois de construír, o ficheiro EXE está en `dist/ChipPeek.exe`.

## Uso

### Operacións Básicas

| Acción | Descripción |
|------|------|
| Arrastrar esquerda | Mover a posición da xanela |
| Clic dereito | Abrir menú (cambiar modo / configuración / saír) |
| Axuste automático | Axústase automaticamente a menos de 20px dos bordos da pantalla |

### Modos de Visualización

- **Widget de Esquina**: Todas as métricas dispostas verticalmente, pódese colocar en calquera esquina da pantalla
- **Barra Superior**: Todas as métricas dispostas horizontalmente, centradas na parte superior da pantalla por defecto

### Configuración

- **Modo de visualización**: Widget de esquina / Barra superior
- **Posición do widget**: Inferior dereito / Inferior esquerdo / Superior dereito / Superior esquerdo
- **Opacidade da xanela**: 30% - 100% de opacidade xeral da xanela
- **Transparencia do fondo**: 0% - 100% de fondo transparente (o texto mantense nítido)
- **Intervalo de amostraxo**: 200ms - 3000ms de taxa de actualización de datos
- **Tamaño da fonte**: 8 - 20 puntos de tamaño de fonte
- **Idioma**: 20+ idiomas, detecta automaticamente o idioma do sistema
- **Métricas de visualización**: Alternar cada métrica de forma independente
- **Formato de visualización**: VRAM / Memoria pode alternar entre porcentaxe ou valores reais
- **Inicio automático**: Executarse automaticamente ao iniciar sesión en Windows

## Tech Stack

- **GUI**：Tkinter
- **Datos hardware**：LibreHardwareMonitorLib (vía pythonnet), psutil, pynvml (alternativa GPU NVIDIA)
- **Integración do sistema**：pywin32 (xanela en primeiro plano, rexistro de inicio automático)
- **Empaquetado**：PyInstaller

## Estrutura do Proxecto

```
ChipPeek/
├── main.py                  # Punto de entrada
├── monitor_window.py        # UI da xanela e lóxica de interacción
├── hardware_monitor.py      # Recolla de datos hardware
├── config.py                # Xestión da configuración
├── i18n.py                  # Internacionalización
├── generate_icon.py         # Script de xeración de iconas
├── admin.manifest           # Manifesto de privilexios de admin UAC
├── app.ico                  # Icona da aplicación
├── app.png                  # Vista previa da icona
├── requirements.txt         # Dependencias de Python
├── docs/                    # Documentos multi-idioma
│   └── README_*.md
├── i18n/                    # Ficheiros de tradución
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # DLL LibreHardwareMonitorLib
└── dist/
    └── ChipPeek.exe         # Executable compilado
```

## Ficheiro de Configuración

O ficheiro `config.json` gárdase no mesmo directorio que o EXE, contén todos os axustes configurables. Os axustes gárdanse automaticamente cando se modifican.

## Licenza

MIT License

## Desenvolvedor

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL do Proxecto: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Créditos

- LibreHardwareMonitor - Biblioteca de monitorización hardware
- psutil - Monitorización do sistema multiplataforma
- PyInstaller - Ferramenta de empaquetado Python
