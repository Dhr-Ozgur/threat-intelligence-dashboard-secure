import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv
load_dotenv()

ABUSE_KEY = os.getenv("ABUSEIPDB_KEY")
URL = "https://api.abuseipdb.com/api/v2/check"

def get_ip_report(ips):
    rows = []
    if not ABUSE_KEY:
        return pd.DataFrame([{"ip": "Missing Key"}])
    headers = {'Key': ABUSE_KEY, 'Accept': 'application/json'}
    for ip in ips:
        try:
            r = requests.get(URL, headers=headers, params={'ipAddress': ip}, timeout=10)
            data = r.json().get("data", {})
            rows.append({
                "ip": ip,
                "country": data.get("countryCode"),
                "isp": data.get("isp"),
                "abuseScore": data.get("abuseConfidenceScore")
            })
            time.sleep(0.4)
        except Exception as e:
            rows.append({"ip": ip, "error": str(e)})
    return pd.DataFrame(rows)
