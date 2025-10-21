import os
import time
import pandas as pd
import streamlit as st
import plotly.express as px

from core.config import ABUSEIPDB_KEY, VT_KEY, RAPIDAPI_KEY
from core.logger import logger
from services.abuseipdb import get_ip_report
from services.virustotal import get_domain_report
from services.breachdirectory import get_email_report
from exports.export_csv import export_combined_csv

st.set_page_config(page_title="Threat Intelligence Dashboard – Secure", layout="wide")
st.title("🧠 Threat Intelligence Dashboard – Secure Edition")

missing = []
if not ABUSEIPDB_KEY: missing.append("ABUSEIPDB_KEY")
if not VT_KEY: missing.append("VT_KEY")
if not RAPIDAPI_KEY: missing.append("RAPIDAPI_KEY")
if missing:
    st.warning("⚠️ Ontbrekende env-variabelen: " + ", ".join(missing) + ". "
               "Gebruik `.env` lokaal of Codespaces Secrets in GitHub.")

st.sidebar.header("🔍 Analyseer IP-adressen")
ip_input = st.sidebar.text_area("Voer IP's in (één per regel):", key="ip_input")
if st.sidebar.button("Analyseer IP’s"):
    ips = [i.strip() for i in ip_input.splitlines() if i.strip()]
    if ips:
        with st.spinner("IP-rapport ophalen..."):
            df_ip = get_ip_report(ips)
            st.subheader("IP Resultaten")
            st.dataframe(df_ip)
            if not df_ip.empty:
                fig = px.bar(df_ip, x="ip", y="abuseConfidenceScore",
                             color="countryCode", title="Abuse Confidence Score per IP")
                st.plotly_chart(fig)
else:
    df_ip = pd.DataFrame()

st.sidebar.header("🌐 Analyseer Domeinen")
domain_input = st.sidebar.text_area("Voer domeinnamen in (één per regel):", key="domain_input")
if st.sidebar.button("Analyseer Domeinen"):
    domains = [d.strip() for d in domain_input.splitlines() if d.strip()]
    if domains:
        with st.spinner("Domein-rapport ophalen..."):
            df_dom = get_domain_report(domains)
            st.subheader("Domein Resultaten")
            st.dataframe(df_dom)
            if not df_dom.empty:
                fig2 = px.bar(df_dom, x="domain", y="malicious", color="suspicious")
                st.plotly_chart(fig2)
else:
    df_dom = pd.DataFrame()

st.sidebar.header("📧 Controleer E-mailadressen")
email_input = st.sidebar.text_area("Voer e-mailadressen in (één per regel):", key="email_input")
if st.sidebar.button("Controleer E-mails"):
    emails = [e.strip() for e in email_input.splitlines() if e.strip()]
    if emails:
        with st.spinner("E-mailbreaches ophalen..."):
            df_em = get_email_report(emails)
            st.subheader("E-mail Breach Resultaten")
            st.dataframe(df_em)
            if not df_em.empty:
                fig3 = px.bar(df_em, x="email_masked", y="count", color="count")
                st.plotly_chart(fig3)
else:
    df_em = pd.DataFrame()

st.sidebar.header("💾 Export & Download")
if st.sidebar.button("📦 Export Combined CSV (IP + Domain + Email)"):
    csv_bytes = export_combined_csv(df_ip, df_dom, df_em)
    st.download_button("📥 Download combined_report.csv", csv_bytes, "combined_report.csv", "text/csv")
