import os
from dotenv import load_dotenv
# 1. Menggunakan modul AI
from google import genai

def setup_ai_client():
    """Fungsi memuat API key dan menyiapkan Client AI versi baru."""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("[ERROR] API Key tidak ditemukan. Cek file .env kamu!")
        return None
        
    try:
        # 2. Sintaks baru: Membuat 'Client' untuk koneksi ke server
        client = genai.Client(api_key=api_key)
        return client
    except Exception as e:
        print(f"[ERROR] Gagal inisialisasi Client AI: {e}")
        return None

def analyze_threat_with_ai(client, alert_data: str) -> str:
    """Mengirim data ancaman ke AI menggunakan sintaks SDK terbaru."""
    prompt = f"""
    Kamu adalah Senior Cybersecurity Analyst (Blue Team).
    Tolong analisis log keamanan berikut dan berikan laporan dengan format:
    1. Tingkat Keparahan (Low/Medium/High/Critical)
    2. Penjelasan Singkat (Apa yang sedang terjadi?)
    3. Rekomendasi Mitigasi (Berikan 2 langkah konkret)
    
    Data Serangan:
    {alert_data}
    """
    
    try:
        print("[*] Mengirim data ke AI untuk dianalisis... (mohon tunggu)")
        
        # 3. Sintaks baru: generate_content dipanggil langsung dari client.models
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"[ERROR] Gagal menghubungi AI: {e}"

# Blok eksekusi utama
if __name__ == "__main__":
    ai_client = setup_ai_client()
    
    if ai_client:
        contoh_alert = "IP: 192.168.1.50 -> Terdeteksi Brute Force: 3x gagal login ke layanan SSH."
        hasil = analyze_threat_with_ai(ai_client, contoh_alert)
        
        print("\n=== HASIL ANALISIS AI ===")
        print(hasil)