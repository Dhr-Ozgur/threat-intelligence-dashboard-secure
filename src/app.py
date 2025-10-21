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

# ----------------------------------------------------------
# 🧠 Threat Intelligence Dashboard – Secure Edition
# ----------------------------------------------------------
st.set_page_config(page_title="Threat Intelligence Dashboard – Secure", layout="wide")
st.title("🧠 Threat Intelligence Dashboard – Secure Edition")


missing = []
if not ABUSEIPDB_KEY:
    missing.append("ABUSEIPDB_KEY")
if not VT_KEY:
    missing.append("VT_KEY")
if not RAPIDAPI_KEY:
    missing.append("RAPIDAPI_KEY")

if missing:
    st.warning("⚠️ Ontbrekende environment-variabelen: " + ", ".join(missing) + ". "
               "Gebruik `.env` lokaal of Codespaces Secrets in GitHub.")


st.sidebar.header("🔍 Analyseer IP-adressen")
ip_input = st.sidebar.text_area("Voer IP's in (één per regel):", key="ip_input")

if st.sidebar.button("Analyseer IP’s"):
    ips = [i.strip() for i in ip_input.splitlines() if i.strip()]
    if ips:
        with st.spinner("IP-rapport ophalen..."):
            try:
                df_ip = get_ip_report(ips)
                st.session_state["df_ip"] = df_ip  
                st.subheader("IP Resultaten")
                st.dataframe(df_ip, use_container_width=True)
                if not df_ip.empty:
                    fig = px.bar(df_ip, x="ip", y="abuseConfidenceScore",
                                 color="countryCode", title="Abuse Confidence Score per IP")
                    st.plotly_chart(fig, use_container_width=True)
                st.success("✅ IP-analyse voltooid.")
            except Exception as e:
                logger.exception("IP analyse fout")
                st.error(f"IP analyse mislukt: {e}")
    else:
        st.info("Geen IP’s ingevoerd.")


st.sidebar.header("🌐 Analyseer Domeinen")
domain_input = st.sidebar.text_area("Voer domeinnamen in (één per regel):", key="domain_input")

if st.sidebar.button("Analyseer Domeinen"):
    domains = [d.strip() for d in domain_input.splitlines() if d.strip()]
    if domains:
        with st.spinner("Domein-rapport ophalen..."):
            try:
                df_dom = get_domain_report(domains)
                st.session_state["df_dom"] = df_dom  
                st.subheader("Domein Resultaten")
                st.dataframe(df_dom, use_container_width=True)
                if not df_dom.empty:
                    fig2 = px.bar(df_dom, x="domain", y="malicious",
                                  color="suspicious", title="Malicious detecties per domein")
                    st.plotly_chart(fig2, use_container_width=True)
                st.success("✅ Domeinanalyse voltooid.")
            except Exception as e:
                logger.exception("Domein analyse fout")
                st.error(f"Domein analyse mislukt: {e}")
    else:
        st.info("Geen domeinen ingevoerd.")


st.sidebar.header("📧 Controleer E-mailadressen")
email_input = st.sidebar.text_area("Voer e-mailadressen in (één per regel):", key="email_input")

if st.sidebar.button("Controleer E-mails"):
    emails = [e.strip() for e in email_input.splitlines() if e.strip()]
    if emails:
        with st.spinner("E-mailbreaches ophalen..."):
            try:
                df_em = get_email_report(emails)
                st.session_state["df_em"] = df_em 
                st.subheader("E-mail Breach Resultaten")
                st.dataframe(df_em, use_container_width=True)
                if not df_em.empty:
                    fig3 = px.bar(df_em, x="email_masked", y="count", color="count",
                                  title="Aantal datalekken per e-mailadres")
                    st.plotly_chart(fig3, use_container_width=True)
                st.success("✅ E-mailanalyse voltooid.")
            except Exception as e:
                logger.exception("E-mail analyse fout")
                st.error(f"E-mail analyse mislukt: {e}")
    else:
        st.info("Geen e-mailadressen ingevoerd.")


st.sidebar.header("💾 Export & Download")
if st.sidebar.button("📦 Export Combined CSV (IP + Domain + Email)"):
    try:
        df_ip = st.session_state.get("df_ip", pd.DataFrame())
        df_dom = st.session_state.get("df_dom", pd.DataFrame())
        df_em = st.session_state.get("df_em", pd.DataFrame())

        if df_ip.empty and df_dom.empty and df_em.empty:
            st.warning("⚠️ Geen gegevens gevonden. Voer eerst analyses uit.")
        else:
            csv_bytes = export_combined_csv(df_ip, df_dom, df_em)
            st.success("📁 CSV-bestand klaar om te downloaden.")
            st.download_button("📥 Download combined_report.csv", csv_bytes, "combined_report.csv", "text/csv")
    except Exception as e:
        logger.exception("Export fout")
        st.error(f"Export mislukt: {e}")

st.markdown("---")
st.caption("🛡️ Secure edition – API-keys beschermd via `.env` of Codespaces Secrets. "
           "CSV bevat gemaskeerde e-mails en logt geen gevoelige data.")
