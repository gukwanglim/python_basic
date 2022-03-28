count = 0

while count < 10:
    count += 1
    if count < 4:
        continue
    if count == 9:
        break
    print('횟수 : ', count)
