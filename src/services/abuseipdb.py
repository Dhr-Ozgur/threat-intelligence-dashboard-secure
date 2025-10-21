import time
import requests
import pandas as pd
from core.config import ABUSEIPDB_KEY

ABUSE_URL = "https://api.abuseipdb.com/api/v2/check"

def check_ip(ip: str) -> dict:
    if not ABUSEIPDB_KEY:
        return {"ip": ip, "abuseConfidenceScore": None, "countryCode": None, "error": "No API key"}
    headers = {'Key': ABUSEIPDB_KEY, 'Accept': 'application/json'}
    params = {'ipAddress': ip, 'maxAgeInDays': 90}
    r = requests.get(ABUSE_URL, headers=headers, params=params, timeout=15)
    if r.status_code != 200:
        return {"ip": ip, "error": f"HTTP {r.status_code}"}
    data = r.json().get("data", {})
    time.sleep(0.4)
    return {
        "ip": ip,
        "abuseConfidenceScore": data.get("abuseConfidenceScore"),
        "countryCode": data.get("countryCode"),
        "isp": data.get("isp"),
        "domain": data.get("domain"),
        "error": None
    }

def get_ip_report(ips: list[str]) -> pd.DataFrame:
    return pd.DataFrame([check_ip(ip) for ip in ips])
