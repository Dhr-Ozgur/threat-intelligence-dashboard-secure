import streamlit as st
import requests
import pandas as pd
import plotly.express as px

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Threat Intelligence Report Generator", layout="wide")
st.title("🧠 Threat Intelligence Report Generator")

ips = st.text_area("IP addresses (one per line)")
domains = st.text_area("Domains (one per line)")
emails = st.text_area("Emails (one per line)")

if st.button("🚀 Run Analysis"):
    payload = {
        "ips": [i.strip() for i in ips.splitlines() if i.strip()],
        "domains": [d.strip() for d in domains.splitlines() if d.strip()],
        "emails": [e.strip() for e in emails.splitlines() if e.strip()]
    }
    r = requests.post(f"{BACKEND_URL}/analyze/", json=payload)
    if r.status_code == 200:
        st.success("✅ Analysis completed.")
        results = r.json()
        for key, df_data in results.items():
            st.subheader(key.upper())
            df = pd.DataFrame(df_data)
            st.dataframe(df)
            if key == "ip":
                fig = px.bar(df, x="ip", y="abuseScore", color="country")
                st.plotly_chart(fig)
    else:
        st.error("Failed to connect to backend.")

if st.button("📄 Generate PDF Report"):
    r = requests.get(f"{BACKEND_URL}/export/pdf")
    if r.status_code == 200:
        with open("threat_report.pdf", "wb") as f:
            f.write(r.content)
        st.success("PDF report generated. Saved as threat_report.pdf")
