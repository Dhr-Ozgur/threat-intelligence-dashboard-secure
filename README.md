🧠 Threat Intelligence Dashboard

A simple and secure dashboard for analyzing IP addresses, domains, and emails using public threat intelligence APIs.
It helps cybersecurity researchers and analysts quickly detect potential risks and export results for reporting.

🚀 Features

IP, domain, and email reputation checks

Combined analysis and CSV/PDF export

Power BI–ready datasets

Secure .env configuration for API keys

Lightweight interface with Streamlit and FastAPI

⚙️ Setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


Run the backend:

uvicorn backend.main:app --reload


Run the frontend:

streamlit run frontend/app.py

🔐 Environment Variables

Create a .env file in the root directory:

ABUSEIPDB_KEY=your_abuseipdb_key
VT_KEY=your_virustotal_key
RAPIDAPI_KEY=your_rapidapi_key

📄 Exports

reports/threat_report.pdf — formatted intelligence report

data/combined_report.csv — Power BI–ready dataset

🧩 Tech Stack

Frontend: Streamlit

Backend: FastAPI

Data: Pandas, Plotly, ReportLab

APIs: AbuseIPDB · VirusTotal · BreachDirectory

📜 License

MIT License © 2025
Developed by Dhr-Ozgur
