a = 0


while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)
# continue는 주어진 조건에 만족하는 것이 나오면 print 하지 않고 넘어간다
