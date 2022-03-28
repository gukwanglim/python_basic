coffee = 10


while True:
    money = int(input('돈을 넣어 주세요. : '))
    print(money)
    if money == 300:
        print('커피를 드립니다.')
        coffee -= 1
    elif money > 300:
        print('거스름돈 %d와 커피를 드립니다' % (money - 300))
        coffee -= 1
    else:
        print('잔돈이 부족합니다.')
        print('남은 커피의 양은 %d잔 입니다.' % coffee)
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다. ^^')
        break
