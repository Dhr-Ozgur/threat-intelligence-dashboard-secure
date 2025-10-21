from fastapi import FastAPI
from backend.services.abuseipdb import get_ip_report
from backend.services.virustotal import get_domain_report
from backend.services.breachdirectory import get_email_report
from backend.database import save_result, get_all_results
from reports.generator import generate_pdf
from fastapi.responses import FileResponse
import pandas as pd
import os

app = FastAPI(title="Threat Intelligence Report API")

@app.get("/")
def root():
    return {"status": "ok", "message": "Threat Intelligence Backend Running"}

@app.post("/analyze/")
def analyze(data: dict):
    ips = data.get("ips", [])
    domains = data.get("domains", [])
    emails = data.get("emails", [])
    results = {}

    if ips:
        results["ip"] = get_ip_report(ips)
    if domains:
        results["domain"] = get_domain_report(domains)
    if emails:
        results["email"] = get_email_report(emails)

    # Save results to SQLite
    save_result(results)
    return results

@app.get("/results")
def get_results():
    return get_all_results()

@app.get("/export/pdf")
def export_pdf():
    df_all = get_all_results(as_df=True)
    path = generate_pdf(df_all)
    return FileResponse(path, filename="threat_report.pdf", media_type="application/pdf")
