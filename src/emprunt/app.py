import os
from pathlib import Path
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from .simulator import simulate_mortgage

app = FastAPI(title="Emprunt Mortgage Simulator")

# Determine the base directory for the package
BASE_DIR = Path(__file__).resolve().parent

# Mount static and templates directories using absolute paths relative to this file
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


class SimRequest(BaseModel):
    principal: float
    annual_rate: float
    years: int
    payments_per_year: int = 12


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})


@app.post("/simulate", response_class=HTMLResponse)
async def simulate(request: Request, principal: float = Form(...), annual_rate: float = Form(...), years: int = Form(...)):
    result = simulate_mortgage(principal, annual_rate, years)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})


@app.post("/api/simulate")
def api_simulate(req: SimRequest):
    result = simulate_mortgage(req.principal, req.annual_rate, req.years, req.payments_per_year)
    return JSONResponse(content=result)
