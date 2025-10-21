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
# 🧠 Threat Intelligence Dashboard – Secure Unified Edition
# ----------------------------------------------------------
st.set_page_config(page_title="Threat Intelligence Dashboard – Secure", layout="wide")
st.title("🧠 Threat Intelligence Dashboard – Secure Unified Edition")

# --- Check missing API keys ---
missing = []
if not ABUSEIPDB_KEY:
    missing.append("ABUSEIPDB_KEY")
if not VT_KEY:
    missing.append("VT_KEY")
if not RAPIDAPI_KEY:
    missing.append("RAPIDAPI_KEY")

if missing:
    st.warning("⚠️ Missing environment variables: " + ", ".join(missing) +
               ". Use `.env` locally or GitHub Codespaces Secrets.")

# ----------------------------------------------------------
# Input fields
# ----------------------------------------------------------
st.sidebar.header("🔎 Enter Data for Analysis")

ip_input = st.sidebar.text_area("IP addresses (one per line):", key="ip_input")
domain_input = st.sidebar.text_area("Domain names (one per line):", key="domain_input")
email_input = st.sidebar.text_area("Email addresses (one per line):", key="email_input")

# Initialize session state for results if not set
for key in ["df_ip", "df_dom", "df_em"]:
    if key not in st.session_state:
        st.session_state[key] = pd.DataFrame()

# ----------------------------------------------------------
# Run all analyses at once
# ----------------------------------------------------------
def run_full_analysis():
    """Run IP, domain, and email analysis in sequence."""
    ips = [i.strip() for i in ip_input.splitlines() if i.strip()]
    domains = [d.strip() for d in domain_input.splitlines() if d.strip()]
    emails = [e.strip() for e in email_input.splitlines() if e.strip()]

    all_empty = not any([ips, domains, emails])
    if all_empty:
        st.info("Please enter at least one IP, domain, or email.")
        return

    # --- IP analysis ---
    if ips:
        with st.spinner("Fetching IP reports..."):
            try:
                df_ip = get_ip_report(ips)
                st.session_state["df_ip"] = df_ip
                st.subheader("📊 IP Results")
                st.dataframe(df_ip, use_container_width=True)
                if not df_ip.empty:
                    fig = px.bar(df_ip, x="ip", y="abuseConfidenceScore",
                                 color="countryCode", title="Abuse Confidence Score per IP")
                    st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                logger.exception("IP analysis error")
                st.error(f"IP analysis failed: {e}")

    # --- Domain analysis ---
    if domains:
        with st.spinner("Fetching domain reports..."):
            try:
                df_dom = get_domain_report(domains)
                st.session_state["df_dom"] = df_dom
                st.subheader("🌐 Domain Results")
                st.dataframe(df_dom, use_container_width=True)
                if not df_dom.empty:
                    fig2 = px.bar(df_dom, x="domain", y="malicious",
                                  color="suspicious", title="Malicious detections per domain")
                    st.plotly_chart(fig2, use_container_width=True)
            except Exception as e:
                logger.exception("Domain analysis error")
                st.error(f"Domain analysis failed: {e}")

    # --- Email analysis ---
    if emails:
        with st.spinner("Fetching email breach data..."):
            try:
                df_em = get_email_report(emails)
                st.session_state["df_em"] = df_em
                st.subheader("📧 Email Breach Results")
                st.dataframe(df_em, use_container_width=True)
                if not df_em.empty:
                    fig3 = px.bar(df_em, x="email_masked", y="count", color="count",
                                  title="Number of breaches per email address")
                    st.plotly_chart(fig3, use_container_width=True)
            except Exception as e:
                logger.exception("Email analysis error")
                st.error(f"Email analysis failed: {e}")

    st.success("✅ All analyses completed successfully.")


# ----------------------------------------------------------
# Run button
# ----------------------------------------------------------
if st.sidebar.button("🚀 Run All Analyses"):
    run_full_analysis()

# ----------------------------------------------------------
# Export CSV
# ----------------------------------------------------------
st.sidebar.header("💾 Export & Download")

if st.sidebar.button("📦 Export Combined CSV"):
    try:
        df_ip = st.session_state.get("df_ip", pd.DataFrame())
        df_dom = st.session_state.get("df_dom", pd.DataFrame())
        df_em = st.session_state.get("df_em", pd.DataFrame())

        if df_ip.empty and df_dom.empty and df_em.empty:
            st.warning("⚠️ No data found. Please run the analysis first.")
        else:
            csv_bytes = export_combined_csv(df_ip, df_dom, df_em)
            st.success("📁 CSV file is ready for download.")
            st.download_button("📥 Download combined_report.csv",
                               csv_bytes, "combined_report.csv", "text/csv")
    except Exception as e:
        logger.exception("CSV export error")
        st.error(f"Export failed: {e}")

st.markdown("---")
st.caption(
    "🛡️ Secure unified version – performs IP, domain, and email analysis together. "
    "API keys secured via environment variables. CSV uses masked emails and sanitized logs."
)
