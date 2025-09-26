import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1
url = "https://raw.githubusercontent.com/slemeshevsky/python-course-ipynb/master/src-pandas/la-crimes-sample.csv.zip"
df = pd.read_csv(url, compression='zip')

# 2
print(f"2. Размер таблицы: {df.shape[0]} строк, {df.shape[1]} столбцов")
print()

# 3
print("3")
print(df.columns.tolist())
print()
print("Типы данных:")
print(df.dtypes)
print()

# 4
print("4")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} уникальных значений")
print()

# 5
print("5")
print(df.isnull().sum())
print()

# 6
print("6")
print(df.head())
print()

sex_columns = [col for col in df.columns if 'sex' in col.lower() or 'gender' in col.lower()]
print(f"Столбцы, связанные с полом: {sex_columns}")
print()

if sex_columns:
    victim_sex_column = sex_columns[0]
    victim_sex_counts = df[victim_sex_column].value_counts()
    print(f"Распределение по полу ({victim_sex_column}):")
    print(victim_sex_counts)

    if 'F' in victim_sex_counts.index and 'M' in victim_sex_counts.index:
        if victim_sex_counts['F'] > victim_sex_counts['M']:
            print("ДА, женщины чаще оказываются жертвами преступлений")
        else:
            print("НЕТ, мужчины чаще оказываются жертвами преступлений")


# 7
crime_columns = [col for col in df.columns if 'crime' in col.lower() or 'crm' in col.lower() or 'desc' in col.lower()]
print(f"Столбцы, связанные с описанием преступлений: {crime_columns}")
print()

if crime_columns:
    crime_desc_column = crime_columns[0]
    print(f"7 ({crime_desc_column}):")
    top_crimes = df[crime_desc_column].value_counts().head(10)
    print(top_crimes)

    plt.figure(figsize=(12, 6))
    top_crimes.plot(kind='bar', color='skyblue')
    plt.title('10 самых распространенных преступлений в Лос-Анджелесе')
    plt.xlabel('Вид преступления')
    plt.ylabel('Количество случаев')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
print()

# 8
if sex_columns and crime_columns:
    print("8")

    female_crimes = df[df[victim_sex_column] == 'F'][crime_desc_column].value_counts().head(5)
    print("Топ-5 преступлений против женщин:")
    print(female_crimes)
    print()

    male_crimes = df[df[victim_sex_column] == 'M'][crime_desc_column].value_counts().head(5)
    print("Топ-5 преступлений против мужчин:")
    print(male_crimes)

print()

# 9
descent_columns = [col for col in df.columns if
                   'descent' in col.lower() or 'race' in col.lower() or 'ethnic' in col.lower()]
print(f"Столбцы, связанные с происхождением: {descent_columns}")
print()

if descent_columns:
    victim_descent_column = descent_columns[0]
    print(f"9 ({victim_descent_column}):")
    victim_descent_counts = df[victim_descent_column].value_counts()
    print(victim_descent_counts)

    most_common_descent = victim_descent_counts.index[0]
    print(f"Чаще всего преступлениям подвергаются {most_common_descent}")
print()

# 10
area_columns = [col for col in df.columns if
                'area' in col.lower() or 'district' in col.lower() or 'location' in col.lower()]
print(f"Столбцы, связанные с районами: {area_columns}")
print()

if area_columns:
    area_column = area_columns[0]
    print(f"10 ({area_column}):")
    area_crimes = df[area_column].value_counts().sort_values(ascending=False)
    print(area_crimes.head(10))

    plt.figure(figsize=(12, 6))
    area_crimes.head(10).sort_values(ascending=True).plot(kind='barh', color='lightcoral')
    plt.title('Топ-10 районов по количеству преступлений в Лос-Анджелесе')
    plt.xlabel('Количество преступлений')
    plt.ylabel('Район')
    plt.tight_layout()
    plt.show()


    safest_area = area_crimes.index[-1]
    most_dangerous_area = area_crimes.index[0]

    safest_count = area_crimes[safest_area]
    dangerous_count = area_crimes[most_dangerous_area]

    print(f"Самый опасный район: {most_dangerous_area} ({dangerous_count} преступлений)")
    print(f"Самый безопасный район: {safest_area} ({safest_count} преступлений)")
