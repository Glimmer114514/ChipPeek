# ChipPeek

Windows için hafif bir kayan donanım izleme widget'ı. CPU/GPU frekansı, sıcaklık, VRAM ve bellek kullanımının gerçek zamanlı izlenmesi, tam ekran uygulamalar dahil her zaman en üstte görünür.

> **Diğer Diller**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | **Türkçe** | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Özellikler

- **Gerçek zamanlı izleme**: CPU frekansı, CPU sıcaklığı, GPU frekansı, GPU sıcaklığı, VRAM kullanımı, bellek kullanımı
- **İki görüntüleme modu**: Köşe widget'ı / üst çubuk, tek tıkla geçiş
- **Özelleştirilebilir görüntüleme**: Hangi metriklerin gösterileceğini serbestçe seçin, yüzde/gerçek değerler arasında geçiş yapın
- **Her zaman en üstte**: Tüm pencerelerin üzerinde kalır, tam ekran oyunlarda çalışır
- **Otomatik boyut**: Pencere genişliği içeriğe göre otomatik olarak ayarlanır
- **Ayarlanabilir stil**: Pencere opaklığı, arka plan şeffaflığı, yazı tipi boyutu - hepsi ayarlanabilir
- **Çok dilli destek**: 20+ dil, sistem dilini otomatik olarak algılar
- **Kullanışlı çalıştırma**: Taşımak için sol tıkla sürükleyin, hızlı ayarlar için sağ tık menüsü, ekran kenarlarına otomatik yapışma
- **Yapılandırılabilir örnekleme**: 200ms - 3000ms ayarlanabilir
- **Otomatik başlatma**: Windows oturum açmada otomatik olarak başlar
- **Düşük kaynak kullanımı**: Arka planda minimum ayak izi

## Hızlı Başlangıç

### Doğrudan Kullanım

`ChipPeek.exe` dosyasını indirin ve çalıştırmak için çift tıklayın (CPU sıcaklığı ve doğru frekans okuması için otomatik olarak yönetici izni isteyecektir).

### Kaynak Koddan Çalıştırma

```bash
# Depoyu klonlayın
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Çalıştır
python main.py
```

## Sistem Gereksinimleri

- Windows 10 / Windows 11
- Yönetici izinleri (önerilir), aksi takdirde CPU sıcaklığı ve doğru frekans kullanılamayabilir
- .NET Framework 4.7.2 veya üstü (LibreHardwareMonitor tarafından gerekli)

## EXE Olarak Derleme

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Derlemeden sonra, EXE dosyası `dist/ChipPeek.exe` konumunda bulunur.

## Kullanım

### Temel İşlemler

| Eylem | Açıklama |
|------|------|
| Sol tıkla sürükleme | Pencere konumunu taşı |
| Sağ tık | Menüyü aç (modu değiştir / ayarlar / çıkış) |
| Otomatik yapışma | Ekran kenarlarının 20px içinde otomatik olarak yapışır |

### Görüntüleme Modları

- **Köşe Widget'ı**: tüm metrikler dikey olarak düzenlenir, ekranın herhangi bir köşesine yerleştirilebilir
- **Üst Çubuk**: tüm metrikler yatay olarak düzenlenir, varsayılan olarak ekranın üst kısmında ortalanır

### Ayarlar

- **Görüntüleme modu**: köşe widget'ı / üst çubuk
- **Widget konumu**: sağ alt / sol alt / sağ üst / sol üst
- **Pencere opaklığı**: %30 - %100 genel pencere şeffaflığı
- **Arka plan şeffaflığı**: %0 - %100 arka plan şeffaf (metin net kalır)
- **Örnekleme aralığı**: 200ms - 3000ms veri yenileme hızı
- **Yazı tipi boyutu**: 8 - 20 punto yazı tipi
- **Dil**: 20+ dil, sistem dilini otomatik olarak algılar
- **Görüntüleme metrikleri**: her metriği bağımsız olarak aç/kapat
- **Görüntüleme biçimi**: VRAM / Bellek yüzde veya gerçek değerler arasında geçiş yapabilir
- **Otomatik başlatma**: Windows oturum açmada otomatik olarak çalıştır

## Teknoloji Yığını

- **GUI**：Tkinter
- **Donanım verileri**：LibreHardwareMonitorLib (pythonnet aracılığıyla), psutil, pynvml (NVIDIA GPU için yedek çözüm)
- **Sistem entegrasyonu**：pywin32 (pencere en üstte, otomatik başlatma kayıt defteri)
- **Paketleme**：PyInstaller

## Proje Yapısı

```
ChipPeek/
├── main.py                  # Giriş noktası
├── monitor_window.py        # Pencere UI ve etkileşim mantığı
├── hardware_monitor.py      # Donanım veri toplama
├── config.py                # Yapılandırma yönetimi
├── i18n.py                  # Uluslararasılaştırma
├── generate_icon.py         # Simge oluşturma betiği
├── admin.manifest           # UAC yönetici izni bildirimi
├── app.ico                  # Uygulama simgesi
├── app.png                  # Simge önizlemesi
├── requirements.txt         # Python bağımlılıkları
├── docs/                    # Çok dilli belgeler
│   └── README_*.md
├── i18n/                    # Çeviri dosyaları
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Derlenmiş yürütülebilir dosya
```

## Yapılandırma Dosyası

`config.json` dosyası EXE ile aynı dizinde kaydedilir ve tüm ayarlanabilir ayarları içerir. Ayarlar değiştirildiğinde otomatik olarak kaydedilir.

## Lisans

MIT License

## Geliştirici

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- Proje URL'si: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Teşekkürler

- LibreHardwareMonitor - Donanım izleme kitaplığı
- psutil - Çapraz platform sistem izleme
- PyInstaller - Python paketleme aracı
