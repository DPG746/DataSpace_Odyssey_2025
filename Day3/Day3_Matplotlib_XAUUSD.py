import matplotlib.pyplot as plt
dates = ['2025-06-01', '2025-06-02', '2025-06-03', '2025-06-04', '2025-06-05']
prices = [2590, 2605, 2585, 2610, 2595]
plt.figure(figsize=(8, 5))
plt.plot(dates, prices, marker='o', color='gold', label='XAU/USD Price')
plt.title('XAU/USD Closing Prices (June 2025)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Day3/xauusd_plot.png')
plt.show()