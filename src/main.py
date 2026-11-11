from log_parser import read_log_file, parse_ssh_log, detect_brute_force
from ai_analyzer import setup_ai_client, analyze_threat_with_ai
from datetime import datetime 

def main():
    print("=== 🛡️ AI-POWERED LOG ANALYZER 🛡️ ===")
    
    raw_logs = read_log_file("logs/auth_sample.log")
    
    parsed_logs = []
    for line in raw_logs:
        hasil_parsing = parse_ssh_log(line)
        if hasil_parsing:
            parsed_logs.append(hasil_parsing)
            
    alerts = detect_brute_force(parsed_logs, threshold=3)
    
    if alerts:
        print(f"[*] Ditemukan {len(alerts)} peringatan! Menghubungi AI...")
        ai_client = setup_ai_client()
        
        if ai_client:
            # Kita siapkan string kosong untuk menampung seluruh teks laporan
            teks_laporan = f"# Laporan Insiden Keamanan\nTanggal: {datetime.now()}\n\n"
            
            for ip, pesan_alert in alerts.items():
                print(f"\n[!] ALERT: {pesan_alert}")
                
                hasil_ai = analyze_threat_with_ai(ai_client, pesan_alert)
                print(hasil_ai)
                
                # Gabungkan hasil AI ke dalam string teks_laporan
                teks_laporan += f"## Temuan pada IP: {ip}\n{hasil_ai}\n\n"
            
            
            # 'w' artinya write (menulis).
            with open("laporan_insiden.md", "w") as file_laporan:
                file_laporan.write(teks_laporan)
                
            print("\n[+] Laporan lengkap telah disimpan ke file 'laporan_insiden.md'")
    else:
        print("[+] Sistem aman. Tidak ada ancaman yang melewati batas threshold.")

if __name__ == "__main__":
    main()