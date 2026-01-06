from prophet import Prophet

def forecast_cost(df, periods=24, freq='H'):
    df_train = df[['timestamp', 'cost']].rename(columns={'timestamp':'ds','cost':'y'})
    model = Prophet()
    model.fit(df_train)
    future = model.make_future_dataframe(periods=periods, freq=freq)
    forecast = model.predict(future)
    return forecast
