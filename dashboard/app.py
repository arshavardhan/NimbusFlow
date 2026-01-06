import streamlit as st
import pandas as pd
import plotly.express as px
from preprocessing.preprocess import preprocess
from ml.forecast import forecast_cost
from ml.anomaly_detection import detect_anomalies
from recommendations.optimize import generate_recommendations

st.set_page_config(page_title="NimbusFlow SaaS", layout="wide")
st.title("☁️ NimbusFlow – Real-Time Multi-Cloud FinOps Dashboard")

refresh_sec = st.sidebar.slider("Refresh Interval (sec)", 5, 30, 10)

while True:
    df = preprocess()
    df = detect_anomalies(df)
    forecast_df = forecast_cost(df)

    # KPI Cards
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Cost", f"{df['cost'].mean():.2f}")
    col2.metric("Max Cost", f"{df['cost'].max():.2f}")
    col3.metric("Anomalies", f"{(df['anomaly_flag']=='Anomaly').sum()}")

    # Plots
    st.subheader("Cost Trend with Anomalies")
    fig = px.line(df, x='timestamp', y='cost', color='anomaly_flag')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Forecast (Next 24 Hours)")
    fig2 = px.line(forecast_df, x='ds', y='yhat')
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Recommendations")
    for rec in generate_recommendations(df):
        st.write("•", rec)

    st.experimental_rerun()
    st.stop()
