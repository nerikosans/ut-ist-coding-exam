import numpy as np
import scipy as sp
import math
import common

# (3) 解答です

def print_nice_line(instruction):
    inst = instruction.split(',')
    num_input = inst[0]

    mode = 'NUM'

    num_list = []

    for i in range(len(num_input)):
        ch = num_input[i]
        vert_offset = int(inst[2*i + 1])

        # 記号にする
        num = common.num_template(int(ch))
        # ずらす
        num = common.pull_down(num, offset=vert_offset)
        # 追加
        num_list.append(num)

        # 空白
        if i is not len(num_input)-1:
            hor_offset = int(inst[2*i + 2])
            num_list.append(common.space(cols=hor_offset))

    # print
    num_list = common.concat_num(num_list)
    common.print_array(num_list, filename='out3.txt')

def __main():
    input_text = input('Input instruction > ')
    print_nice_line(input_text)
    return

if __name__ =='__main__':
    __main()
