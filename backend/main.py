from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from backend.generator import generate_report

app = FastAPI(title="Threat Intelligence Backend")

# CORS: frontend erişimi için
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "message": "Backend running"}

@app.post("/generate-pdf")
def generate_pdf(data: dict):
    try:
        path = generate_report(data)
        with open(path, "rb") as f:
            pdf_bytes = f.read()
        return Response(content=pdf_bytes, media_type="application/pdf")
    except Exception as e:
        return {"error": str(e)}
