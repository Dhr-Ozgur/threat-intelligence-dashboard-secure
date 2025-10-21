import streamlit as st
import requests
import pandas as pd
import plotly.express as px

BACKEND = "http://127.0.0.1:8000"

st.set_page_config(page_title="Threat Intelligence Dashboard", layout="wide")
st.title("🧠 Threat Intelligence Dashboard — Secure + Functional")

st.sidebar.header("🔎 Input")
ips_raw = st.sidebar.text_area("IPs (one per line)", value="8.8.8.8\n1.1.1.1")
domains_raw = st.sidebar.text_area("Domains (one per line)", value="example.com\ngoogle.com")
emails_raw = st.sidebar.text_area("Emails (one per line)", value="test@example.com")

if "df_ip" not in st.session_state: st.session_state["df_ip"] = pd.DataFrame()
if "df_dom" not in st.session_state: st.session_state["df_dom"] = pd.DataFrame()
if "df_em" not in st.session_state: st.session_state["df_em"] = pd.DataFrame()

if st.sidebar.button("🚀 Run Full Analysis"):
    payload = {
        "ips": [x.strip() for x in ips_raw.splitlines() if x.strip()],
        "domains": [x.strip() for x in domains_raw.splitlines() if x.strip()],
        "emails": [x.strip() for x in emails_raw.splitlines() if x.strip()],
    }
    try:
        r = requests.post(f"{BACKEND}/analyze", json=payload, timeout=120)
        r.raise_for_status()
        data = r.json()
        df_ip = pd.DataFrame(data.get("ip", []))
        df_dom = pd.DataFrame(data.get("domain", []))
        df_em = pd.DataFrame(data.get("email", []))

        st.session_state["df_ip"] = df_ip
        st.session_state["df_dom"] = df_dom
        st.session_state["df_em"] = df_em

        st.success("✅ Analysis complete.")

    except Exception as e:
        st.error(f"Analysis failed: {e}")

# IP section
if not st.session_state["df_ip"].empty:
    st.subheader("📊 IP Results")
    st.dataframe(st.session_state["df_ip"], use_container_width=True)
    if "abuseScore" in st.session_state["df_ip"].columns:
        fig = px.bar(st.session_state["df_ip"], x="ip", y="abuseScore", color="country", title="Abuse Score per IP")
        st.plotly_chart(fig, use_container_width=True)

# Domain section
if not st.session_state["df_dom"].empty:
    st.subheader("🌐 Domain Results")
    st.dataframe(st.session_state["df_dom"], use_container_width=True)
    if "malicious" in st.session_state["df_dom"].columns:
        fig2 = px.bar(st.session_state["df_dom"], x="domain", y="malicious", color="suspicious", title="Malicious per Domain")
        st.plotly_chart(fig2, use_container_width=True)

# Email section
if not st.session_state["df_em"].empty:
    st.subheader("📧 Email Breach Results (masked)")
    st.dataframe(st.session_state["df_em"], use_container_width=True)
    if "count" in st.session_state["df_em"].columns:
        fig3 = px.bar(st.session_state["df_em"], x="email_masked", y="count", title="Breaches per Email")
        st.plotly_chart(fig3, use_container_width=True)

st.sidebar.header("💾 Export")
if st.sidebar.button("📦 Export Combined CSV"):
    parts = []
    for key, df in [("ip", st.session_state["df_ip"]), ("domain", st.session_state["df_dom"]), ("email", st.session_state["df_em"])]:
        if not df.empty:
            df2 = df.copy()
            if "source" not in df2.columns:
                df2["source"] = key
            parts.append(df2)
    if parts:
        combined = pd.concat(parts, ignore_index=True)
        combined["exported_at"] = pd.Timestamp.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")
        st.download_button("📥 Download combined_report.csv", combined.to_csv(index=False).encode("utf-8"), "combined_report.csv", "text/csv")
        st.success("CSV ready.")
    else:
        st.warning("No data to export. Please run analysis first.")

if st.sidebar.button("🧾 Generate PDF Report"):
    payload = {
        "ips": [x.strip() for x in ips_raw.splitlines() if x.strip()],
        "domains": [x.strip() for x in domains_raw.splitlines() if x.strip()],
        "emails": [x.strip() for x in emails_raw.splitlines() if x.strip()],
    }
    try:
        r = requests.post(f"{BACKEND}/export/pdf", json=payload, timeout=200)
        r.raise_for_status()
        st.download_button("📥 Download threat_report.pdf", r.content, "threat_report.pdf", "application/pdf")
        st.success("PDF ready.")
    except Exception as e:
        st.error(f"PDF generation failed: {e}")

st.caption("🛡️ API keys via environment (never in code). Emails masked, no sensitive logs. Ready for portfolio & Power BI.")
