import pandas as pd

# 데이터의 개수가 동일해야함
players = {
    'p1': [7, 9, 9, 10, 10, 10, 10, 10, 11, 11, 13],
    'p2': [7, 8, 9, 9, 10, 10, 10, 11, 11, 12, 13],
    'p3': [3, 3, 6, 7, 7, 10, 10, 10, 11, 13, 30]
}

df = pd.DataFrame(players)
print(df)
print(df.describe())