import pandas as pd
import numpy as np

# 1
polit = pd.read_csv('polit.csv')

print(f"Колонки: {list(polit.columns)}")
print(f"Размер: {polit.shape}")
print("\nТипы данных:")
print(polit.dtypes)
print("\nПервые 5 строк:")
print(polit.head())

# Kолонки из строк в числа
numeric_columns = ['fh09', 'polity09', 'gini', 'fparl08', 'corr0509']

for col in numeric_columns:
    if col in polit.columns:
        if polit[col].dtype == 'object':
            polit[col] = polit[col].str.replace(',', '.').astype(float)

polit = polit.dropna()
print(polit.dtypes)
print()

# 2
fh_above_5 = polit[polit['fh09'] > 5]
print("2")
print(fh_above_5[['ctry', 'fh09']])
print(f"Кол-во стран: {len(fh_above_5)}")
print()

# 3
africa_high_women = polit[(polit['afri'] == 1) & (polit['fparl08'] > 30)]
print("3")
print(africa_high_women[['ctry', 'afri', 'fparl08']])
print(f"Кол-во стран: {len(africa_high_women)}")
print()

# 4
africa_latin_high_polity = polit[((polit['afri'] == 1) | (polit['lati'] == 1)) & (polit['polity09'] >= 8)]
print("4")
print(africa_latin_high_polity[['ctry', 'afri', 'lati', 'polity09']])
print(f"Кол-во стран: {len(africa_latin_high_polity)}")
print()

polit['corr_round'] = polit['corr0509'].round(2)
print("5")
print(polit[['ctry', 'corr0509', 'corr_round']].head())
print()

def get_fln_status(fh_score):
    if fh_score <= 2.5:
        return 'free'
    elif 2.5 < fh_score <= 5.0:
        return 'partly free'
    else:
        return 'not free'

polit['fln_status'] = polit['fh09'].apply(get_fln_status)
print("6")
print(polit[['ctry', 'fh09', 'fln_status']].head())
print(f"Распределение по статусам:\n{polit['fln_status'].value_counts()}")
print()

# 7
gini_stats = polit.groupby('fln_status')['gini'].agg(['min', 'mean', 'max'])
print("7")
print(gini_stats)
print()

# 8
print("8")
for status in polit['fln_status'].unique():
    group_df = polit[polit['fln_status'] == status]
    filename = f'polit_{status.replace(" ", "_")}.csv'
    group_df.to_csv(filename, index=False)
print(polit['fln_status'].unique())

