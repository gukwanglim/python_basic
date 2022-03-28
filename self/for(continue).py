marks = [90, 25, 67, 45, 80]
number = 0


for mark in marks:
    number += 1
    if mark < 60:
        continue
    print('%d번 학생은 합격입니다.' % number)
# continue는 조건을 만족하는 것을 print 하지 않는다.
