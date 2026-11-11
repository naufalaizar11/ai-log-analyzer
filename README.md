# 🛡️ AI-Powered Automated Log Analyzer

Sebuah perangkat CLI (*Command Line Interface*) berbasis Python yang dirancang untuk membantu tim **SOC (Security Operations Center) / Blue Team** dalam mengotomatisasi analisis log keamanan. 

Program ini dapat membaca file log (seperti log SSH), mendeteksi anomali atau pola serangan (*Brute Force*), dan secara otomatis meminta **AI (Google Gemini)** untuk menganalisis ancaman tersebut serta memberikan rekomendasi mitigasi.

---

## ✨ Fitur Utama
- 🔍 **Log Parsing:** Mengekstrak informasi penting (Status, Username, IP Address) dari baris log mentah menggunakan Regular Expression (Regex).
- 🚨 **Threat Detection:** Mendeteksi serangan *Brute Force* berbasis *threshold* (ambang batas kegagalan login).
- 🤖 **AI Integration:** Terintegrasi dengan Google Gemini API (`google-genai` SDK) untuk memberikan konteks serangan dan langkah penanganan cerdas.
- 📄 **Automated Reporting:** Menghasilkan laporan insiden secara otomatis dalam format file Markdown (`.md`).

---

## 🛠️ Prasyarat (Prerequisites)
Sebelum menjalankan program ini, pastikan sistem kamu memiliki:
- **OS:** Linux (disarankan Ubuntu) atau Windows/macOS.
- **Python:** Versi 3.8 atau lebih baru.
- **API Key:** Akun Google AI Studio (untuk Gemini API Key).

---

## 🚀 Cara Instalasi

1. **Clone Repositori ini**
   ```bash
   git clone [https://github.com/username-kamu/ai-log-analyzer.git](https://github.com/username-kamu/ai-log-analyzer.git)
   cd ai-log-analyzer
