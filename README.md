🧠 Threat Intelligence Dashboard – Secure Edition

A 2-layer cybersecurity analytics platform that collects, analyzes, and visualizes open-source threat data.
It combines multiple OSINT sources (AbuseIPDB, VirusTotal, BreachDirectory) and delivers clear, privacy-safe intelligence reports — both interactive and exportable.

🔎 Overview

Threat Intelligence Dashboard (Secure Edition) helps security analysts and SOC teams evaluate indicators of compromise:

IPs for malicious confidence

Domains for threat classification

Emails for known breaches

The system integrates:

Streamlit frontend

FastAPI backend

Secure .env or GitHub Secrets configuration

CSV / PDF exports for reporting and Power BI

⚙️ Main Features

| Category                   | Description                                              |
| -------------------------- | -------------------------------------------------------- |
| 🧩 **IP Intelligence**     | AbuseIPDB integration – abuse confidence, ISP, country   |
| 🌐 **Domain Intelligence** | VirusTotal API – malicious/suspicious detections         |
| 📧 **Email Breach Check**  | BreachDirectory (RapidAPI) – anonymized leak info        |
| 📊 **Export & Reporting**  | Combined CSV and branded PDF report generation           |
| 🔐 **Secure Setup**        | No hardcoded keys – all via `.env` or Codespaces Secrets |
| 🧱 **Data Privacy**        | Masked emails and sanitized logs                         |

🗂️ Directory Layout

threat-intelligence-dashboard-secure/

│
├── backend/               # FastAPI backend
│   ├── main.py
│   ├── report_builder.py
│   └── services/
│
├── frontend/              # Streamlit frontend
│   ├── app.py
│   └── assets/logo.png
│
├── reports/               # Generated output
│   └── threat_report.pdf
│
├── .env.example           # Example environment variables
├── requirements.txt
└── README.md


🔐 Environment Variables

| Variable        | Purpose                        |
| --------------- | ------------------------------ |
| `ABUSEIPDB_KEY` | AbuseIPDB API key              |
| `VT_KEY`        | VirusTotal API key             |
| `RAPIDAPI_KEY`  | BreachDirectory (RapidAPI) key |

Example .env file:

ABUSEIPDB_KEY=your_abuseipdb_key
VT_KEY=your_virustotal_key
RAPIDAPI_KEY=your_rapidapi_key
Use Codespaces → Settings → Secrets → New Secret for secure cloud storage.

🚀 Running the App
1️⃣ Setup Environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

2️⃣ Launch Backend
uvicorn backend.main:app --reload

3️⃣ Launch Frontend
streamlit run frontend/app.py


Then open the Streamlit UI, enter your IPs/domains/emails, and click Analyze.
Results, charts, and exports (CSV/PDF) will appear automatically.

🧾 Output Reports
PDF

IP abuse confidence chart

Domain maliciousness breakdown

Email breach summary

Overall risk pie chart

Export timestamp and logo

Saved under: reports/threat_report.pdf

CSV (Power BI-ready)

Columns:

ip_risk, domain_risk, email_risk, exported_at

Use Power BI → Get Data → Text/CSV for dashboards.

🧱 Security Principles

✅ No API keys in code or logs

✅ .env excluded from git

✅ Masked personal data

✅ Rate-limit protection

✅ Local + Codespaces secrets supported

🧩 Tech Stack

| Layer         | Technology                               |
| ------------- | ---------------------------------------- |
| Frontend      | Streamlit                                |
| Backend       | FastAPI                                  |
| Data          | Pandas                                   |
| Visualization | Plotly / Matplotlib                      |
| PDF Engine    | ReportLab                                |
| OSINT APIs    | AbuseIPDB · VirusTotal · BreachDirectory |

🧾 License

MIT License © 2025
Developed by Dhr-Ozgur

🏁 Release Notes

Version v1.0 – Secure Edition

Integrated 3 OSINT APIs

Added Power BI export

PDF generation with risk charts

Environment-based security model




