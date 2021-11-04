numbers = list(range(10))

evens = [n for n in numbers if n %2 == 0 and n != 0]
print(evens)

odds = [n for n in numbers if n %2 == 1]
print(odds)

square_evens = [n ** 2 for n in numbers if n%2 == 0 and n != 0]
print(square_evens)