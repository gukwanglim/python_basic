def add_mul(c, *args):
    if c == 'add':
        result = 0
        for i in args:
            result = result + i
    elif c == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result
