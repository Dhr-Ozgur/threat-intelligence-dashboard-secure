# 🧠 Threat Intelligence Dashboard — Secure Edition

A modern cybersecurity intelligence tool that analyzes **IP addresses**, **domains**, and **email addresses** using OSINT APIs.  
It generates interactive visualizations and exports professional reports in both **CSV** and **PDF** formats.

---

## 🎯 Overview

**Threat Intelligence Dashboard (Secure Edition)** allows analysts and SOC teams to collect, analyze, and visualize public threat data securely.

- IP reputation lookup (AbuseIPDB)  
- Domain classification (VirusTotal)  
- Email breach check (BreachDirectory)  
- CSV export for Power BI  
- Secure PDF reporting  

---

## ⚙️ Features

| Function | Description |
|-----------|-------------|
| 🧩 IP Analysis | Abuse confidence score, ISP, and country lookup |
| 🌐 Domain Analysis | Malicious / suspicious detection statistics |
| 📧 Email Breach Check | BreachDirectory API (RapidAPI) |
| 📊 CSV Export | Power BI–ready dataset with risk scoring |
| 🧾 PDF Report | Charts, logo, timestamp, and summary table |
| 🔐 Secure Config | Environment variables / GitHub Secrets |
| 🕵️ Data Privacy | Masked emails and anonymized exports |

---

## 🗂️ Project Structure

threat-intelligence-dashboard-secure/
│
├── backend/
│ ├── main.py
│ ├── report_builder.py
│ └── services/
│
├── frontend/
│ ├── app.py
│ └── assets/logo.png
│
├── reports/
│ └── threat_report.pdf
│
├── .env.example
├── requirements.txt
└── README.md

yaml
Code kopiëren

---

## 🔐 Environment Variables

| Variable | Purpose |
|-----------|----------|
| `ABUSEIPDB_KEY` | AbuseIPDB API key |
| `VT_KEY` | VirusTotal API key |
| `RAPIDAPI_KEY` | BreachDirectory API key |

Example `.env` file:
ABUSEIPDB_KEY=your_abuseipdb_key
VT_KEY=your_virustotal_key
RAPIDAPI_KEY=your_rapidapi_key

yaml
Code kopiëren

> Use **Codespaces → Settings → Secrets → New Secret** for secure key management.

---

## 🚀 How to Run

### 1️⃣ Create and Activate Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
2️⃣ Install Dependencies
bash
Code kopiëren
pip install -r requirements.txt
3️⃣ Run Backend
bash
Code kopiëren
uvicorn backend.main:app --reload
4️⃣ Run Frontend
bash
Code kopiëren
streamlit run frontend/app.py
Then open the Streamlit UI → enter IPs/domains/emails → click Analyze
and download CSV or PDF outputs.

📄 PDF Report
Report content:

IP abuse score bar chart

Domain maliciousness overview

Email breach count chart

Overall risk summary (pie chart)

Export timestamp and logo

Output file:

bash
Code kopiëren
reports/threat_report.pdf
📊 Power BI Integration
Open Power BI → Get Data → Text/CSV

Select data/combined_report.csv

Use these fields for visuals:

ip_risk

domain_risk

email_risk

exported_at

Recommended chart: Clustered Column or Pie Chart.

🧱 Security Checklist
✅ .env excluded from commits

✅ API keys never hardcoded

✅ Masked email output

✅ Logs contain no sensitive info

✅ Rate-limiting between requests

🧩 Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	FastAPI
Data	Pandas
Visualization	Plotly / Matplotlib
PDF Engine	ReportLab
APIs	AbuseIPDB · VirusTotal · BreachDirectory

🧾 License
MIT License © 2025
Developed by Dhr-Ozgur

🏁 Release Notes
Version: v1.0 – Secure Edition
Includes:

IP, Domain, and Email analysis

Power BI–ready CSV export

PDF report generator

Secure .env configuration model
