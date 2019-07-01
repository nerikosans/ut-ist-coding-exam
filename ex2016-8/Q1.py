import numpy as np
import scipy as sp
import math
import common

# (1) 解答です

def print_single_line(num):
    line = []
    sp = common.space(5)
    for ch in str(num):
        digit = common.num_template(int(ch))
        line.append(digit)
        line.append(sp)

    line = line[:-1]
    line = common.concat_num(line)
    common.print_array(line, filename='out1.txt')

def __main():
    input_num = input('Input number > ')
    print_single_line(input_num)
    return

if __name__ =='__main__':
    __main()
