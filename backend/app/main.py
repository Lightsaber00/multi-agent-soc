from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Multi-Agent SOC API",
    version="0.1.0",
    description="API skeleton for a SOC alert triage and correlation workflow."
)

class HealthResponse(BaseModel):
    status: str
    service: str

@app.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(status="ok", service="multi-agent-soc")

@app.get("/api/v1/summary")
def summary():
    return {
        "project": "Multi-Agent SOC",
        "mode": "skeleton",
        "message": "Replace mocked handlers with real triage, enrichment, and correlation logic."
    }
