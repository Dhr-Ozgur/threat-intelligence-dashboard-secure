import streamlit as st
import requests
import pandas as pd

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Threat Intelligence Dashboard", layout="wide")
st.title("🧠 Threat Intelligence Dashboard – Secure Edition")

ip = st.text_input("IP Address")
domain = st.text_input("Domain")
email = st.text_input("Email")

if st.button("Generate Report"):
    data = {"ip": ip, "domain": domain, "email": email}
    try:
        res = requests.post(f"{BACKEND_URL}/generate-pdf", json=data)
        if res.status_code == 200:
            st.success("✅ PDF generated successfully!")

            pdf_bytes = res.content
            st.download_button(
                label="📥 Download Threat Report (PDF)",
                data=pdf_bytes,
                file_name="threat_report.pdf",
                mime="application/pdf"
            )

            scores = {
                "ip_risk": len(ip) * 5 % 100,
                "domain_risk": len(domain) * 7 % 100,
                "email_risk": len(email) * 9 % 100
            }

            df = pd.DataFrame([{**data, **scores}])
            csv_bytes = df.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download Power BI CSV", csv_bytes, "powerbi_export.csv")

            st.dataframe(df)
        else:
            st.error(f"Backend error: {res.text}")
    except Exception as e:
        st.error(f"Connection failed: {e}")
