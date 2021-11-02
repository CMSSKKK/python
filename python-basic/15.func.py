def abc() :
    print('a')
    print('b')
    print('c')

def get_vat(price) :
    percent = 0.1
    return price*percent

p = 1000
answer = get_vat(p)
print(answer)