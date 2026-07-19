# ChipPeek

Widget pemantauan perangkat keras mengambang yang ringan untuk Windows. Pemantauan real-time frekuensi CPU/GPU, suhu, VRAM, dan penggunaan memori, selalu di atas termasuk aplikasi layar penuh.

> **Bahasa Lainnya**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | **Bahasa Indonesia** | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Fitur

- **Pemantauan real-time**: frekuensi CPU, suhu CPU, frekuensi GPU, suhu GPU, penggunaan VRAM, penggunaan memori
- **Dua mode tampilan**: widget sudut / bilah atas, beralih dengan satu klik
- **Tampilan yang dapat disesuaikan**: pilih bebas metrik mana yang akan ditampilkan, beralih antara persentase/nilai sebenarnya
- **Selalu di atas**: tetap di atas semua jendela, berfungsi di game layar penuh
- **Ukuran otomatis**: lebar jendela menyesuaikan secara otomatis dengan konten
- **Gaya yang dapat diatur**: opacity jendela, transparansi latar belakang, ukuran font - semuanya dapat diatur
- **Dukungan multibahasa**: 20+ bahasa, mendeteksi bahasa sistem secara otomatis
- **Operasi yang nyaman**: seret dengan klik kiri untuk memindahkan, menu klik kanan untuk pengaturan cepat, menempel otomatis ke tepi layar
- **Pensampelan yang dapat dikonfigurasi**: 200ms - 3000ms dapat diatur
- **Mulai otomatis**: mulai secara otomatis saat masuk Windows
- **Penggunaan sumber daya rendah**: jejak minimal di latar belakang

## Mulai Cepat

### Penggunaan Langsung

Unduh `ChipPeek.exe` dan klik dua kali untuk menjalankan (akan secara otomatis meminta hak istimewa admin untuk suhu CPU dan pembacaan frekuensi yang akurat).

### Jalankan dari Sumber

```bash
# Klon repositori
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Instal dependensi
pip install -r requirements.txt

# Jalankan
python main.py
```

## Persyaratan Sistem

- Windows 10 / Windows 11
- Hak istimewa administrator (disarankan), jika tidak suhu CPU dan frekuensi akurat mungkin tidak tersedia
- .NET Framework 4.7.2 atau lebih tinggi (dibutuhkan oleh LibreHardwareMonitor)

## Bangun sebagai EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Setelah dibangun, file EXE terletak di `dist/ChipPeek.exe`.

## Penggunaan

### Operasi Dasar

| Tindakan | Deskripsi |
|------|------|
| Seret klik kiri | Pindahkan posisi jendela |
| Klik kanan | Buka menu (ganti mode / pengaturan / keluar) |
| Menempel otomatis | Secara otomatis menempel dalam 20px dari tepi layar |

### Mode Tampilan

- **Widget Sudut**: semua metrik disusun secara vertikal, dapat ditempatkan di sudut layar mana saja
- **Bilah Atas**: semua metrik disusun secara horizontal, secara default berada di tengah bagian atas layar

### Pengaturan

- **Mode tampilan**: widget sudut / bilah atas
- **Posisi widget**: kanan bawah / kiri bawah / kanan atas / kiri atas
- **Opacity jendela**: 30% - 100% transparansi jendela keseluruhan
- **Transparansi latar belakang**: 0% - 100% latar belakang transparan (teks tetap jernih)
- **Interval pensampelan**: 200ms - 3000ms tingkat penyegaran data
- **Ukuran font**: font 8 - 20 poin
- **Bahasa**: 20+ bahasa, mendeteksi bahasa sistem secara otomatis
- **Metrik tampilan**: aktifkan/nonaktifkan setiap metrik secara independen
- **Format tampilan**: VRAM / Memori dapat beralih antara persentase atau nilai sebenarnya
- **Mulai otomatis**: jalankan secara otomatis saat masuk ke Windows

## Tumpukan Teknologi

- **GUI**：Tkinter
- **Data perangkat keras**：LibreHardwareMonitorLib (melalui pythonnet), psutil, pynvml (cadangan untuk GPU NVIDIA)
- **Integrasi sistem**：pywin32 (jendela selalu di atas, registri mulai otomatis)
- **Pengemasan**：PyInstaller

## Struktur Proyek

```
ChipPeek/
├── main.py                  # Titik masuk
├── monitor_window.py        # UI jendela dan logika interaksi
├── hardware_monitor.py      # Pengumpulan data perangkat keras
├── config.py                # Manajemen konfigurasi
├── i18n.py                  # Internasionalisasi
├── generate_icon.py         # Skrip pembuatan ikon
├── admin.manifest           # Manifes hak istimewa admin UAC
├── app.ico                  # Ikon aplikasi
├── app.png                  # Pratinjau ikon
├── requirements.txt         # Dependensi Python
├── docs/                    # Dokumentasi multibahasa
│   └── README_*.md
├── i18n/                    # File terjemahan
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # File eksekutabel yang dikompilasi
```

## File Konfigurasi

File `config.json` disimpan di direktori yang sama dengan EXE, berisi semua pengaturan yang dapat diatur. Pengaturan disimpan secara otomatis saat diubah.

## Lisensi

MIT License

## Pengembang

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL Proyek: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Kredit

- LibreHardwareMonitor - Pustaka pemantauan perangkat keras
- psutil - Pemantauan sistem lintas platform
- PyInstaller - Alat pengemasan Python
