import pandas as pd
# Simulated XAU/USD data
data = {'Date': ['2025-06-01', '2025-06-02', '2025-06-03', '2025-06-04'],
        'Close': [2590, 2605, 2585, 2610]}
df = pd.DataFrame(data)
# Filter rows where Close > 2600
filtered_df = df[df['Close'] > 2600]
print(filtered_df['Date'])

