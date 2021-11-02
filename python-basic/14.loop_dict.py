
member = {'name' :'egoing', 'city': 'Seoul', 'job':'Web'}

for key in member :
    print(key,member[key])

members =[
    {'name' :'egoing', 'city': 'Seoul', 'job':'Web'},
    {'name' :'leezche', 'city': 'Jeju', 'job':'Design'}
]
for member in members :
    for key in member :
        print(member[key],end=" ")
    print()