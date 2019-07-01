import numpy as np
import scipy as sp
import math
import common

# (5) 解答です

def __main():
    with open('out5.txt', 'r', encoding='utf-8') as f:
        line = f.read().split('\n')[:-1]

    # 分割
    template_list = common.vertical_split(line)

    # 空行削除
    template_list = [common.trim_spacerow(num) for num in template_list]

    # 表示
    num_list = [common.most_likely(t) for t in template_list]
    print(''.join([str(n) for n in num_list]))

    return

if __name__ =='__main__':
    __main()
