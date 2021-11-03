from datetime import datetime

carNum = int(input('차량 번호 4자리를 입력하세요. '))
today = datetime.today().day

print('오늘 날짜 : %d 일 ' %(today))
if today % 2 == 0 :
    print('오늘 입차 : 번호가 짝수인 차량')
    if carNum % 2 == 0 :
        print('귀하의 차량은 입차 가능합니다.')
    else :
        print('귀하의 차량은 입차 불가능합니다.')
else :
    print('오늘 입차 : 번호가 홀수인 차량')
    if carNum % 2 == 1 :
        print('귀하의 차량은 입차 가능합니다.')
    else :
        print('귀하의 차량은 입차 불가능합니다.')