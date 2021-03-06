fruit = [ '배','배','배','배','사과','사과','귤','귤','귤']
set(fruit)

fruit_count = [(s, fruit.count(s)) for s in set(fruit)]

print(fruit_count)

import pandas as pd

df = pd.DataFrame(fruit,columns=['fruit'])

count = df['fruit'].value_counts()
count2 = df['fruit'].value_counts(normalize=True) # normalize 비율로 나타내줌 (default 값은 False)

print(count)
print(count2)