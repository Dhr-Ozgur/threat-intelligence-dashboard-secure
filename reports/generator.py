from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import pandas as pd
from datetime import datetime

def generate_pdf(df):
    os.makedirs("reports", exist_ok=True)
    file_path = f"reports/threat_report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
    c = canvas.Canvas(file_path, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "Threat Intelligence Report")
    c.setFont("Helvetica", 12)
    c.drawString(100, 780, f"Generated at: {datetime.now()}")

    y = 740
    for _, row in df.iterrows():
        line = f"{row['source']}: {row['key_value']} | {row['created_at']}"
        c.drawString(80, y, line)
        y -= 14
        if y < 100:
            c.showPage()
            y = 800
    c.save()
    return file_path
