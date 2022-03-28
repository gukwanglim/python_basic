#!/usr/bin/env python
# coding: utf-8

# In[ ]:


PI = 3.14

def number_input():
    output = input('숫자 입력 : ')
    return float(output)

def get_circum(r):
    return PI * 2 * r

def get_area(r):
    return r * r * PI

# if __name__ == '__main__':
#     print(get_area(10))
#     print(get_circum(10))

