# 🔍 SPY-WA-EXTRACTOR v2.0 (Cloud Forensics)
### [ WhatsApp Google Drive Backup Downloader & Telegram Exfiltrator ]

![Version](https://img.shields.io/badge/Version-2.0.0--Pro-red.svg)
![Python](https://img.shields.io/badge/Python-3.11-green.svg)
![Exfiltration](https://img.shields.io/badge/Exfiltration-Telegram%20Bot-blue.svg)

**SPY-WA-EXTRACTOR** adalah alat forensik tingkat lanjut yang dirancang untuk menarik database WhatsApp (`msgstore.db.crypt14/15`) langsung dari Google Drive Cloud dan mengirimkannya secara otomatis ke **Telegram Bot** Anda sebagai akses jarak jauh.

---

## 🚀 Fitur Unggulan (Pro Version)
- **Automatic Cloud Sync**: Mengunduh cadangan WhatsApp tanpa menyentuh perangkat fisik.
- **Telegram Auto-Send**: Mengirimkan file database (.db.crypt) langsung ke Chat ID Telegram Anda.
- **Bypass Authentication**: Menggunakan `gpsoauth` untuk meniru sesi login perangkat Android target.
- **Stealth Extraction**: Proses berjalan di latar belakang (background) tanpa jejak di perangkat target.

---

## 🛠️ Persyaratan & Bahan
1. **Hardware**: PC (Windows/Linux) atau HP Android (Termux).
2. **Kredensial Target**: 
   - Gmail & Password (atau App Password jika 2FA Aktif).
   - **Android ID** perangkat target.
3. **Telegram Bot**:
   - **BOT TOKEN**: Didapat dari `@BotFather`.
   - **CHAT ID**: Didapat dari `@userinfobot`.

---

## 📥 Instalasi

### 📱 Termux (Android)
```bash
pkg update && pkg upgrade
pkg install python git clang make -y
git clone [https://github.com/123tool/WHATSAPP-EXTRACTOR-Forensic-Tools-.git](https://github.com/123tool/WHATSAPP-EXTRACTOR-Forensic-Tools-.git)
cd WHATSAPP-EXTRACTOR-Forensic-Tools
pip install gpsoauth pycryptodome requests==2.23.0
