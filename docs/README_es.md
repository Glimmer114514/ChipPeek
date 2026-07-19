# ChipPeek

Un widget flotante ligero de monitorización de hardware para Windows. Monitoriza en tiempo real la frecuencia de CPU/GPU, temperatura, VRAM y uso de memoria, siempre visible incluyendo aplicaciones en pantalla completa.

> **Otros idiomas**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | **Español** | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Características

- **Monitorización en tiempo real**: frecuencia de CPU, temperatura de CPU, frecuencia de GPU, temperatura de GPU, uso de VRAM, uso de memoria
- **Modos de visualización dual**: widget de esquina / barra superior, cambio con un clic
- **Visualización personalizable**: elige libremente qué métricas mostrar, alterna entre porcentaje/valores reales
- **Siempre visible**: se mantiene por encima de todas las ventanas, funciona en juegos de pantalla completa
- **Tamaño automático**: el ancho de la ventana se ajusta automáticamente al contenido
- **Estilo ajustable**: opacidad de la ventana, transparencia del fondo, tamaño de fuente - todo ajustable
- **Soporte multilingüe**: más de 20 idiomas, detecta automáticamente el idioma del sistema
- **Operación conveniente**: arrastre con clic izquierdo para mover, menú de clic derecho para ajustes rápidos, ajuste automático a los bordes de la pantalla
- **Muestreo configurable**: 200ms - 3000ms ajustable
- **Inicio automático**: se inicia automáticamente al iniciar sesión en Windows
- **Bajo consumo de recursos**: huella mínima en segundo plano

## Inicio rápido

### Uso directo

Descarga `ChipPeek.exe` y haz doble clic para ejecutarlo (solicitará automáticamente privilegios de administrador para la temperatura de la CPU y la lectura precisa de la frecuencia).

### Ejecutar desde código fuente

```bash
# Clonar el repositorio
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python main.py
```

## Requisitos del sistema

- Windows 10 / Windows 11
- Privilegios de administrador (recomendado), de lo contrario la temperatura de la CPU y la frecuencia precisa pueden no estar disponibles
- .NET Framework 4.7.2 o superior (requerido por LibreHardwareMonitor)

## Compilar como EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Después de compilar, el archivo EXE se encuentra en `dist/ChipPeek.exe`.

## Uso

### Operaciones básicas

| Acción | Descripción |
|------|------|
| Arrastrar con clic izquierdo | Mover la posición de la ventana |
| Clic derecho | Abrir menú (cambiar modo / ajustes / salir) |
| Ajuste automático | Se ajusta automáticamente a 20px de los bordes de la pantalla |

### Modos de visualización

- **Widget de esquina**: todas las métricas dispuestas verticalmente, se puede colocar en cualquier esquina de la pantalla
- **Barra superior**: todas las métricas dispuestas horizontalmente, centrada en la parte superior de la pantalla por defecto

### Ajustes

- **Modo de visualización**: widget de esquina / barra superior
- **Posición del widget**: abajo derecha / abajo izquierda / arriba derecha / arriba izquierda
- **Opacidad de la ventana**: 30% - 100% de transparencia general de la ventana
- **Transparencia del fondo**: 0% - 100% de fondo transparente (el texto se mantiene nítido)
- **Intervalo de muestreo**: 200ms - 3000ms tasa de refresco de datos
- **Tamaño de fuente**: fuente de 8 - 20 puntos
- **Idioma**: más de 20 idiomas, detecta automáticamente el idioma del sistema
- **Métricas de visualización**: activa/desactiva cada métrica de forma independiente
- **Formato de visualización**: VRAM / Memoria pueden alternar entre porcentaje o valores reales
- **Inicio automático**: ejecutar automáticamente al iniciar sesión en Windows

## Pila tecnológica

- **GUI**：Tkinter
- **Datos de hardware**：LibreHardwareMonitorLib (a través de pythonnet), psutil, pynvml (alternativa para GPU NVIDIA)
- **Integración del sistema**：pywin32 (ventana siempre visible, registro de inicio automático)
- **Empaquetado**：PyInstaller

## Estructura del proyecto

```
ChipPeek/
├── main.py                  # Punto de entrada
├── monitor_window.py        # UI de la ventana y lógica de interacción
├── hardware_monitor.py      # Recopilación de datos de hardware
├── config.py                # Gestión de configuración
├── i18n.py                  # Internacionalización
├── generate_icon.py         # Script de generación de iconos
├── admin.manifest           # Manifiesto de privilegios de administrador UAC
├── app.ico                  # Icono de la aplicación
├── app.png                  # Vista previa del icono
├── requirements.txt         # Dependencias de Python
├── docs/                    # Documentación multilingüe
│   └── README_*.md
├── i18n/                    # Archivos de traducción
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Ejecutable compilado
```

## Archivo de configuración

El archivo `config.json` se guarda en el mismo directorio que el EXE y contiene todos los ajustes configurables. Los ajustes se guardan automáticamente al modificarlos.

## Licencia

MIT License

## Desarrollador

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL del proyecto: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Créditos

- LibreHardwareMonitor - Biblioteca de monitorización de hardware
- psutil - Monitorización del sistema multiplataforma
- PyInstaller - Herramienta de empaquetado de Python
