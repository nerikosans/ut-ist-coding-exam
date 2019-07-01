import numpy as np
import scipy as sp
import math

# (2) だよ
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

convert_8_to_10()
