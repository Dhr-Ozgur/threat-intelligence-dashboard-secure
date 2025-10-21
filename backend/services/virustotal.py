import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv
load_dotenv()

VT_KEY = os.getenv("VT_KEY")
VT_URL = "https://www.virustotal.com/api/v3/domains/"

def get_domain_report(domains):
    rows = []
    if not VT_KEY:
        return pd.DataFrame([{"domain": "Missing Key"}])
    headers = {"x-apikey": VT_KEY}
    for d in domains:
        try:
            r = requests.get(VT_URL + d, headers=headers, timeout=10)
            stats = r.json().get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
            rows.append({
                "domain": d,
                "harmless": stats.get("harmless", 0),
                "malicious": stats.get("malicious", 0),
                "suspicious": stats.get("suspicious", 0)
            })
            time.sleep(0.4)
        except Exception as e:
            rows.append({"domain": d, "error": str(e)})
    return pd.DataFrame(rows)
