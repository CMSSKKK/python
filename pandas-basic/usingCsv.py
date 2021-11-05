import pandas as pd
# 데이터 불러오기 
path = 'https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/lemonade.csv'

df = pd.read_csv(path)

# print(df.shape)
# df.info()
# df.head()
# df.tail()
# print(df.columns)

# # row/column 선택하기
# df[['온도','판매량']]
# df[['온도']]
# df['온도']
# df.iloc[0:3]
# df.loc[0:3] 
# df.iloc[3,1]
# df.iloc[2:4, :]

# df_sorted = df.sort_values(by=['판매량'], ascending=False)
# print(df_sorted)

# 원하는 데이터 찾기
# print(df['온도'] > 23)

# print(df[(df['온도'] > 23)])

# print(df[(df['온도'] > 23 | (df['판매량']==40))])

d = { 'col1' : [ 'item0','item0','item1','item1'],
'col2' : ['Gold','Bronze','Gold','Silver']}
df1 = pd.DataFrame(d)

print(df1['col2'].str.contains('o'))

print(df1[df1['col2'].str.contains('o')])