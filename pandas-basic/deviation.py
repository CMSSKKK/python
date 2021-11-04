# 표준 편차
import random

sales = [random.randint(1,10) for i in range(10)]
print(sales)

mean = sum(sales) / len(sales)

deviations = [round(s - mean,2) for s in sales]
print(deviations)

import math
분산 = sum([d ** 2 for d in deviations]) / len(deviations)
std = math.sqrt(분산)

# pandas 활용
import pandas as pd

df = pd.DataFrame(sales,columns=['sales'])
std = df['sales'].std()
print(std)