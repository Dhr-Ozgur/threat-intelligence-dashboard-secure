# 🧠 Threat Intelligence Dashboard - Secure Edition

A cybersecurity dashboard analyzing IPs, domains, and emails via trusted OSINT APIs.  
Generates clear reports in CSV (Power BI-ready) and PDF formats. Ensures API key security.

---

## Overview

Designed for cybersecurity students, analysts, and blue teams.  
Integrates multiple data sources, masking sensitive data for privacy.

---

## Features

- IP reputation & abuse score lookup (AbuseIPDB)  
- Domain threat classification (VirusTotal)  
- Email breach analysis (BreachDirectory API)  
- CSV export for Power BI  
- Secure PDF report generation  
- API keys protected via `.env` or GitHub Secrets  

---

## Project Structure

- `backend/`: Python backend with FastAPI  
- `frontend/`: Streamlit UI app  
- `reports/`: Generated PDF reports  
- `.env.example`: Environment variables template  
- `requirements.txt`: Python dependencies  

---

## Environment Variables

| Variable        | Purpose               |
|-----------------|-----------------------|
| ABUSEIPDB_KEY   | AbuseIPDB API key     |
| VT_KEY          | VirusTotal API key    |
| RAPIDAPI_KEY    | BreachDirectory API key|

*Use GitHub Secrets or `.env` (do not commit `.env` files).*

---

## Quick Start

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
streamlit run frontend/app.py


---

## PDF Report Details

- Abuse score charts  
- Domain threat summaries  
- Masked email breach data  
- Combined risk graphs  
- Timestamp and logo

Saved under `reports/threat_report.pdf`.

---

## Power BI Integration

In Power BI:  
- Get Data → CSV → `data/combined_report.csv`  
- Use columns: `ip_risk`, `domain_risk`, `email_risk`, `exported_at`  
- Create your favorite charts

---

## Tech Stack

- Frontend: Streamlit  
- Backend: FastAPI  
- Data: Pandas  
- Visualization: Plotly, Matplotlib  
- PDF generation: ReportLab  
- APIs: AbuseIPDB, VirusTotal, BreachDirectory

---

## License

MIT License © 2025  
Developed by Dhr-Ozgur




