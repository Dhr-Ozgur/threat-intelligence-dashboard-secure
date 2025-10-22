🧠 Threat Intelligence Dashboard — Secure Edition

🎯 Overview

Threat Intelligence Dashboard is a security analysis tool for evaluating IP addresses, domains, and email addresses using open-source intelligence (OSINT).
It collects data from multiple APIs, calculates risk scores, and generates professional visual reports (📊 CSV + 📑 PDF).

Designed for security analysts, SOC teams, and researchers who need a quick overview of potential threats.

⚙️ Key Features
Feature	Description
🔍 IP Analysis	Uses AbuseIPDB API to retrieve abuse confidence and geolocation data
🌐 Domain Analysis	Queries VirusTotal API for malicious/suspicious domain indicators
📧 Email Breach Analysis	Checks exposed credentials via BreachDirectory (RapidAPI)
📦 CSV Export	Power BI–ready CSV file with risk scores
🧾 PDF Report	Corporate-style PDF with charts, tables, logo, and risk summary
🔐 Secure Keys	API keys loaded from .env or GitHub Secrets
🕵️ Data Privacy	Automatically masks sensitive email addresses
🗂️ Project Structure
threat-intelligence-dashboard-secure/
│
├── backend/
│   ├── main.py                # FastAPI backend service
│   ├── report_builder.py      # PDF report generator
│   └── services/              # API integrations (AbuseIPDB, VirusTotal, BreachDirectory)
│
├── frontend/
│   ├── app.py                 # Streamlit frontend
│   └── assets/logo.png        # Optional logo for PDF header
│
├── reports/
│   └── threat_report.pdf      # Generated reports
│
├── .env.example               # Environment variable template
├── requirements.txt           # Python dependencies
└── README.md

🔐 Environment Variables
Variable	Description
ABUSEIPDB_KEY	AbuseIPDB API key

VT_KEY	VirusTotal API key

RAPIDAPI_KEY	BreachDirectory API key

💡 For GitHub Codespaces:
Go to Settings → Secrets → Codespaces → New Secret and add each key.

🚀 Running the Project
1️⃣ Backend (FastAPI)
source .venv/bin/activate
uvicorn backend.main:app --reload

2️⃣ Frontend (Streamlit)
source .venv/bin/activate
streamlit run frontend/app.py

🔗 Usage

Enter an IP, domain, or email

Click Analyze to fetch OSINT data

Use Generate PDF Report or Export CSV to get visual outputs

📄 PDF Report Example

Each report includes:

IP Risk Score Distribution

Domain Threat Graph

Email Breach Table

Overall Risk Pie Chart (%)

Timestamp and optional logo

📁 Sample file: reports/threat_report.pdf

📊 Power BI Integration

Import data/combined_report.csv into Power BI →
Visualize risk metrics using the Clustered Column Chart for interactive threat dashboards.

🧱 Security Checklist

☑ .env is excluded from git
☑ All API keys managed securely (env/secrets)
☑ Sensitive data masked in logs
☑ Emails automatically anonymized
☑ API rate limiting enabled for safe OSINT queries

📦 Setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

🧩 Technologies
Layer	Technology
Frontend	Streamlit
Backend	FastAPI
Data Processing	Pandas
Visualization	Matplotlib / Plotly
PDF Generator	ReportLab
OSINT APIs	AbuseIPDB · VirusTotal · BreachDirectory
🧾 License

MIT License © 2025
Developed by Dhr-Ozgur

🏁 Release Recommendation

When everything is stable:

Go to your repo → Releases → Create new release

Tag it as v1.0 Secure Edition

Attach:

threat_report.pdf (sample output)

combined_report.csv

That will make your project look professional and versioned properly.
