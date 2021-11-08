import pandas as pd

path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/iris.csv'

df = pd.read_csv(path)
# print(df.describe())
# print(df[['꽃잎길이', '꽃잎폭']].sum()) 
# print(df[['꽃잎길이', '꽃잎폭']].mean()) 
# print(df[['꽃잎길이', '꽃잎폭']].std()) 
# print(df[['꽃잎길이', '꽃잎폭']].median()) # 중간값
# print(df[['꽃잎길이', '꽃잎폭']].min()) 
# print(df[['꽃잎길이', '꽃잎폭']].max())

print(df.groupby(['품종'])[['꽃잎길이','꽃잎폭']].mean()) # 품종별로 꽃잎길이와 꽃잎폭의 평균
print(df.groupby(['품종'])[['꽃잎길이','꽃잎폭']].std().sort_values(by=['꽃잎폭'])) # 품종별로 꽃잎길이와 꽃잎폭의 표준편차(꽃잎폭을 기준으로 오름차순)
print(df.groupby(['품종'])[['꽃잎길이','꽃잎폭']].describe()) # 품종별로 꽃잎길이와 꽃잎폭의 정보를 보여줌