import time
import requests
import pandas as pd
from core.config import RAPIDAPI_KEY

RAPID_HOST = "breachdirectory.p.rapidapi.com"

def _mask(email: str) -> str:
    # Maskeleme: j***e@gmail.com gibi
    try:
        user, dom = email.split("@", 1)
        if len(user) <= 2:
            masked_user = user[0] + "*" * max(0, len(user) - 1)
        else:
            masked_user = user[0] + "*" * (len(user) - 2) + user[-1]
        return masked_user + "@" + dom
    except Exception:
        return "***"

def check_email(email: str) -> dict:
    if not RAPIDAPI_KEY:
        return {"email": email, "email_masked": _mask(email), "breaches": None, "count": None, "error": "No API key"}
    url = f"https://{RAPID_HOST}/?func=auto&term={email}"
    headers = {"X-RapidAPI-Key": RAPIDAPI_KEY, "X-RapidAPI-Host": RAPID_HOST}
    r = requests.get(url, headers=headers, timeout=20)
    if r.status_code != 200:
        return {"email": email, "email_masked": _mask(email), "breaches": None, "count": None, "error": f"HTTP {r.status_code}"}
    data = r.json()
    if "result" in data and data["result"]:
        sources = [x.get("source", "Onbekend") for x in data["result"]]
        result = {"email": email, "email_masked": _mask(email), "breaches": ", ".join(sources), "count": len(sources), "error": None}
    else:
        result = {"email": email, "email_masked": _mask(email), "breaches": "Geen gevonden", "count": 0, "error": None}
    time.sleep(0.4)
    return result

def get_email_report(emails: list[str]) -> pd.DataFrame:
    return pd.DataFrame([check_email(e) for e in emails])
