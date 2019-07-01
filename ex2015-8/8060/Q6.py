import numpy as np
import scipy as sp
import math

# (6) だよ
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

def convert_10_to_exrome(input_num):
    temp_num = input_num + 0

    # 123 => [(0, 1000), (1, 100), (2,10), (3,1)] みたいに分解
    def explode_order(n):
        orders = [1000, 100, 10, 1]
        ret_list = []
        temp = n + 0
        for ord in orders:
            # 現在の位における数 2345, ord=100 => 3など
            num_ord = math.floor(temp / ord)
            temp -= num_ord * ord
            ret_list.append((num_ord, ord))
        return ret_list

    num_ord_list = explode_order(temp_num)

    mapper = { 1000: ('M'), 100: ('C', 'D'), 10: ('X', 'L'), 1:('I', 'V')}

    str_rome = ''

    # 1000の位は普通
    i = 0
    s = num_ord_list[i]
    str_rome += convert_10_to_rome(s[0] * s[1])

    # 100の位
    i = 1
    s = num_ord_list[i]
    if s[0] in (4,9):
        t = num_ord_list[i+1]
        u = num_ord_list[i+2]
        if t[0] == 9:
            # .(4|9)99
            if u[0] == 9: # (4|9)99
                if s[0] == 9: # 999
                    str_rome += 'IM'
                elif s[0] == 4: # 499
                    str_rome += 'IL'
                i = 4
            if u[0] >= 5: # (4|9)95, (4|9)96, ..
                if s[0] == 9: # 995, 996, ..
                    str_rome += 'VM'
                    num_ord_list = explode_order( temp_num - 995 )
                elif s[0] == 4: # 495, 496, ..
                    str_rome += 'VD'
                    num_ord_list = explode_order( temp_num - 495 )
                i = 3
            else:
                if s[0] == 9: # 99*
                    str_rome += 'XM'
                    num_ord_list = explode_order( temp_num - 990 )
                elif s[0] == 4: # 49*
                    str_rome += 'XD'
                    num_ord_list = explode_order( temp_num - 490 )
                i = 3

        elif t[0] >= 5:
            if s[0] == 9: # 95*, 96*, ..
                str_rome += 'LM'
                num_ord_list = explode_order( temp_num - 950 )
            elif s[0] == 4: # 45*, 46*, ..
                str_rome += 'LD'
                num_ord_list = explode_order( temp_num - 450 )
            i = 2

        else:
            if s[0] == 9: # 9**, 9**, ..
                str_rome += 'CM'
                num_ord_list = explode_order( temp_num - 900 )
            elif s[0] == 4: # 4**, 4**, ..
                str_rome += 'DC'
                num_ord_list = explode_order( temp_num - 400 )
            i = 2

    else:
        str_rome += convert_10_to_rome(s[0] * s[1])
        i = 2

    # 10の位
    if i == 2:
        s = num_ord_list[i]
        if s[0] in (4,9):
            t = num_ord_list[i+1]
            if t[0] == 9:
                if s[0] == 9: # 99
                    str_rome += 'IC'
                elif s[0] == 4: # 49
                    str_rome += 'IL'
                i = 4
            elif t[0] >= 5:
                if s[0] == 9: # 95, 96,
                    str_rome += 'VC'
                    num_ord_list = explode_order( temp_num - 95 )
                elif s[0] == 4: # 45, 46
                    str_rome += 'VL'
                    num_ord_list = explode_order( temp_num - 45 )
                i = 3
            else:
                if s[0] == 9: # 9*
                    str_rome += 'XC'
                    num_ord_list = explode_order( temp_num - 90 )
                elif s[0] == 4: # 4*
                    str_rome += 'DC'
                    num_ord_list = explode_order( temp_num - 40 )
                i = 3
        else:
            str_rome += convert_10_to_rome(s[0] * s[1])
            i = 3

    # 10の位
    if i == 3:
        s = num_ord_list[i]
        str_rome += convert_10_to_rome(s[0] * s[1])

    return str_rome

print(convert_10_to_exrome(int(input('Input (10進数) >'))))
