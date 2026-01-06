# NimbusFlow – System Architecture

## High-Level Flow

1. **Metric Ingestion**
   - CPU, memory, cost metrics (synthetic or cloud APIs)
2. **Data Preprocessing**
   - Cleaning, normalization, aggregation
3. **Forecasting Engine**
   - Time-series forecasting using Prophet
4. **Anomaly Detection**
   - Detects cost & usage spikes
5. **Recommendation Engine**
   - Right-sizing, scaling suggestions
6. **Visualization Layer**
   - Streamlit dashboard for insights

## Architecture Diagram (Textual)

User  
↓  
Streamlit UI  
↓  
Data Processing → Forecasting → Anomaly Detection  
↓  
Recommendation Engine  
↓  
Cost Optimization Insights

## Future Enhancements
- Real-time AWS/Azure ingestion
- Auto-remediation hooks
- LLM-powered explanations
