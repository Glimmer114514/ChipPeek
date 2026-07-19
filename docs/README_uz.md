# ChipPeek

Windows uchun engil suzuvchi apparat ta'minot monitoring vidjeti. CPU/GPU chastotasi, harorati, VRAM va xotiradan foydalanishning real vaqt monitoringi, to'liq ekran ilovalari bilan ham har doim yuqorida bo'ladi.

> **Boshqa tillar**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | [Ελληνικά](README_el.md) | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | **O'zbekcha** | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Xususiyatlar

- **Real vaqt monitoringi**: CPU chastotasi, CPU harorati, GPU chastotasi, GPU harorati, VRAM foydalanishi, xotira foydalanishi
- **Ikki displey rejimi**: Burchak vidjeti / Yuqori panel, bir bosishda almashtirish
- **Moslashtirilgan displey**: Qaysi metrikalarni ko'rsatish kerakligini erkin tanlang, foiz/haqiqiy qiymatlar o'rtasida almashtiring
- **Har doim yuqorida**: Barcha oynalar yuqorisida bo'ladi, to'liq ekran o'yinlarida ishlaydi
- **Avtomatik o'lcham**: Mazmunga ko'ra oyna kengligi avtomatik tarzda sozlanadi
- **Sozlanadigan uslub**: Oyna shaffofligi, fon shaffofligi, shrift o'lchami - hammasi sozlanadi
- **Ko'p tillik qo'llab-quvvatlash**: 20+ til, avtomatik tarzda tizim tilini aniqlaydi
- **Oson operatsiya**: Chap bosish bilan tortib o'tkazing, o'ng bosish menyusi tez sozlamalar uchun, ekran chetida avtomatik qulflash
- **Namuna olish chastotasini sozlash**: 200ms - 3000ms sozlanadi
- **Avtomatik ishga tushirish**: Windows ga kirganda avtomatik tarzda boshlanadi
- **Kam resurs foydalanishi**: Fonda minimal joy

## Tez boshlanish

### To'g'ridan-to'g'ri foydalanish

`ChipPeek.exe` ni yuklab oling va ishga tushirish uchun ikki marta bosing (CPU harorati va aniq chastotani o'qish uchun avtomatik tarzda ma'muriyat huquqlarini so'raydi).

### Manba kodidan ishga tushirish

```bash
# Omborni klonlang
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Bog'liqliklarni o'rnating
pip install -r requirements.txt

# Ishga tushiring
python main.py
```

## Tizim talablari

- Windows 10 / Windows 11
- Ma'muriyat huquqlari (Tavsiya etiladi), aks holda CPU harorati va aniq chastota mavjud bo'lmasligi mumkin
- .NET Framework 4.7.2 yoki undan yuqori (LibreHardwareMonitor uchun zarur)

## EXE sifatida yasash

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Yasallgandan so'ng, EXE fayli `dist/ChipPeek.exe` da joylashgan.

## Foydalanish

### Asosiy operatsiyalar

| Operatsiya | Tavsif |
|------|------|
| Chap bosish bilan tortish | Oyna joyini o'zgartirish |
| O'ng bosish | Menyu ochish (rejimni almashtirish / sozlamalar / chiqish) |
| Avtomatik qulflash | Ekranning chetidan 20px ichida avtomatik tarzda qulflanadi |

### Displey rejimlari

- **Burchak vidjeti**: Barcha metrikalar vertikal tarzda joylashtirilgan, ekranning istalgan burchagiga qo'yish mumkin
- **Yuqori panel**: Barcha metrikalar gorizontal tarzda joylashtirilgan, odatda ekranning yuqori qismida o'rtada joylashgan

### Sozlamalar

- **Displey rejimi**: Burchak vidjeti / Yuqori panel
- **Vidjet joylashuvi**: Pastki o'ng / Pastki chap / Yuqori o'ng / Yuqori chap
- **Oyna shaffofligi**: 30% - 100% umumiy oyna shaffofligi
- **Fon shaffofligi**: 0% - 100% fon shaffofligi (matn aniq qoladi)
- **Namuna olish oralig'i**: 200ms - 3000ms ma'lumotni yangilash tezligi
- **Shrift o'lchami**: 8 - 20 nuqtalar
- **Til**: 20+ til, avtomatik tarzda tizim tilini aniqlaydi
- **Displey metrikalari**: Har bir metrikani mustaqil yoqish/o'chirish
- **Displey formati**: VRAM / xotira foiz yoki haqiqiy qiymatlar o'rtasida almashtirish mumkin
- **Avtomatik ishga tushirish**: Windows ga kirganda avtomatik tarzda ishga tushirish

## Texnik to'plam

- **GUI**：Tkinter
- **Apparat ma'lumotlari**：LibreHardwareMonitorLib (pythonnet orqali), psutil, pynvml (NVIDIA GPU uchun zaxira)
- **Tizim integratsiyasi**：pywin32 (oyna har doim yuqorida, avtomatik ishga tushirish registri)
- **Qadoqlash**：PyInstaller

## Loyihaning tuzilishi

```
ChipPeek/
├── main.py                  # kirish nuqtasi
├── monitor_window.py        # oyna UI va o'zaro ta'sir mantiqi
├── hardware_monitor.py      # apparat ma'lumotlarini to'plash
├── config.py                # konfiguratsiyani boshqarish
├── i18n.py                  # xalqaro lashtirish
├── generate_icon.py         # belgini yaratish skripti
├── admin.manifest           # UAC ma'muriyat huquqlari manifesti
├── app.ico                  # ilova belgisi
├── app.png                  # belgilash oldindan ko'rish
├── requirements.txt         # Python bog'liqliklari
├── docs/                    # ko'p tillik hujjatlashtirish
│   └── README_*.md
├── i18n/                    # tarjima fayllari
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # qurilgan bajariladigan fayl
```

## Konfiguratsiya fayli

`config.json` fayli EXE bilan bir xil katalogda saqlanadi va barcha sozlanadigan sozlamalarni o'z ichiga oladi. Sozlamalar o'zgartirilganda avtomatik tarzda saqlanadi.

## Litsenziya

MIT License

## Dasturchi

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- Loyiha URL: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Minnatdorchiliklar

- LibreHardwareMonitor - apparat ta'minot monitoringi kutubxonasi
- psutil - kross-platformali tizim monitoringi
- PyInstaller - Python qadoqlash vositasi
