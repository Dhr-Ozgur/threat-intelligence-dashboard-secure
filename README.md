🧠 Threat Intelligence Dashboard — Secure Edition

A professional cybersecurity intelligence dashboard that analyzes IPs, domains, and emails through trusted OSINT APIs.
It generates clear analytics, Power BI–ready CSVs, and detailed PDF reports — all while keeping API keys secure.

🎯 Overview

Threat Intelligence Dashboard (Secure Edition) is built for cybersecurity students, analysts, and blue teams.
It integrates trusted data sources and ensures privacy by masking sensitive information.

Capabilities:

🔍 IP reputation & abuse confidence lookup (AbuseIPDB)

🌐 Domain threat classification (VirusTotal)

📧 Email breach analysis (BreachDirectory API)

📊 Power BI–ready CSV export with risk scores

🧾 Secure PDF report generation

🔐 Key protection via .env or GitHub Secrets

⚙️ Features
Category	Description
🧩 IP Analysis	Retrieve abuse score, ISP, and geolocation
🌐 Domain Analysis	Detect malicious or suspicious domains
📧 Email Breach	Query leaked emails securely
📊 Export System	Combine all results into one dataset
🧾 PDF Reports	Visual summaries with charts & timestamps
🔐 Secure Setup	Environment variables only
🧱 Data Privacy	Email masking and anonymized outputs
🗂️ Project Structure
threat-intelligence-dashboard-secure/
│
├── backend/
│   ├── main.py
│   ├── report_builder.py
│   └── services/
│
├── frontend/
│   ├── app.py
│   └── assets/banner.png
│
├── reports/
│   └── threat_report.pdf
│
├── .env.example
├── requirements.txt
└── README.md

🔐 Environment Variables
Variable	Description
ABUSEIPDB_KEY	AbuseIPDB API key
VT_KEY	VirusTotal API key
RAPIDAPI_KEY	BreachDirectory API key

Example .env file:

ABUSEIPDB_KEY=your_abuseipdb_key
VT_KEY=your_virustotal_key
RAPIDAPI_KEY=your_rapidapi_key


💡 Security Tip: Never commit .env files.
Add secrets under GitHub → Settings → Secrets → Codespaces for automatic injection.

🚀 How to Run
1️⃣ Create Environment
python3 -m venv .venv
source .venv/bin/activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Backend
uvicorn backend.main:app --reload

4️⃣ Run Frontend
streamlit run frontend/app.py


Now open the Streamlit dashboard, enter your IPs/domains/emails, and analyze.
You can export results as CSV or PDF instantly.

📄 PDF Report

The generated PDF includes:

Abuse confidence score charts

Domain maliciousness breakdown

Email breach counts (masked addresses)

Combined risk graph

Timestamp and dashboard logo

📁 Output location:

reports/threat_report.pdf

📊 Power BI Integration

To visualize risk analytics in Power BI:

Open Power BI → Get Data → Text/CSV

Select data/combined_report.csv

Use columns:

ip_risk

domain_risk

email_risk

exported_at

Create a Clustered Column Chart or Pie Chart

🧱 Security Checklist

✅ .env excluded from repository

✅ No hardcoded keys

✅ Masked personal data

✅ Encrypted communications

✅ Rate-limited requests

🧩 Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	FastAPI
Data Processing	Pandas
Visualization	Plotly / Matplotlib
PDF Engine	ReportLab
APIs	AbuseIPDB · VirusTotal · BreachDirectory
🧾 License

MIT License © 2025
Developed by Dhr-Ozgur

🏁 Version 1.0 — Secure Edition

Includes:

IP / Domain / Email threat intelligence

Power BI export

PDF reporting

Secure key handling

Streamlit + FastAPI integration
