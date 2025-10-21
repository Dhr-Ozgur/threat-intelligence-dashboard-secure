import requests
import pandas as pd
import os
import time
from dotenv import load_dotenv
load_dotenv()

RAPID_KEY = os.getenv("RAPIDAPI_KEY")
RAPID_HOST = "breachdirectory.p.rapidapi.com"

def get_email_report(emails):
    rows = []
    if not RAPID_KEY:
        return pd.DataFrame([{"email": "Missing Key"}])
    headers = {"X-RapidAPI-Key": RAPID_KEY, "X-RapidAPI-Host": RAPID_HOST}
    for e in emails:
        try:
            r = requests.get(f"https://{RAPID_HOST}/?func=auto&term={e}", headers=headers)
            data = r.json()
            count = len(data.get("result", []))
            rows.append({
                "email": e,
                "breaches": ", ".join([x.get("source", "Unknown") for x in data.get("result", [])]),
                "count": count
            })
            time.sleep(0.4)
        except Exception as ex:
            rows.append({"email": e, "error": str(ex)})
    return pd.DataFrame(rows)
