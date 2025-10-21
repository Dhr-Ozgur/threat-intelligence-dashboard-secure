import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
RAPID_KEY = os.getenv("RAPIDAPI_KEY")
RAPID_HOST = "breachdirectory.p.rapidapi.com"


def _mask(email: str) -> str:
    try:
        user, dom = email.split("@", 1)
    except ValueError:
        return "***"
    if len(user) <= 2:
        masked_user = user[0] + "*" * max(0, len(user) - 1)
    else:
        masked_user = user[0] + "*" * (len(user) - 2) + user[-1]
    return f"{masked_user}@{dom}"


def check_email(email: str) -> dict:
    if not RAPID_KEY:
        return {"email": email, "email_masked": _mask(email), "breaches": None, "count": None, "error": "Missing RAPIDAPI_KEY"}
    url = f"https://{RAPID_HOST}/?func=auto&term={email}"
    headers = {"X-RapidAPI-Key": RAPID_KEY, "X-RapidAPI-Host": RAPID_HOST}
    r = requests.get(url, headers=headers, timeout=30)
    if r.status_code != 200:
        return {"email": email, "email_masked": _mask(email), "breaches": None, "count": None, "error": f"HTTP {r.status_code}"}
    data = r.json()
    items = data.get("result", []) or []
    sources = [x.get("source", "Unknown") for x in items]
    time.sleep(0.35)
    return {
        "email": email,
        "email_masked": _mask(email),
        "breaches": ", ".join(sources) if sources else "None found",
        "count": len(sources),
        "error": None,
    }


def get_email_report(emails: list[str]) -> pd.DataFrame:
    rows = [check_email(e.strip()) for e in emails if e.strip()]
    df = pd.DataFrame(rows)
    if not df.empty:
        df["source"] = "email"
    return df
