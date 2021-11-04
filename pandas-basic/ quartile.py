# 사분위수
import random

sales = [random.randint(1,100) for i in range(16)]
sales.sort()

n = len(sales) // 4
print(f"{sales[n]},{sales[2*n]},{sales[3*n]}")

# pandas 활용
import pandas as pd

df = pd.DataFrame(sales, columns=['sales'])
quan =df['sales'].quantile([.25, .5, .75])
print(quan)

# 기술통계한번에 보기
all = df.describe()
print(all)