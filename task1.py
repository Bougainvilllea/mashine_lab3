import pandas as pd
import numpy as np

# 1
series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print("1.")
print(series)
print()

# 2
value_4 = series['d']
print(f"2. {value_4}")
print()

# 3
value_2 = series.iloc[1]
print(f"3. {value_2}")
print()

# 4
series['f'] = 6
print("4.")
print(series)
print()

# 5
slice_values = series['c':'e']
print("5.")
print(slice_values)
print()

# 6
df = pd.DataFrame([[1, 2], [5, 3], [3.7, 4.8]], columns=['col1', 'col2'])
print("6.")
print(df)
print()

# 7
element_3_7 = df.iloc[2, 0]
print(f"7. {element_3_7}")
print()

# 8
df.at[1, 'col2'] = 9
print("8.")
print(df)
print()

# 9
slice_rows = df.iloc[1:3]
print("9.")
print(slice_rows)
print()

# 10
df['col3'] = df['col1'] * df['col2']
print("10.")
print(df)