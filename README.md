🧠 Threat Intelligence Dashboard — Secure Edition

A modern cybersecurity intelligence tool that analyzes IP addresses, domains, and email addresses using multiple OSINT APIs.
It visualizes threat data, calculates risk scores, and generates both Power BI–ready CSV files and professional PDF reports.

🎯 Overview

The Threat Intelligence Dashboard helps analysts and SOC teams collect and visualize open-source threat data.
All API keys are securely managed through environment variables (.env) or GitHub Secrets — ensuring no sensitive data appears in code or logs.

⚙️ Key Features

🔍 IP Analysis — via AbuseIPDB (abuse confidence, ISP, geolocation)

🌐 Domain Analysis — via VirusTotal (malicious / suspicious scores)

📧 Email Breach Analysis — via BreachDirectory (RapidAPI)

📊 CSV Export — Power BI–compatible with risk percentages

🧾 PDF Report — charts, tables, logo, and overall risk summary

🔐 Secure Configuration — API keys loaded from environment

🕵️ Data Privacy — emails automatically masked (e.g., j***e@gmail.com)

⚡ Rate Limiting — prevents API abuse
🚀 Running the Project
1️⃣ Create Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Backend (FastAPI)
uvicorn backend.main:app --reload

4️⃣ Run Frontend (Streamlit)
streamlit run frontend/app.py


Then open the Streamlit interface → enter IPs, domains, or emails → click Analyze
and export results via Download CSV or Generate PDF Report.

📄 PDF Report

Each generated report includes:

IP risk distribution (bar chart)

Domain malicious/suspicious metrics

Email breach results (masked addresses)

Overall risk pie chart (%)

Timestamp and logo header

Output file: reports/threat_report.pdf

📊 Power BI Integration

Open Power BI → Get Data → Text/CSV

Select data/combined_report.csv

Visualize fields such as:

ip_risk

domain_risk

email_risk

exported_at

Create Clustered Column Chart or Pie Chart visuals for threat comparison.

🧱 Security Checklist

✅ .env file excluded from repository

✅ API keys stored securely (not hardcoded)

✅ Logs contain no personal data

✅ Email addresses masked in output

✅ Rate limiting protects API calls

🧩 Technology Stack
Layer	Technology
Frontend	Streamlit
Backend	FastAPI
Data	Pandas
Visualization	Matplotlib / Plotly
PDF Engine	ReportLab
APIs	AbuseIPDB · VirusTotal · BreachDirectory
🧾 License

MIT License © 2025
Developed by Dhr-Ozgur

🏁 Release

When the project is stable:

Go to Releases → New Release

Tag it as v1.0 Secure Edition

Attach:

reports/threat_report.pdf

data/combined_report.csv

Example description:

🚀 Initial release — Threat Intelligence Dashboard (Secure Edition)
Includes IP, Domain, and Email analysis + PDF and Power BI exports.

