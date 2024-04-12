# Calculate the Average for each Row in a Pandas DataFrame


import pandas as pd

df = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [30, 40, 50],
    'C': [50, 60, 70]
})

print(df)

df['row_average'] = df.mean(axis=1)

print('-' * 50)

print(df['row_average'])