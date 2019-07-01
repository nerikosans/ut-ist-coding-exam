import numpy as np
import scipy as sp
import math

# (4) だよ
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

convert_rome_to_10()
