# 평균
import random

sales = [random.randint(1,10) for i in range(10)]
print(sales)

averageVal = sum(sales) / len(sales)
print(averageVal)

# pandas 활용 
import pandas as pd

df = pd.DataFrame(sales,columns=['sales'])
print(df)

mean = df['sales'].mean()
print(mean)