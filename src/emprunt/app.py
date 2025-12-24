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
    # Scenario 1
    s1_home_cost: str = Form(...),
    s1_down_payment: str = Form(...),
    s1_annual_rate: float = Form(...),
    s1_years: int = Form(...),
    s1_savings: str = Form(...),
    s1_investment_rate: float = Form(...),
    s1_monthly_cash: str = Form(...),
    # Scenario 2
    s2_home_cost: str = Form(...),
    s2_down_payment: str = Form(...),
    s2_annual_rate: float = Form(...),
    s2_years: int = Form(...),
    s2_savings: str = Form(...),
    s2_investment_rate: float = Form(...),
    s2_monthly_cash: str = Form(...),
):
    def clean_money(val: str) -> float:
        return float(val.replace(",", ""))

    # Run Scenario 1
    res1 = simulate_mortgage(
        clean_money(s1_home_cost),
        clean_money(s1_down_payment),
        s1_annual_rate,
        s1_years,
        clean_money(s1_savings),
        s1_investment_rate,
        clean_money(s1_monthly_cash)
    )

    # Run Scenario 2
    res2 = simulate_mortgage(
        clean_money(s2_home_cost),
        clean_money(s2_down_payment),
        s2_annual_rate,
        s2_years,
        clean_money(s2_savings),
        s2_investment_rate,
        clean_money(s2_monthly_cash)
    )

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result1": res1,
        "result2": res2
    })


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
