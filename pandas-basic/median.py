# 중앙값
import random

sales = [random.randint(1, 100) for i in range(100)]
sales.sort()

n = len(sales) // 2 #  // <- 몫을 정수로 구하는 연산자

if len(sales) %2 == 0 :
    median = sum(sales[n-1:n+1]) / 2
else :
    median = sales[n] 
print(median)

# pandas 활용
import pandas as pd

df = pd.DataFrame(sales, columns=['sales'])

med = df['sales'].median()

print(med)