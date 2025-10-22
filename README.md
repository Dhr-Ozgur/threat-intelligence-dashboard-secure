# 🧠 Threat Intelligence Dashboard — Secure Edition

Profesyonel bir siber güvenlik istihbarat gösterge paneli. IP, alan adı ve e-posta analizlerini güvenilir OSINT API’ler ile yapar. Güvenli API anahtarı yönetimi ile ayrıntılı raporlar ve Power BI uyumlu CSV dosyaları oluşturur.

---

## 🎯 Genel Bakış

Siber güvenlik öğrencileri, analistleri ve mavi takım kullanıcıları için geliştirilmiştir.  
Veri kaynakları güvenilir olup gizlilik için hassas bilgiler maskelenir.

---

## 🚀 Özellikler

- IP itibarı ve kötüye kullanım puanı (AbuseIPDB)  
- Alan adı tehdit sınıflandırması (VirusTotal)  
- E-posta sızıntısı sorgulama (BreachDirectory)  
- Power BI uyumlu CSV dışa aktarımı  
- Güvenli PDF raporu oluşturma  
- API anahtarları `.env` veya GitHub Secrets ile korunur

---

## ⚙️ Teknik Bilgiler

| Kategori | Açıklama |
|----------|----------|
| IP Analizi | ISP, konum ve kötüye kullanım puanı alın |
| Alan Adı | Şüpheli veya zararlı alanlar tespit edilir |
| E-posta | Maskelenmiş e-posta sızıntısı sorgu sistemi |
| Dışa Aktarım | Veriler tek CSV’de birleştirilir |
| PDF Raporu | Grafik ve zaman damgaları ile özetler |
| Güvenlik | Çevresel değişkenlerle API anahtarları gizlenir |

---

## 📁 Proje Yapısı

threat-intelligence-dashboard-secure/
├── backend/
│ ├── main.py
│ ├── report_builder.py
│ └── services/
├── frontend/
│ ├── app.py
│ └── assets/banner.png
├── reports/
│ └── threat_report.pdf
├── .env.example
├── requirements.txt
└── README.md

text

---

## 🔐 Ortam Değişkenleri

| Değişken | Açıklama |
|----------|----------|
| ABUSEIPDB_KEY | AbuseIPDB API anahtarı |
| VT_KEY | VirusTotal API anahtarı |
| RAPIDAPI_KEY | BreachDirectory API anahtarı |

**Örnek `.env`:**

ABUSEIPDB_KEY=your_abuseipdb_key
VT_KEY=your_virustotal_key
RAPIDAPI_KEY=your_rapidapi_key

text

> `.env` dosyalarını versiyon kontrolüne eklemeyin; GitHub Secrets’i kullanın.

---

## 🚀 Kurulum ve Çalıştırma

Ortam oluşturma
python3 -m venv .venv
source .venv/bin/activate

Bağımlılıkları yükle
pip install -r requirements.txt

Backend başlat
uvicorn backend.main:app --reload

Frontend başlat
streamlit run frontend/app.py

text

---

## 📄 PDF Rapor Özellikleri

- Kötüye kullanım skorları grafikleri  
- Alan adı tehdit analizi  
- E-posta sızıntı sayıları (maskelenmiş)  
- Birleşik risk grafiği  
- Zaman damgası ve logo  

**Dosya yolu:** `reports/threat_report.pdf`

---

## 📊 Power BI Entegrasyonu

1. Power BI aç → Veri al → Metin/CSV  
2. `data/combined_report.csv` dosyasını seç  
3. `ip_risk`, `domain_risk`, `email_risk`, `exported_at` sütunlarını kullan  
4. Grafikler oluştur (Çubuk, Pasta vb.)

---

## 🧱 Güvenlik Kontrol Listesi

- `.env` dosyası repo dışında  
- Sabit kodlanmış anahtar yok  
- Kişisel veriler maskelenmiş  
- Şifreli iletişim  
- İstek sınırlandırma var  

---

## 🧩 Teknoloji Yığını

| Katman | Teknoloji |
|--------|-----------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Veri İşleme | Pandas |
| Görselleştirme | Plotly / Matplotlib |
| PDF Motoru | ReportLab |
| API’ler | AbuseIPDB · VirusTotal · BreachDirectory |

---

## 🧾 Lisans

MIT License © 2025  
Geliştiren: Dhr-Ozgur

---

## 🏁 Versiyon 1.0 — Secure Edition

- IP / Alan / E-posta istihbaratı  
- Power BI dışa aktarımı  
- PDF raporlama  
- Güvenli anahtar yönetimi  
- Streamlit + FastAPI entegrasyonu
