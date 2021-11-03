import random
lotto = []

while len(lotto) < 6 :
    num  = random.randrange(1,46)
    if num not in lotto:
        lotto.append(num)

print(lotto)