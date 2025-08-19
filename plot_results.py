import matplotlib.pyplot as plt
import pandas as pd

def plot_forecast(df, forecast, start_year):
    # Create future years index
    future_years = pd.date_range(start=start_year, periods=len(forecast), freq="Y")

    plt.figure(figsize=(10,5))
    plt.plot(df.index, df["TotalSales"], label="Historical")
    plt.plot(future_years, forecast, label="Forecast", marker="o")
    plt.title("Sales Forecast")
    plt.xlabel("Year")
    plt.ylabel("Total Sales")
    plt.legend()
    plt.show()
