import pandas as pd
# chas가 1인 데이터 중에 가장 비싼 집을 찾아봅시다.
path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/boston.csv'

df = pd.read_csv(path)

df_selected = df[(df['chas'] == 1)]
print(df_selected.sort_values(by=['medv'],ascending=False).head(1))

