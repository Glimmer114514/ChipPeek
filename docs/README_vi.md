# ChipPeek

Một tiện ích giám sát phần cứng nổi nhẹ cho Windows. Giám sát thời gian thực tần số CPU/GPU, nhiệt độ, VRAM và sử dụng bộ nhớ, luôn hiển thị trên cùng kể cả ứng dụng toàn màn hình.

> **Ngôn ngữ khác**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | **Tiếng Việt** | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Tính năng

- **Giám sát thời gian thực**: tần số CPU, nhiệt độ CPU, tần số GPU, nhiệt độ GPU, sử dụng VRAM, sử dụng bộ nhớ
- **Hai chế độ hiển thị**: tiện ích góc / thanh trên, chuyển đổi bằng một cú nhấp
- **Hiển thị có thể tùy chỉnh**: tự do chọn số liệu nào sẽ hiển thị, chuyển đổi giữa phần trăm/giá trị thực tế
- **Luôn trên cùng**: nằm trên tất cả các cửa sổ, hoạt động trong game toàn màn hình
- **Kích thước tự động**: chiều rộng cửa sổ tự động điều chỉnh theo nội dung
- **Kiểu dáng có thể điều chỉnh**: độ mờ cửa sổ, độ trong suốt nền, kích thước phông chữ - tất cả đều có thể điều chỉnh
- **Hỗ trợ đa ngôn ngữ**: 20+ ngôn ngữ, tự động phát hiện ngôn ngữ hệ thống
- **Hoạt động tiện lợi**: kéo bằng nút trái để di chuyển, menu nút phải cho cài đặt nhanh, tự động dính vào cạnh màn hình
- **Lấy mẫu có thể cấu hình**: 200ms - 3000ms có thể điều chỉnh
- **Khởi động tự động**: khởi chạy tự động khi đăng nhập Windows
- **Sử dụng tài nguyên thấp**: dấu chân tối thiểu ở chế độ nền

## Bắt đầu nhanh

### Sử dụng trực tiếp

Tải xuống `ChipPeek.exe` và nhấp đúp để chạy (sẽ tự động yêu cầu quyền quản trị viên cho nhiệt độ CPU và đọc tần số chính xác).

### Chạy từ mã nguồn

```bash
# Sao chép kho lưu trữ
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Cài đặt các phụ thuộc
pip install -r requirements.txt

# Chạy
python main.py
```

## Yêu cầu hệ thống

- Windows 10 / Windows 11
- Quyền quản trị viên (khuyến nghị), nếu không nhiệt độ CPU và tần số chính xác có thể không khả dụng
- .NET Framework 4.7.2 trở lên (bắt buộc cho LibreHardwareMonitor)

## Xây dựng thành EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Sau khi xây dựng, tệp EXE nằm ở `dist/ChipPeek.exe`.

## Cách sử dụng

### Thao tác cơ bản

| Thao tác | Mô tả |
|------|------|
| Kéo nút trái | Di chuyển vị trí cửa sổ |
| Nút phải | Mở menu (chuyển đổi chế độ / cài đặt / thoát) |
| Tự động dính | Tự động dính trong phạm vi 20px từ cạnh màn hình |

### Chế độ hiển thị

- **Tiện ích góc**: tất cả các số liệu được sắp xếp theo chiều dọc, có thể đặt ở bất kỳ góc nào của màn hình
- **Thanh trên**: tất cả các số liệu được sắp xếp theo chiều ngang, mặc định được căn giữa ở trên cùng của màn hình

### Cài đặt

- **Chế độ hiển thị**: tiện ích góc / thanh trên
- **Vị trí tiện ích**: dưới cùng bên phải / dưới cùng bên trái / trên cùng bên phải / trên cùng bên trái
- **Độ mờ cửa sổ**: 30% - 100% độ trong suốt tổng thể của cửa sổ
- **Độ trong suốt nền**: 0% - 100% nền trong suốt (văn bản vẫn rõ nét)
- **Khoảng lấy mẫu**: 200ms - 3000ms tốc độ làm mới dữ liệu
- **Kích thước phông chữ**: phông chữ 8 - 20 điểm
- **Ngôn ngữ**: 20+ ngôn ngữ, tự động phát hiện ngôn ngữ hệ thống
- **Số liệu hiển thị**: bật/tắt từng số liệu độc lập
- **Định dạng hiển thị**: VRAM / Bộ nhớ có thể chuyển đổi giữa phần trăm hoặc giá trị thực tế
- **Khởi động tự động**: chạy tự động khi đăng nhập Windows

## Ngăn xếp công nghệ

- **GUI**：Tkinter
- **Dữ liệu phần cứng**：LibreHardwareMonitorLib (thông qua pythonnet), psutil, pynvml (phương án dự phòng cho GPU NVIDIA)
- **Tích hợp hệ thống**：pywin32 (cửa sổ trên cùng, đăng ký khởi động tự động)
- **Đóng gói**：PyInstaller

## Cấu trúc dự án

```
ChipPeek/
├── main.py                  # Điểm vào
├── monitor_window.py        # Giao diện người dùng cửa sổ và logic tương tác
├── hardware_monitor.py      # Thu thập dữ liệu phần cứng
├── config.py                # Quản lý cấu hình
├── i18n.py                  # Quốc tế hóa
├── generate_icon.py         # Tập lệnh tạo biểu tượng
├── admin.manifest           # Tệp kê khai quyền quản trị UAC
├── app.ico                  # Biểu tượng ứng dụng
├── app.png                  # Xem trước biểu tượng
├── requirements.txt         # Phụ thuộc Python
├── docs/                    # Tài liệu đa ngôn ngữ
│   └── README_*.md
├── i18n/                    # Tệp dịch
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Tệp thực thi đã biên dịch
```

## Tệp cấu hình

Tệp `config.json` được lưu trong cùng thư mục với EXE, chứa tất cả các cài đặt có thể điều chỉnh. Cài đặt được lưu tự động khi sửa đổi.

## Giấy phép

MIT License

## Nhà phát triển

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL dự án: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Lời cảm ơn

- LibreHardwareMonitor - Thư viện giám sát phần cứng
- psutil - Giám sát hệ thống đa nền tảng
- PyInstaller - Công cụ đóng gói Python
