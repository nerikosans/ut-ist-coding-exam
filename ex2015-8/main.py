import numpy as np
import scipy as sp
import math
# 19:00
# (1)
def convert_4_to_10():
    base = 4

    input_str = input('Input (4進数) >')
    num_pow = [
        (int(n), p)
        for (n,p) in
        zip(input_str, range(len(input_str)-1, -1, -1))
    ]

    num_10 = sum([
        n * math.pow(base, p)
        for (n,p) in num_pow
    ])

    print(int(num_10))
    return int(num_10)

# convert_4_to_10()

# (2)
def convert_8_to_10():
    base = 8
    mapper = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}

    input_str = input('Input (特殊8進数) >')
    input_mapped = map(lambda x: mapper[x], input_str)
    num_pow = zip( input_mapped, range(len(input_str)-1, -1, -1) )

    num_10 = sum([
        n * math.pow(base, p)
        for (n,p) in num_pow
    ])

    print(int(num_10))
    return int(num_10)

# convert_8_to_10()

# (3)
# MMXV

# (4)
def convert_rome_to_10():
    mapper = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}

    input_str = input('Input (ローマ数字) >')

    i = 0
    num_10 = 0
    while i < len(input_str):
        s = input_str[i]

        # 最後の桁
        if i == len(input_str)-1:
            num_10 += mapper[s]
            i += 1
        else:
            t = input_str[i+1]
            # 引き算例外？
            if (
                (s == 'I' and t in ('V', 'X'))
                or (s == 'X' and t in ('L', 'C'))
                or (s == 'C' and t in ('D', 'M'))
            ):
                num_10 += (mapper[t] - mapper[s])
                i+=2

            # 引き算例外ではない
            else:
                num_10 += mapper[s]
                i += 1

    print(num_10)
    return num_10

# convert_rome_to_10()

# (5)
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

# print(convert_10_to_rome(int(input('Input (10進数) >'))))

# (6)
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

    print(num_ord_list)
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

# (7)

def convert_eng_to_10():
    eng_dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90
    }

    eng_dict_order = {
        'hundred': 100,
        'thousand': 1000
    }

    input_str = input('Input (英語) >')

    words = input_str.split(' ')

    num_10 = 0
    temp = 0

    for w in words:
        if w in eng_dict:
            temp += eng_dict[w]
        elif w in eng_dict_order:
            num_10 += temp * eng_dict_order[w]
            temp = 0

    num_10 += temp

    print(num_10)
    return num_10

# convert_eng_to_10()
