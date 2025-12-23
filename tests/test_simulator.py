from emprunt.simulator import simulate_mortgage


def test_simulator_basic():
    res = simulate_mortgage(100000, 3.5, 20)
    assert "payment" in res
    assert "schedule" in res
    assert len(res["schedule"]) == 20 * 12
    assert res["payment"] > 0
