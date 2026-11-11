

import re

def read_log_file(file_path: str) -> list:
    """Fungsi untuk membaca file log dan mengembalikan daftar baris teks."""
    try:
        # Membuka file dalam mode 'r' (read/baca)
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines 
    except FileNotFoundError:
        print(f"[ERROR] File tidak ditemukan di lokasi: {file_path}")
        return []

def parse_ssh_log(line: str) -> dict:
    """Mengekstrak informasi penting dari baris log SSH menjadi Dictionary."""
    
    # (\w+)     --> menangkap kata apa pun (untuk username)
    # ([\d\.]+) --> menangkap kombinasi angka dan titik (untuk IP Address)
    pola = r"(Failed|Accepted) password for (\w+) from ([\d\.]+)"
    pencarian = re.search(pola, line)

    if pencarian:
        return {
            "status": pencarian.group(1),
            "user": pencarian.group(2),
            "ip_address": pencarian.group(3)
        }
    return None

def detect_brute_force(parsed_logs: list, threshold: int = 3) -> dict:
    """Menghitung jumlah kegagalan per IP dan mendeteksi yang melewati batas threshold."""
    
    failed_attempts = {} # Dictionary untuk menyimpan jumlah gagal per IP
    alerts = {}          # Dictionary untuk menyimpan IP yang terkena alert

    for log in parsed_logs: 
        if log["status"] == "Failed":
            ip = log["ip_address"]
            
            # Jika IP sudah ada di list, tambah 1. Jika belum, set ke 1.
            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

            # Cek apakah sudah melebihi batas (threshold)
            if failed_attempts[ip] >= threshold:
                alerts[ip] = f"Terdeteksi Brute Force: {failed_attempts[ip]}x gagal login."
                
    return alerts

# Blok eksekusi utama (untuk testing file ini saja)
if __name__ == '__main__':
    log_path = "logs/auth_sample.log"
    raw_logs = read_log_file(log_path)

    # Mengumpulkan semua log yang berhasil diparsing
    list_parsed = []
    for line in raw_logs:
        result = parse_ssh_log(line)
        if result:
            list_parsed.append(result)

    print("Menganalisis potensi serangan...")
    findings = detect_brute_force(list_parsed, threshold=3)

    print("-" * 30)
    
    if findings:
        print("[!] ALERT DITEMUKAN [!]")
        for ip, pesan in findings.items():
            print(f"IP: {ip} -> {pesan}")
    else:
        print("[+] Sistem aman, tidak ada alert.")