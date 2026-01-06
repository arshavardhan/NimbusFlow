from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    clf = IsolationForest(contamination=0.03, random_state=42)
    df['anomaly'] = clf.fit_predict(df[['cost']])
    df['anomaly_flag'] = df['anomaly'].apply(lambda x: 'Anomaly' if x == -1 else 'Normal')
    return df
