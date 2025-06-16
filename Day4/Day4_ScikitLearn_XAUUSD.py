import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os
os.makedirs('Day4', exist_ok=True)
days = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
prices = np.array([2590, 2605, 2585, 2610, 2595])
model = LinearRegression()
model.fit(days, prices)
day_6 = np.array([[6]])
predicted_price = model.predict(day_6)
plt.figure(figsize=(8, 5))
plt.scatter(days, prices, color='gold', label='Actual Prices')
plt.plot(days, model.predict(days), color='blue', label='Regression Line')
plt.scatter(day_6, predicted_price, color='red', marker='*', s=200, label=f'Predicted Day 6: ${predicted_price[0]:.2f}')
plt.title('XAU/USD Price Prediction (June 2025)')
plt.xlabel('Day')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('Day4/xauusd_prediction.png')
plt.show()
print(f"Predicted XAU/USD Price for Day 6: ${predicted_price[0]:.2f}")