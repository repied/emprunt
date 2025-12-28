import pytest
from emprunt.simulator import simulate_mortgage


def test_simulator_basic():
    # home_cost, down_payment, annual_rate, years, savings, investment_rate, monthly_cash
    res = simulate_mortgage(100000, 20000, 3.5, 20, 30000, 5.0, 1000)
    assert "payment" in res
    assert "schedule" in res
    assert len(res["schedule"]) == 20 * 12
    assert res["payment"] > 0

def test_simulator_zero_rate():
    res = simulate_mortgage(100000, 0, 0, 10, 0, 0, 1000)
    assert res["payment"] == round(100000 / 120, 2)

def test_simulator_invalid_inputs():
    with pytest.raises(ValueError, match="Down payment cannot exceed home cost"):
        simulate_mortgage(100000, 120000, 3.5, 20, 30000, 5.0, 1000)
    
    with pytest.raises(ValueError, match="Years and payments_per_year must be positive"):
        simulate_mortgage(100000, 20000, 3.5, 0, 30000, 5.0, 1000)
