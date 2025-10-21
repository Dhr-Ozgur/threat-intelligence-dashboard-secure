from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

from backend.services.abuseipdb import get_ip_report
from backend.services.virustotal import get_domain_report
from backend.services.breachdirectory import get_email_report
from backend.report_builder import build_pdf

app = FastAPI(title="Threat Intelligence Backend – Secure + Functional")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "message": "Threat Intelligence Backend Running"}


@app.post("/analyze")
def analyze(payload: dict):
    ips = payload.get("ips", []) or []
    domains = payload.get("domains", []) or []
    emails = payload.get("emails", []) or []

    df_ip = get_ip_report(ips) if ips else pd.DataFrame()
    df_dom = get_domain_report(domains) if domains else pd.DataFrame()
    df_em = get_email_report(emails) if emails else pd.DataFrame()

    return {
        "ip": df_ip.to_dict(orient="records"),
        "domain": df_dom.to_dict(orient="records"),
        "email": df_em.to_dict(orient="records"),
    }


@app.post("/export/pdf")
def export_pdf(payload: dict):
    # Recompute (stateless) so we don't keep server memory
    ips = payload.get("ips", []) or []
    domains = payload.get("domains", []) or []
    emails = payload.get("emails", []) or []

    df_ip = get_ip_report(ips) if ips else pd.DataFrame()
    df_dom = get_domain_report(domains) if domains else pd.DataFrame()
    df_em = get_email_report(emails) if emails else pd.DataFrame()

    path = build_pdf(df_ip, df_dom, df_em)
    with open(path, "rb") as f:
        pdf_bytes = f.read()
    return Response(content=pdf_bytes, media_type="application/pdf")
