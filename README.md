🧠 Threat Intelligence Dashboard — Secure Edition
A professional dashboard for cybersecurity analytics. Analyze IPs, domains, and emails via trusted OSINT APIs. Instantly generate Power BI–ready CSVs and detailed PDF reports — always with secure API key handling.

🎯 Overview
Threat Intelligence Dashboard (Secure Edition) is for cybersecurity students, analysts, and blue teams.
It aggregates trusted sources and keeps your data secure and private.

🚀 Capabilities
🔍 IP Reputation & Abuse Score (AbuseIPDB)

🌐 Domain Threat Classification (VirusTotal)

📧 Email Breach Search (BreachDirectory)

📊 Power BI–Ready CSV Export

🧾 Secure PDF Report Generation

🔐 API Key Protection via .env or GitHub Secrets

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
text
threat-intelligence-dashboard-secure/
├── backend/
│   ├── main.py
│   ├── report_builder.py
│   └── services/
├── frontend/
│   ├── app.py
│   └── assets/banner.png
├── reports/
│   └── threat_report.pdf
├── .env.example
├── requirements.txt
└── README.md
🔐 Environment Variables
Variable	Description
ABUSEIPDB_KEY	AbuseIPDB API key
VT_KEY	VirusTotal API key
RAPIDAPI_KEY	BreachDirectory API key
Example .env file:

text
ABUSEIPDB_KEY=your_abuseipdb_key
VT_KEY=your_virustotal_key
RAPIDAPI_KEY=your_rapidapi_key
💡 Never commit .env files.
Add secrets under GitHub → Settings → Secrets → Codespaces for automatic injection.

🚀 How to Run
Create Environment

bash
python3 -m venv .venv
source .venv/bin/activate
Install Dependencies

bash
pip install -r requirements.txt
Run Backend

bash
uvicorn backend.main:app --reload
Run Frontend

bash
streamlit run frontend/app.py
Open your dashboard, enter IPs/domains/emails, and analyze instantly.
Export results as CSV or PDF.

📄 PDF Report
Abuse confidence score charts

Domain threat details

Email breach counts (masked)

Combined risk graph

Timestamp & logo

Output: reports/threat_report.pdf

📊 Power BI Integration
To visualize in Power BI:

Open Power BI → Get Data → Text/CSV

Choose data/combined_report.csv

Use columns: ip_risk, domain_risk, email_risk, exported_at

Create a Clustered Column or Pie Chart

🧱 Security Checklist
✅ .env excluded
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

IP / Domain / Email intelligence

Power BI export

PDF reporting

Secure key handling

Streamlit + FastAPI integration
