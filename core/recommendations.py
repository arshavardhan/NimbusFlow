def generate_recommendation(cpu_avg, cost_avg):
    insights = []

    if cpu_avg < 30:
        insights.append(
            "Low CPU utilization detected. Consider downsizing resources."
        )

    if cost_avg > 100:
        insights.append(
            "High monthly cost observed. Evaluate reserved or spot instances."
        )

    if not insights:
        insights.append("Resource usage is within optimal thresholds.")

    return insights
