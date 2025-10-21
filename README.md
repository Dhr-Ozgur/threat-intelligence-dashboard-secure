# 🧠 Threat Intelligence Dashboard - Secure Edition

Een veilige, modulaire Streamlit-applicatie voor het analyseren van IP’s, domeinen en e-mails via OSINT-API’s.

## 🔐 Security
- Geen hardcoded API-sleutels
- Environment variables (.env / GitHub Secrets)
- Logging met RotatingFileHandler
- Rate limiting + foutafhandeling
- CSV-export met gemaskeerde e-mails

## 🚀 Snel starten (Codespaces)
1. Repository openen → **Code → Codespaces → Create codespace on main**
2. Terminal:
   ```bash
   pip install -r requirements.txt
   streamlit run src/app.py
---

## 📊 Power BI Integration
The app automatically generates a `powerbi_export.csv` file.
You can import this file into Power BI:
1. Open Power BI Desktop
2. Select **Get Data → Text/CSV**
3. Load `powerbi_export.csv`
4. Visualize threat intelligence data interactively

---

## 🧾 PDF Reports
Each request also produces a professional PDF summary located in `/reports/threat_report.pdf`.
The report includes:
- Input metadata
- Timestamp
- Structured field-value table
