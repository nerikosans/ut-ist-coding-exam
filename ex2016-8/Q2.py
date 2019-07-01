import numpy as np
import scipy as sp
import math
import common

# (2) 解答です

def read_line(line):
    template_list = common.vertical_split(line)
    num_list = [common.template_to_num(t) for t in template_list]
    return num_list

def __main():
    with open('out1.txt', 'r', encoding='utf-8') as f:
        num_list = read_line(f.read().split('\n')[:-1])

    print(''.join([str(n) for n in num_list]))
    return

if __name__ =='__main__':
    __main()
