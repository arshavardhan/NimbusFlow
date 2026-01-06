import pandas as pd
import time
import os

SOURCE_CSV = "data/cloud_metrics.csv"
LIVE_CSV = "data/live_metrics.csv"

# Initialize live CSV
if not os.path.exists(LIVE_CSV):
    df = pd.read_csv(SOURCE_CSV).iloc[:10]
    df.to_csv(LIVE_CSV, index=False)

# Simulate real-time feed
def simulate_feed(interval=5, chunk_size=5):
    while True:
        df_source = pd.read_csv(SOURCE_CSV)
        df_live = pd.read_csv(LIVE_CSV)
        next_idx = len(df_live)
        if next_idx < len(df_source):
            new_rows = df_source.iloc[next_idx:next_idx+chunk_size]
            df_live = pd.concat([df_live, new_rows])
            df_live.to_csv(LIVE_CSV, index=False)
        time.sleep(interval)

if __name__ == "__main__":
    simulate_feed()
