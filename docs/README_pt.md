# ChipPeek

Um widget flutuante leve de monitoramento de hardware para Windows. Monitoramento em tempo real de frequência CPU/GPU, temperatura, VRAM e uso de memória, sempre visível inclusive em aplicativos de tela cheia.

> **Outros idiomas**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | **Português** | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Recursos

- **Monitoramento em tempo real**: frequência CPU, temperatura CPU, frequência GPU, temperatura GPU, uso de VRAM, uso de memória
- **Modos de exibição duplos**: widget de canto / barra superior, alternância com um clique
- **Exibição personalizável**: escolha livremente quais métricas mostrar, alterne entre porcentagem/valores reais
- **Sempre visível**: fica acima de todas as janelas, funciona em jogos de tela cheia
- **Dimensionamento automático**: a largura da janela se ajusta automaticamente ao conteúdo
- **Estilo ajustável**: opacidade da janela, transparência do fundo, tamanho da fonte - tudo ajustável
- **Suporte multilíngue**: mais de 20 idiomas, detecta automaticamente o idioma do sistema
- **Operação conveniente**: arraste com clique esquerdo para mover, menu de clique direito para configurações rápidas, encaixe automático nas bordas da tela
- **Amostragem configurável**: 200ms - 3000ms ajustável
- **Inicialização automática**: inicia automaticamente no login do Windows
- **Baixo uso de recursos**: pegada mínima em segundo plano

## Início rápido

### Uso direto

Baixe `ChipPeek.exe` e dê dois cliques para executar (solicitará automaticamente privilégios de administrador para temperatura da CPU e leitura precisa de frequência).

### Executar do código-fonte

```bash
# Clonar o repositório
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Instalar dependências
pip install -r requirements.txt

# Executar
python main.py
```

## Requisitos do sistema

- Windows 10 / Windows 11
- Privilégios de administrador (recomendado), caso contrário a temperatura da CPU e a frequência precisa podem não estar disponíveis
- .NET Framework 4.7.2 ou superior (requerido pelo LibreHardwareMonitor)

## Compilar como EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Após a compilação, o arquivo EXE está localizado em `dist/ChipPeek.exe`.

## Uso

### Operações básicas

| Ação | Descrição |
|------|------|
| Arrastar com clique esquerdo | Mover a posição da janela |
| Clique direito | Abrir menu (alterar modo / configurações / sair) |
| Encaixe automático | Encaixa automaticamente a 20px das bordas da tela |

### Modos de exibição

- **Widget de canto**: todas as métricas dispostas verticalmente, podem ser colocadas em qualquer canto da tela
- **Barra superior**: todas as métricas dispostas horizontalmente, centralizadas no topo da tela por padrão

### Configurações

- **Modo de exibição**: widget de canto / barra superior
- **Posição do widget**: inferior direito / inferior esquerdo / superior direito / superior esquerdo
- **Opacidade da janela**: 30% - 100% de transparência geral da janela
- **Transparência do fundo**: 0% - 100% de fundo transparente (o texto permanece nítido)
- **Intervalo de amostragem**: 200ms - 3000ms taxa de atualização de dados
- **Tamanho da fonte**: fonte de 8 - 20 pontos
- **Idioma**: mais de 20 idiomas, detecta automaticamente o idioma do sistema
- **Métricas de exibição**: ative/desative cada métrica independentemente
- **Formato de exibição**: VRAM / Memória podem alternar entre porcentagem ou valores reais
- **Inicialização automática**: executar automaticamente ao fazer login no Windows

## Pilha tecnológica

- **GUI**：Tkinter
- **Dados de hardware**：LibreHardwareMonitorLib (via pythonnet), psutil, pynvml (alternativa para GPU NVIDIA)
- **Integração do sistema**：pywin32 (janela sempre visível, registro de inicialização automática)
- **Empacotamento**：PyInstaller

## Estrutura do projeto

```
ChipPeek/
├── main.py                  # Ponto de entrada
├── monitor_window.py        # UI da janela e lógica de interação
├── hardware_monitor.py      # Coleta de dados de hardware
├── config.py                # Gerenciamento de configuração
├── i18n.py                  # Internacionalização
├── generate_icon.py         # Script de geração de ícones
├── admin.manifest           # Manifesto de privilégios de admin UAC
├── app.ico                  # Ícone do aplicativo
├── app.png                  # Visualização do ícone
├── requirements.txt         # Dependências Python
├── docs/                    # Documentação multilíngue
│   └── README_*.md
├── i18n/                    # Arquivos de tradução
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Executável compilado
```

## Arquivo de configuração

O arquivo `config.json` é salvo no mesmo diretório que o EXE e contém todas as configurações ajustáveis. As configurações são salvas automaticamente quando modificadas.

## Licença

MIT License

## Desenvolvedor

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL do projeto: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Créditos

- LibreHardwareMonitor - Biblioteca de monitoramento de hardware
- psutil - Monitoramento de sistema multiplataforma
- PyInstaller - Ferramenta de empacotamento Python
