from core.recommendations import generate_recommendation

def test_low_cpu_usage():
    recs = generate_recommendation(cpu_avg=20, cost_avg=40)
    assert any("downsizing" in r.lower() for r in recs)

def test_high_cost():
    recs = generate_recommendation(cpu_avg=70, cost_avg=200)
    assert any("reserved" in r.lower() or "spot" in r.lower() for r in recs)

def test_optimal_case():
    recs = generate_recommendation(cpu_avg=60, cost_avg=60)
    assert "optimal" in recs[0].lower()
