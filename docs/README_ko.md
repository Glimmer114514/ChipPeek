# ChipPeek

가벼운 Windows 하드웨어 모니터링 플로팅 위젯입니다. CPU/GPU 주파수, 온도, VRAM, 메모리 사용량을 실시간으로 모니터링하며 전체화면 앱 위에도 항상 표시됩니다.

> **기타 언어**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | **한국어** | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## 기능

- **실시간 모니터링**: CPU 주파수, CPU 온도, GPU 주파수, GPU 온도, VRAM 사용량, 메모리 사용량
- **듀얼 디스플레이 모드**: 코너 위젯 / 상단 바, 원클릭 전환
- **사용자 정의 디스플레이**: 표시할 지표를 자유롭게 선택, 백분율/실제 값 전환
- **항상 위에 표시**: 모든 창 위에 표시, 풀스크린 게임에서도 작동
- **자동 크기 조정**: 창 너비가 내용에 맞춰 자동 조정
- **조정 가능한 스타일**: 창 불투명도, 배경 투명도, 글꼴 크기 모두 조정 가능
- **다국어 지원**: 20개 이상의 언어, 시스템 언어 자동 감지
- **편리한 조작**: 좌클릭 드래그로 이동, 우클릭 메뉴로 빠른 설정, 화면 가장자리 자동 스냅
- **샘플링 간격 조정**: 200ms - 3000ms 조정 가능
- **자동 시작**: Windows 로그인 시 자동 실행
- **낮은 리소스 사용**: 백그라운드에서 최소한의 리소스 사용

## 빠른 시작

### 직접 사용

`ChipPeek.exe`를 다운로드하고 더블클릭하여 실행하세요 (CPU 온도와 정확한 주파수 읽기를 위해 관리자 권한을 자동으로 요청합니다).

### 소스에서 실행

```bash
# 리포지토리 복제
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# 의존성 설치
pip install -r requirements.txt

# 실행
python main.py
```

## 시스템 요구 사항

- Windows 10 / Windows 11
- 관리자 권한 (권장), 그렇지 않으면 CPU 온도와 정확한 주파수를 읽을 수 없을 수 있습니다
- .NET Framework 4.7.2 이상 (LibreHardwareMonitor에 필요)

## EXE로 빌드

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

빌드 후 EXE 파일은 `dist/ChipPeek.exe`에 위치합니다.

## 사용 방법

### 기본 작업

| 작업 | 설명 |
|------|------|
| 좌클릭 드래그 | 창 위치 이동 |
| 우클릭 | 메뉴 열기 (모드 전환 / 설정 / 종료) |
| 자동 스냅 | 화면 가장자리 20px 이내에서 자동으로 스냅 |

### 디스플레이 모드

- **코너 위젯**: 모든 지표가 세로로 배열되며 화면 모서리에 배치 가능
- **상단 바**: 모든 지표가 가로로 배열되며 기본적으로 화면 상단 중앙에 표시

### 설정

- **디스플레이 모드**: 코너 위젯 / 상단 바
- **위젯 위치**: 오른쪽 아래 / 왼쪽 아래 / 오른쪽 위 / 왼쪽 위
- **창 불투명도**: 30% - 100% 전체 창 투명도
- **배경 투명도**: 0% - 100% 배경 투명 (텍스트는 선명하게 유지)
- **샘플링 간격**: 200ms - 3000ms 데이터 새로 고침 빈도
- **글꼴 크기**: 8 - 20포인트 글꼴
- **언어**: 20개 이상의 언어, 시스템 언어 자동 감지
- **디스플레이 지표**: 각 지표를 개별적으로 켜기/끄기
- **디스플레이 형식**: VRAM / 메모리는 백분율 또는 실제 값으로 전환 가능
- **자동 시작**: Windows 로그인 시 자동 실행

## 기술 스택

- **GUI**：Tkinter
- **하드웨어 데이터**：LibreHardwareMonitorLib (pythonnet 통해), psutil, pynvml (NVIDIA GPU 대체)
- **시스템 통합**：pywin32 (창 최상위, 자동 시작 레지스트리)
- **패키징**：PyInstaller

## 프로젝트 구조

```
ChipPeek/
├── main.py                  # 진입점
├── monitor_window.py        # 창 UI 및 상호작용 로직
├── hardware_monitor.py      # 하드웨어 데이터 수집
├── config.py                # 설정 관리
├── i18n.py                  # 국제화
├── generate_icon.py         # 아이콘 생성 스크립트
├── admin.manifest           # UAC 관리자 권한 매니페스트
├── app.ico                  # 애플리케이션 아이콘
├── app.png                  # 아이콘 미리보기
├── requirements.txt         # Python 의존성
├── docs/                    # 다국어 문서
│   └── README_*.md
├── i18n/                    # 번역 파일
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # 컴파일된 실행 파일
```

## 설정 파일

`config.json` 파일은 EXE와 같은 디렉터리에 저장되며 모든 조정 가능한 설정이 포함되어 있습니다. 설정이 변경되면 자동으로 저장됩니다.

## 라이선스

MIT License

## 개발자

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- 프로젝트 URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## 감사의 글

- LibreHardwareMonitor - 하드웨어 모니터링 라이브러리
- psutil - 크로스플랫폼 시스템 모니터링
- PyInstaller - Python 패키징 도구
