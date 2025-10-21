import streamlit as st
import requests
import pandas as pd
from io import BytesIO

BACKEND_URL = "http://127.0.0.1:8000"  # Codespaces / localhost

st.set_page_config(page_title="Threat Intelligence Dashboard", layout="wide")
st.title("🧠 Threat Intelligence Dashboard – Secure Edition")

st.sidebar.header("📊 Input Data")

ip = st.sidebar.text_input("Enter IP address:")
domain = st.sidebar.text_input("Enter Domain:")
email = st.sidebar.text_input("Enter Email:")

if st.sidebar.button("Generate Report"):
    data = {"ip": ip, "domain": domain, "email": email}
    try:
        # PDF isteği
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

            # CSV export (optional)
            df = pd.DataFrame([data])
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("⬇️ Download CSV", csv, "input_data.csv", "text/csv")

        else:
            st.error(f"❌ Error: {res.text}")
    except Exception as e:
        st.error(f"Connection failed: {e}")
