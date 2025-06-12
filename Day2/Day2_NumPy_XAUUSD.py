import numpy as np
prices = [2590, 2605, 2585, 2610, 2595]
price_array = np.array(prices)
mean_price = np.mean(price_array)
std_price = np.std(price_array)
print(f"Mean XAU/USD Price: ${mean_price:.2f}")
print(f"Price Volatility (Std Dev): ${std_price:.2f}")