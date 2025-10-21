import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
VT_KEY = os.getenv("VT_KEY")
VT_URL = "https://www.virustotal.com/api/v3/domains/"


def check_domain(domain: str) -> dict:
    if not VT_KEY:
        return {"domain": domain, "harmless": None, "malicious": None, "suspicious": None, "undetected": None, "error": "Missing VT_KEY"}
    headers = {"x-apikey": VT_KEY}
    r = requests.get(VT_URL + domain, headers=headers, timeout=20)
    if r.status_code != 200:
        return {"domain": domain, "harmless": None, "malicious": None, "suspicious": None, "undetected": None, "error": f"HTTP {r.status_code}"}
    stats = r.json().get("data", {}).get("attributes", {}).get("last_analysis_stats", {}) or {}
    time.sleep(0.35)
    return {
        "domain": domain,
        "harmless": stats.get("harmless", 0),
        "malicious": stats.get("malicious", 0),
        "suspicious": stats.get("suspicious", 0),
        "undetected": stats.get("undetected", 0),
        "error": None,
    }


def get_domain_report(domains: list[str]) -> pd.DataFrame:
    rows = [check_domain(d.strip()) for d in domains if d.strip()]
    df = pd.DataFrame(rows)
    if not df.empty:
        df["source"] = "domain"
    return df
