# 합치기

import pandas as pd

df1 = pd.DataFrame([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
df2 = pd.DataFrame([[1,2,3,4],[4,5,6,7],[7,8,9,10]])

df_concat = pd.concat([df1,df2], axis=1) # axis =1 -> 열 / axis = 0 -> 행

#print(df_concat)

#df_concat.columns = [0,1,2,3,4,5,6,7]
#print(df_concat)

df_concat = df_concat.reset_index(drop=True)
print(df_concat)