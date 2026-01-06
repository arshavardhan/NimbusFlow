import pandas as pd

def preprocess(csv_path="data/live_metrics.csv"):
    df = pd.read_csv(csv_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    # Normalize metrics (0–1)
    for col in ['cpu', 'memory', 'disk', 'network', 'cost']:
        df[col + '_norm'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df
