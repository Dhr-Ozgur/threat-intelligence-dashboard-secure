import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
ABUSE_KEY = os.getenv("ABUSEIPDB_KEY")
ABUSE_URL = "https://api.abuseipdb.com/api/v2/check"


def check_ip(ip: str) -> dict:
    if not ABUSE_KEY:
        return {"ip": ip, "country": None, "isp": None, "abuseScore": None, "error": "Missing ABUSEIPDB_KEY"}
    headers = {"Key": ABUSE_KEY, "Accept": "application/json"}
    params = {"ipAddress": ip, "maxAgeInDays": 90}
    r = requests.get(ABUSE_URL, headers=headers, params=params, timeout=20)
    if r.status_code != 200:
        return {"ip": ip, "country": None, "isp": None, "abuseScore": None, "error": f"HTTP {r.status_code}"}
    data = r.json().get("data", {})
    time.sleep(0.35)  # gentle rate-limit
    return {
        "ip": ip,
        "country": data.get("countryCode"),
        "isp": data.get("isp"),
        "abuseScore": data.get("abuseConfidenceScore"),
        "error": None,
    }


def get_ip_report(ips: list[str]) -> pd.DataFrame:
    rows = [check_ip(ip.strip()) for ip in ips if ip.strip()]
    df = pd.DataFrame(rows)
    if not df.empty:
        df["source"] = "ip"
    return df
