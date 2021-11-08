import pandas as pd

path_boston = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/boston.csv'

df = pd.read_csv(path_boston)

df.info()

df_chas1 = df.groupby(['medv'])[['tax']].describe()

print(df_chas1)

