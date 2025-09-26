import pandas as pd

vg_data = pd.read_csv('vgsales.csv')
print("1. Список игровых платформ:", vg_data['Platform'].unique())

meta_data = pd.read_csv('metacritic_games.csv')
combined_df = vg_data.merge(meta_data[['name', 'platform', 'rating', 'metascore']], 
                           left_on=['Name', 'Platform'], 
                           right_on=['name', 'platform'], 
                           how='left').drop(['name', 'platform'], axis=1)
combined_df.rename(columns={'metascore': 'critic_score'}, inplace=True)

adult_games = combined_df[(combined_df['rating'] == 'M') & (combined_df['Year'] >= 2012)]
print("\n3. Список игр для взрослых (2012+ год):")
print(adult_games[['Name', 'Year', 'rating']].to_string(index=False))

print("\n4. Основные статистические показатели:")
print(adult_games.describe())

genre_stats = vg_data['Genre'].value_counts()
vowel_letters = set('aeiouауоыиэяюёе')
selected_genres = {
    genre: count for genre, count in genre_stats.items() 
    if len([v for v in set(genre.lower()) if v in vowel_letters]) >= 3
}
print("\n5. Популярные игровые жанры:")
for genre, count in selected_genres.items():
    print(f"Жанр {genre}: {count} игр")