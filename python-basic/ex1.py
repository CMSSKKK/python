radius = int(input('원의 반지름을 입력하시오 : '))

area = 3.14 * radius* radius
circum = 3.14 * 2 * radius

print('반지름은 %.2f의 면적은 = %.2f' %(radius,area))
print('반지름은 %.2f의 둘레는 = %.2f' %(radius,circum))