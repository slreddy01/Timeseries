from data_prep import load_data
from forecast_model import forecast_sales
from plot_results import plot_forecast

# Step 1: Load Data
df = load_data()

# Step 2: Forecast next 5 years
forecast = forecast_sales(df, steps=5)
print("Forecasted Sales:")
print(forecast)

# Step 3: Plot Results
plot_forecast(df, forecast, start_year="2025")
