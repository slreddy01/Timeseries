import pandas as pd
#
data = [
    (2000, 120000.0),
    (2001, 135000.5),
    (2002, 150500.8),
    (2003, 175000.2),
    (2004, 210000.9),
    (2005, 250000.0),
    (2006, 310000.7),
    (2007, 380000.3),
    (2008, 420000.5),
    (2009, 390000.1),
    (2010, 43421.0364),   # anomaly
    (2011, 7075525.9291),
    (2012, 5842485.1952),
    (2013, 16351550.34),
    (2014, 45694.72),     # anomaly
    (2015, 2100000.5),
    (2016, 3100000.9),
    (2017, 4200000.3),
    (2018, 5300000.4),
    (2019, 6400000.1),
    (2020, 7200000.2),
    (2021, 8150000.8),
    (2022, 9500000.5),
    (2023, 10500000.7),
    (2024, 11500000.2)
]

# Create DataFrame
df = pd.DataFrame(data, columns=["Year", "TotalSales"])

# Convert Year → datetime
df["Year"] = pd.to_datetime(df["Year"], format="%Y")
df = df.set_index("Year")

print(df.head())


from statsmodels.tsa.arima.model import ARIMA

# Fit ARIMA model
model = ARIMA(df["TotalSales"], order=(1,1,1))
model_fit = model.fit()

# Forecast next 5 years
forecast = model_fit.forecast(steps=5)
print("Forecast for 2025–2029:")
print(forecast)


import matplotlib.pyplot as plt

# Plot historical data
plt.figure(figsize=(10,5))
plt.plot(df.index, df["TotalSales"], label="Historical")

# Plot forecast
future_years = pd.date_range(start="2025", periods=5, freq="Y")
plt.plot(future_years, forecast, label="Forecast", marker="o")

plt.title("Sales Forecast")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.legend()
plt.show()
