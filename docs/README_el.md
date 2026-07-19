# ChipPeek

Ένα ελαφρύ επιπλέον widget παρακολούθησης υλικού για Windows. Παρακολούθηση σε πραγματικό χρόνο της συχνότητας CPU/GPU, θερμοκρασίας, VRAM και χρήσης μνήμης, πάντα στην κορυφή συμπεριλαμβανομένων εφαρμογών πλήρους οθόνης.

> **Άλλες γλώσσες**: [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md) | [English](README_en.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [ไทย](README_th.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Türkçe](README_tr.md) | [Italiano](README_it.md) | [Nederlands](README_nl.md) | [Polski](README_pl.md) | [हिन्दी](README_hi.md) | [বাংলা](README_bn.md) | [Svenska](README_sv.md) | [Norsk](README_no.md) | [Dansk](README_da.md) | [Suomi](README_fi.md) | [Čeština](README_cs.md) | **Ελληνικά** | [Magyar](README_hu.md) | [Română](README_ro.md) | [Українська](README_uk.md) | [Slovenčina](README_sk.md) | [Български](README_bg.md) | [Hrvatski](README_hr.md) | [Српски](README_sr.md) | [Català](README_ca.md) | [Slovenščina](README_sl.md) | [Eesti](README_et.md) | [Latviešu](README_lv.md) | [Lietuvių](README_lt.md) | [فارسی](README_fa.md) | [Bahasa Melayu](README_ms.md) | [اردو](README_ur.md) | [தமிழ்](README_ta.md) | [తెలుగు](README_te.md) | [मराठी](README_mr.md) | [ગુજરાતી](README_gu.md) | [ਪੰਜਾਬੀ](README_pa.md) | [ಕನ್ನಡ](README_kn.md) | [മലയാളം](README_ml.md) | [Қазақша](README_kk.md) | [O'zbekcha](README_uz.md) | [עברית](README_he.md) | [မြန်မာဘာသာ](README_my.md) | [ភាសាខ្មែរ](README_km.md) | [ພາສາລາວ](README_lo.md) | [Kiswahili](README_sw.md) | [Afrikaans](README_af.md) | [አማርኛ](README_am.md) | [isiZulu](README_zu.md) | [Filipino](README_fil.md) | [Gaeilge](README_ga.md) | [Íslenska](README_is.md) | [Malti](README_mt.md) | [Cymraeg](README_cy.md) | [Euskara](README_eu.md) | [Galego](README_gl.md) | [नेपाली](README_ne.md) | [සිංහල](README_si.md) | [ქართული](README_ka.md) | [Հայերեն](README_hy.md) | [Македонски](README_mk.md) | [Беларуская](README_be.md) | [ייִדיש](README_yi.md) | [Lëtzebuergesch](README_lb.md) | [Esperanto](README_eo.md)

## Χαρακτηριστικά

- **Παρακολούθηση σε πραγματικό χρόνο**: συχνότητα CPU, θερμοκρασία CPU, συχνότητα GPU, θερμοκρασία GPU, χρήση VRAM, χρήση μνήμης
- **Δύο λειτουργίες εμφάνισης**: widget γωνίας / επάνω γραμμή, εναλλαγή με ένα κλικ
- **Προσαρμόσιμη εμφάνιση**: επιλέξτε ελεύθερα ποιες μετρικές να εμφανίζονται, εναλλαγή μεταξύ ποσοστού/πραγματικών τιμών
- **Πάντα στην κορυφή**: παραμένει πάνω από όλα τα παράθυρα, λειτουργεί σε παιχνίδια πλήρους οθόνης
- **Αυτόματο μέγεθος**: το πλάτος του παραθύρου προσαρμόζεται αυτόματα στο περιεχόμενο
- **Ρυθμιζόμενο στυλ**: αδιαφάνεια παραθύρου, διαφάνεια φόντου, μέγεθος γραμματοσειράς - όλα ρυθμιζόμενα
- **Υποστήριξη πολλών γλωσσών**: 20+ γλώσσες, ανιχνεύει αυτόματα τη γλώσσα του συστήματος
- **Βολεότητα λειτουργίας**: σύρετε με αριστερό κλικ για μετακίνηση, μενού δεξιού κλικ για γρήγορες ρυθμίσεις, αυτόματο προσκόλλημα στις άκρες της οθόνης
- **Ρυθμιζόμενη συχνότητα δειγματοληψίας**: 200ms - 3000ms ρυθμιζόμενο
- **Αυτόματη εκκίνηση**: εκκινείται αυτόματα κατά την είσοδο στα Windows
- **Χαμηλή χρήση πόρων**: ελάχιστη κατασκευή στο παρασκήνιο

## Γρήγορη έναρξη

### Απευθείας χρήση

Κατεβάστε το `ChipPeek.exe` και κάντε διπλό κλικ για εκτέλεση (θα ζητήσει αυτόματα δικαιώματα διαχειριστή για τη θερμοκρασία CPU και την ακριβή ανάγνωση συχνότητας).

### Εκτέλεση από πηγαίο κώδικα

```bash
# Κλωνοποιήστε το αποθετήριο
git clone https://github.com/Glimmer114514/ChipPeek.git
cd ChipPeek

# Εγκαταστήστε τις εξαρτήσεις
pip install -r requirements.txt

# Εκτελέστε
python main.py
```

## Απαιτήσεις συστήματος

- Windows 10 / Windows 11
- Δικαιώματα διαχειριστή (συνιστώνται), διαφορετικά η θερμοκρασία CPU και η ακριβής συχνότητα ενδέχεται να μην είναι διαθέσιμες
- .NET Framework 4.7.2 ή νεότερο (απαιτείται από το LibreHardwareMonitor)

## Δημιουργία ως EXE

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "ChipPeek" --icon "app.ico" --manifest "admin.manifest" --add-data "libs;libs" --add-data "app.ico;." --hidden-import "clr" --hidden-import "pynvml" --hidden-import "win32gui" --hidden-import "win32con" main.py
```

Μετά τη δημιουργία, το αρχείο EXE βρίσκεται στη διαδρομή `dist/ChipPeek.exe`.

## Χρήση

### Βασικές λειτουργίες

| Λειτουργία | Περιγραφή |
|------|------|
| Σύρσιμο με αριστερό κλικ | Μετακίνηση του παραθύρου |
| Δεξί κλικ | Άνοιγμα μενού (αλλαγή λειτουργίας / ρυθμίσεις / έξοδος) |
| Αυτόματο προσκόλλημα | Προσκολλάται αυτόματα εντός 20px από τις άκρες της οθόνης |

### Λειτουργίες εμφάνισης

- **Widget γωνίας**: όλες οι μετρικές διατεταγμένες κάθετα, μπορούν να τοποθετηθούν σε οποιαδήποτε γωνία της οθόνης
- **Επάνω γραμμή**: όλες οι μετρικές διατεταγμένες οριζόντια, προεπιλεγμένα κεντραρισμένες στο επάνω μέρος της οθόνης

### Ρυθμίσεις

- **Λειτουργία εμφάνισης**: widget γωνίας / επάνω γραμμή
- **Θέση widget**: κάτω δεξιά / κάτω αριστερά / πάνω δεξιά / πάνω αριστερά
- **Αδιαφάνεια παραθύρου**: 30% - 100% συνολική διαφάνεια παραθύρου
- **Διαφάνεια φόντου**: 0% - 100% διαφανές φόντο (το κείμενο παραμένει καθαρό)
- **Διάστημα δειγματοληψίας**: 200ms - 3000ms συχνότητα ανανέωσης δεδομένων
- **Μέγεθος γραμματοσειράς**: 8 - 20 πόντοι
- **Γλώσσα**: 20+ γλώσσες, ανιχνεύει αυτόματα τη γλώσσα του συστήματος
- **Μετρικές εμφάνισης**: ενεργοποίηση/απενεργοποίηση κάθε μετρικής ανεξάρτητα
- **Μορφότυπος εμφάνισης**: VRAM / Μνήμη μπορούν να εναλλάσσονται μεταξύ ποσοστού ή πραγματικών τιμών
- **Αυτόματη εκκίνηση**: αυτόματη εκτέλεση κατά την είσοδο στα Windows

## Τεχνολογική στοίβα

- **GUI**：Tkinter
- **Δεδομένα υλικού**：LibreHardwareMonitorLib (μέσω pythonnet), psutil, pynvml (εναλλακτικό για NVIDIA GPU)
- **Ενσωμάτωση συστήματος**：pywin32 (παράθυρο πάντα στην κορυφή, μητρώο αυτόματης εκκίνησης)
- **Συσκευασία**：PyInstaller

## Δομή έργου

```
ChipPeek/
├── main.py                  # Σημείο εισόδου
├── monitor_window.py        # UI παραθύρου και λογική αλληλεπίδρασης
├── hardware_monitor.py      # Συλλογή δεδομένων υλικού
├── config.py                # Διαχείριση διαμόρφωσης
├── i18n.py                  # Διεθνοποίηση
├── generate_icon.py         # Σενάριο δημιουργίας εικονιδίων
├── admin.manifest           # Διακηρύξη δικαιωμάτων διαχειριστή UAC
├── app.ico                  # Εικονίδιο εφαρμογής
├── app.png                  # Προεπισκόπηση εικονιδίου
├── requirements.txt         # Εξαρτήσεις Python
├── docs/                    # Πολύγλωσση τεκμηρίωση
│   └── README_*.md
├── i18n/                    # Αρχεία μετάφρασης
│   └── *.json
├── libs/
│   └── lhm/
│       └── lib/net472/      # LibreHardwareMonitorLib DLL
└── dist/
    └── ChipPeek.exe         # Μεταγλωττισμένο εκτελέσιμο αρχείο
```

## Αρχείο διαμόρφωσης

Το αρχείο `config.json` αποθηκεύεται στον ίδιο κατάλογο με το EXE και περιέχει όλες τις ρυθμιζόμενες ρυθμίσεις. Οι ρυθμίσεις αποθηκεύονται αυτόματα όταν τροποποιούνται.

## Άδεια

MIT License

## Προγραμματιστής

**R41NH4RD**

- GitHub: [@R41NH4RD](https://github.com/Glimmer114514)
- URL έργου: [https://github.com/Glimmer114514/ChipPeek](https://github.com/Glimmer114514/ChipPeek)

## Ευχαριστίες

- LibreHardwareMonitor - Βιβλιοθήκη παρακολούθησης υλικού
- psutil - Παρακολούθηση συστήματος μεταξύ πλατφορμών
- PyInstaller - Εργαλείο συσκευασίας Python
