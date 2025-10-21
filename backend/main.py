from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from reports.generator import generate_report
import os

app = FastAPI(title="Threat Intelligence Backend", version="1.1")

class ReportRequest(BaseModel):
    ip: str | None = None
    domain: str | None = None
    email: str | None = None

@app.get("/")
def root():
    return {"status": "ok", "message": "Threat Intelligence Backend Running"}

@app.post("/generate-pdf")
def create_pdf(request_data: ReportRequest):
    data = {
        "IP Address": request_data.ip or "—",
        "Domain": request_data.domain or "—",
        "Email": request_data.email or "—",
    }
    pdf_path = generate_report(data)
    if os.path.exists(pdf_path):
        return FileResponse(pdf_path, media_type="application/pdf", filename="threat_report.pdf")
    return JSONResponse(content={"error": "PDF not generated"}, status_code=500)
