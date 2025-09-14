import pandas as pd
# DataFrame creation
# df = pd.read_csv('pokemon_data.csv')
# print("DataFrame:\n", df)  # Вывод DataFrame 
# or print(df)
#print(df.head(2))  # Вывод первых 2 строк DataFrame
#print(df.tail(3)) # Вывод последних 3 строк DataFrame

df = pd.read_csv('pokemon_data.txt', delimiter='\t')  
# Чтение данных из текстового файла с разделителем табуляции

# print("DataFrame из текстового файла:\n", df_text) 
# Вывод DataFrame из текстового файла


# read data in pandas
# Read Header
print(df.columns)  # Вывод названий столбцов DataFrame
df.columns  # Вывод названий столбцов DataFrame

# Read each Column
print(df['Name'])  # Вывод столбца 'Name' DataFrame
# or print(df.Name)  # Вывод столбца 'Name' DataFrame
print(df[['Name', 'Type 1', 'HP']]) # Вывод столбца 'Name' DataFrame


# read each row 
print(df.iloc[1])  # Вывод строк с 1 по 4 (не включая 4) DataFrame

# read a specific location (R,C)ш

df = pd.read_csv('pokemon_data.txt', delimiter='\t')  # Чтение данных из текстового файла с разделителем табуляции
df.groupby(['Type 1']).mean().sort_values('Defense',ascending=False)
# Группировка по столбцу 'Type 1' и вычисление среднего значения
# print("Группировка по 'Type 1' и среднее значение:\n", df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)) 
# Вывод сгруппированных данных
