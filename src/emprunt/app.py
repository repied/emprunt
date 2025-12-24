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
    home_cost: float
    down_payment: float
    annual_rate: float
    years: int
    savings: float
    investment_rate: float
    monthly_cash: float
    payments_per_year: int = 12


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})


@app.post("/simulate", response_class=HTMLResponse)
async def simulate(
    request: Request,
    home_cost: float = Form(...),
    down_payment: float = Form(...),
    annual_rate: float = Form(...),
    years: int = Form(...),
    savings: float = Form(...),
    investment_rate: float = Form(...),
    monthly_cash: float = Form(...),
):
    result = simulate_mortgage(
        home_cost,
        down_payment,
        annual_rate,
        years,
        savings,
        investment_rate,
        monthly_cash
    )
    return templates.TemplateResponse("index.html", {"request": request, "result": result})


@app.post("/api/simulate")
def api_simulate(req: SimRequest):
    result = simulate_mortgage(
        req.home_cost,
        req.down_payment,
        req.annual_rate,
        req.years,
        req.savings,
        req.investment_rate,
        req.monthly_cash,
        req.payments_per_year
    )
    return JSONResponse(content=result)
