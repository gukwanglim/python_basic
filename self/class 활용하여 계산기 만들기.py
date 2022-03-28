class fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
# class로 사칙연산 가능한 계산기 만들기
# def setdata(self, first, second)에서 self는 a.setdata에서의 a부분을 뜻한다.


a = fourcal()
b = fourcal()


a.setdata(4, 5)
b.setdata(4, 5)


print(a.add())
print(b.add())


print(id(a))
print(id(b))
# class로 만든 계산기 a, b는 id가 서로 다르다.


class fourcal:
    def __init__(self, first, second):   # 이번에는 __init__이 추가 되었다.
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


c = fourcal(5, 8) # 이처럼 __init__이 추가되면 따로 setdata를 사용하지 않는다.


print(c.add())
print(c.mul())
print(c.div())
print(c.sub())



class mfc(fourcal): # ()안에 fourcal(이미 만들어진 계산기)를 넣어면 상속이 된다.
    def pow(self):
        result = self.first ** self.second
        return result


d = mfc(5, 2)
print(d.pow())



class selffc(fourcal):
    def div(self):
        if self.second == 0: # second가 0일 때, return이 0이 되도록.
            return 0
        else:
            result = self.first / self.second
            return result


e = selffc(5, 0)
print(e.div())


f = selffc(3, 6)
print(f.div())
