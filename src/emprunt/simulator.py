"""Mortgage simulator utilities (simple initial implementation).

This is intentionally simple for the scaffold. We'll expand later.
"""
from typing import Dict, List
import pandas as pd
import numpy as np


def simulate_mortgage(
    home_cost: float,
    down_payment: float,
    annual_rate: float,
    years: int,
    savings: float,
    investment_rate: float,
    monthly_cash: float,
    payments_per_year: int = 12
) -> Dict:
    """Return an amortization schedule and investment summary.

    Returns:
        dict with keys: monthly_payment, schedule (list of rows), ...
    """
    principal = home_cost - down_payment
    if principal < 0:
        raise ValueError("Down payment cannot exceed home cost")
    if years <= 0 or payments_per_year <= 0:
        raise ValueError("Years and payments_per_year must be positive")

    r = annual_rate / 100.0 / payments_per_year
    n = years * payments_per_year
    inv_r = investment_rate / 100.0 / payments_per_year

    if r == 0:
        payment = principal / n
    else:
        payment = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)

    # Initial state
    investment_portfolio = savings - down_payment
    balance = principal
    schedule = []

    for period in range(1, n + 1):
        interest = balance * r
        principal_paid = min(balance, payment - interest)
        balance = max(0.0, balance - principal_paid)
        
        # Investment calculation
        investment_return = investment_portfolio * inv_r
        leftover_cash = monthly_cash - payment
        investment_portfolio += investment_return + leftover_cash
        
        home_equity = home_cost - balance
        combined_wealth = home_equity + investment_portfolio

        schedule.append({
            "period": period,
            "payment": round(payment, 2),
            "principal_paid": round(principal_paid, 2),
            "interest_paid": round(interest, 2),
            "balance": round(balance, 2),
            "home_equity": round(home_equity, 2),
            "investment_portfolio": round(investment_portfolio, 2),
            "combined_wealth": round(combined_wealth, 2),
        })

    df = pd.DataFrame(schedule)

    return {
        "home_cost": float(home_cost),
        "down_payment": float(down_payment),
        "principal": float(principal),
        "annual_rate": float(annual_rate),
        "years": int(years),
        "savings": float(savings),
        "investment_rate": float(investment_rate),
        "monthly_cash": float(monthly_cash),
        "payment": round(float(payment), 2),
        "schedule": df.to_dict(orient="records"),
    }
