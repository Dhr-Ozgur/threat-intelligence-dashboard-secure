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
