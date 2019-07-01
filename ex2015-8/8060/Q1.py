import numpy as np
import scipy as sp
import math

# (1) だよ
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

convert_4_to_10()
