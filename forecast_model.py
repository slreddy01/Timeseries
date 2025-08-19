from statsmodels.tsa.arima.model import ARIMA

# Fit ARIMA model
model = ARIMA(df["TotalSales"], order=(1,1,1))
model_fit = model.fit()

# Forecast next 5 years
forecast = model_fit.forecast(steps=5)
print("Forecast for 2025–2029:")
print(forecast)
