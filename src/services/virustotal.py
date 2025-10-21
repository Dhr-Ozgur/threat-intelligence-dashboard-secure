import time
import requests
import pandas as pd
from core.config import VT_KEY

VT_URL = "https://www.virustotal.com/api/v3/domains/"

def check_domain(domain: str) -> dict:
    if not VT_KEY:
        return {"domain": domain, "harmless": None, "malicious": None, "suspicious": None, "undetected": None, "error": "No API key"}
    headers = {"x-apikey": VT_KEY}
    r = requests.get(VT_URL + domain, headers=headers, timeout=15)
    if r.status_code != 200:
        return {"domain": domain, "error": f"HTTP {r.status_code}"}
    stats = r.json().get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
    time.sleep(0.4)
    return {
        "domain": domain,
        "harmless": stats.get("harmless", 0),
        "malicious": stats.get("malicious", 0),
        "suspicious": stats.get("suspicious", 0),
        "undetected": stats.get("undetected", 0),
        "error": None
    }

def get_domain_report(domains: list[str]) -> pd.DataFrame:
    return pd.DataFrame([check_domain(d) for d in domains])
