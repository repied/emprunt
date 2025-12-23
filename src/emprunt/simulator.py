"""Mortgage simulator utilities (simple initial implementation).

This is intentionally simple for the scaffold. We'll expand later.
"""
from typing import Dict, List
import pandas as pd
import numpy as np


def simulate_mortgage(principal: float, annual_rate: float, years: int, payments_per_year: int = 12) -> Dict:
    """Return a simple amortization schedule and summary.

    Returns:
        dict with keys: monthly_payment, schedule (list of rows as dicts), principal, annual_rate, years
    """
    if principal <= 0 or years <= 0 or payments_per_year <= 0:
        raise ValueError("Principal, years and payments_per_year must be positive")

    r = annual_rate / 100.0 / payments_per_year
    n = years * payments_per_year

    if r == 0:
        payment = principal / n
    else:
        payment = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)

    # Build schedule using pandas for convenience
    schedule = []
    balance = principal

    for period in range(1, n + 1):
        interest = balance * r
        principal_paid = min(balance, payment - interest)
        balance = max(0.0, balance - principal_paid)
        schedule.append({
            "period": period,
            "payment": round(payment, 2),
            "principal_paid": round(principal_paid, 2),
            "interest_paid": round(interest, 2),
            "balance": round(balance, 2),
        })

    df = pd.DataFrame(schedule)

    return {
        "principal": float(principal),
        "annual_rate": float(annual_rate),
        "years": int(years),
        "payments_per_year": int(payments_per_year),
        "payment": round(float(payment), 2),
        "schedule": df.to_dict(orient="records"),
    }
