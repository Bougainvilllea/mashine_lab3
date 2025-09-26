import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [["Вжик", "Zipper the Fly", "fly", "0.7"],
        ["Тайка", "Gadget Hackwrench", "mouse", None],
        ["Дейл", "Dale", "chipmunk", "1"],
        ["Рокфор", "Monterey Jack", "mouse", "0.8"],
        ["Чип", "Сhip", "chipmunk", "0.2"]]

# 1
df = pd.DataFrame(data, columns=['ru_name', 'en_name', 'class', 'cheer'])
df['cheer'] = pd.to_numeric(df['cheer'], errors='coerce')
print("1:")
print(df)
print(f"Тип: {df['cheer'].dtype}")
print()

# 2
num_rows = len(df)
print(f"2. Число строк: {num_rows}")
print()

# 3
non_null_count = df['cheer'].notna().sum()
print(f"3. Число заполненных ячеек в столбце: {non_null_count}")
print()

# 4
value = df.iloc[2, 1]
print(f"4. Значение в третьей строке, втором столбце: {value}")
print()

# 5
df1 = df.iloc[1:4, 0:3]
print("5. (строки 2-4, столбцы 1-3):")
print(df1)
print()

# 6
df.columns = ['ru_name', 'en_name', 'class', 'cheer']
print("6. Столбцы:")
print(df.columns.tolist())
print()

# 7
df['logcheer'] = np.log(df['cheer'])
print("7")
print(df)
print()

# 8
value_counts = df['class'].value_counts()
x = value_counts.index
y = value_counts.values

plt.figure(figsize=(8, 5))
plt.bar(x, y, color=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Распределение персонажей по видам')
plt.xlabel('Вид персонажа')
plt.ylabel('Количество')
plt.grid(axis='y', alpha=0.3)
plt.show()

print("8. Уникальные значения (x):", x)
print("   Частоты значений (y):", y)