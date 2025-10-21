import streamlit as st
import requests
import pandas as pd
from io import BytesIO

# Backend endpoint (FastAPI)
BACKEND_URL = "http://127.0.0.1:8000"

# Streamlit page config
st.set_page_config(page_title="Threat Intelligence Dashboard", layout="wide")
st.title("🧠 Threat Intelligence Dashboard – Secure Edition")

# Sidebar inputs
st.sidebar.header("📊 Input Data")

ip = st.sidebar.text_input("Enter IP address:")
domain = st.sidebar.text_input("Enter Domain:")
email = st.sidebar.text_input("Enter Email:")

# Generate button
if st.sidebar.button("Generate Report"):
    data = {"ip": ip, "domain": domain, "email": email}

    # ---- Risk Scoring (for Power BI + visualization) ----
    scores = {
        "ip_risk": len(ip) * 5 % 100,
        "domain_risk": len(domain) * 7 % 100,
        "email_risk": len(email) * 9 % 100
    }

    df = pd.DataFrame([{**data, **scores}])

    # ---- Request PDF from Backend ----
    try:
        res = requests.post(f"{BACKEND_URL}/generate-pdf", json=data)

        if res.status_code == 200:
            st.success("✅ PDF report generated successfully!")

            pdf_bytes = res.content
            st.download_button(
                label="📥 Download Threat Report (PDF)",
                data=pdf_bytes,
                file_name="threat_report.pdf",
                mime="application/pdf"
            )

            # ---- CSV Export (Power BI Ready) ----
            csv_bytes = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Download Power BI CSV",
                data=csv_bytes,
                file_name="powerbi_export.csv",
                mime="text/csv"
            )

            st.info("💡 Open Power BI → Get Data → Text/CSV → select 'powerbi_export.csv'")
            st.dataframe(df, use_container_width=True)

        else:
            st.error(f"❌ Error from backend: {res.text}")

    except Exception as e:
        st.error(f"Connection failed: {e}")
