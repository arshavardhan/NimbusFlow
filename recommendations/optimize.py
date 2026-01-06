def generate_recommendations(df):
    latest_cost = df['cost'].iloc[-1]
    avg_cost = df['cost'].mean()
    recommendations = []

    if latest_cost > avg_cost * 1.2:
        recommendations.append(f"⚠️ Cost spike detected ({latest_cost:.2f}). Consider stopping idle instances or scaling down.")
    else:
        recommendations.append(f"✅ Cost is within expected range ({latest_cost:.2f}).")

    # Example: CPU/memory scaling recommendation
    high_cpu = df[df['cpu'] > 80]
    if not high_cpu.empty:
        recommendations.append("⚠️ Some instances have high CPU utilization. Consider scaling up resources.")

    return recommendations
