amount = int(input('전기 사용량을 입력하세요. '))
print('사용량 : %.1f kwh' %(amount))

if amount > 400 :
    basicFee = 7300
    unitPrice = 280.6
elif amount>200 :
    basicFee = 1600
    unitPrice = 187.9
else :
    basicFee = 910
    unitPrice = 99.3

print('사용량은 : %.1f kwh' %(amount))
print('기본요금 : %d 원' %(basicFee))
print('단가 : %.1f 원' %(unitPrice))
print('전기 요금 : %.1f 원' %(basicFee+amount*unitPrice))