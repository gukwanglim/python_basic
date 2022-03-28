coffee = 10
money = 300


while money:
    print('돈을 받았으니 커피를 드립니다.')
    coffee -= 1
    print('남은 커피의 양은 %d잔 입니다.' % coffee)
    if coffee == 0:
        print('커피가 매진되었습니다.')
        break
