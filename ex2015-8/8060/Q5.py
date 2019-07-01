import numpy as np
import scipy as sp
import math

# (5) だよ
def convert_10_to_rome(input_num):
    # input_num = int(input('Input (10進数) >'))
    temp_num = input_num + 0

    orders = [1000, 100, 10, 1]
    mapper = { 1000: ('M'), 100: ('C', 'D'), 10: ('X', 'L'), 1:('I', 'V')}

    str_rome = ''
    for ord in orders:
        # 現在の位における数 2345, ord=100 => 3など
        num_ord = math.floor(temp_num / ord)
        temp_num -= num_ord * ord

        if num_ord == 4:
            str_rome += (mapper[ord][0] + mapper[ord][1])
            continue
        if num_ord == 9:
            str_rome += (mapper[ord][0] + mapper[ord * 10][0])
            continue
        elif num_ord >= 5:
            str_rome += mapper[ord][1]
            num_ord -= 5

        str_rome += mapper[ord][0] * num_ord

    return str_rome

print(convert_10_to_rome(int(input('Input (10進数) >'))))
