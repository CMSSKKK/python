import pandas as pd

# 품종별로 꽃잎 폭이 가장 큰 행을 찾아 비교해 봅시다.

path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/iris.csv'

df = pd.read_csv(path)

print(df.head())

print(df['품종'].value_counts())

df_selected = df[(df['품종'] == 'setosa')]
df_selected.sort_values(by=['꽃잎폭'], ascending=False).head(1)

df_selected = df[(df['품종'] == 'virginica')]
df_selected.sort_values(by=['꽃잎폭'], ascending=False).head(1)

df_selected = df[(df['품종'] == 'versicolor')]
df_selected.sort_values(by=['꽃잎폭'], ascending=False).head(1)