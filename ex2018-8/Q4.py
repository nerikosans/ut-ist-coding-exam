import numpy as np
import scipy as sp
import math
import util

# (4) 解答です！

def get_quantizes(image, k=4):
    sorted_records = image.sorted_on_brightness()
    cell_count = image.cell_count()

    # print(cell_count)

    target_ranks = [ int(i * cell_count / k) for i in range(k)]
    # print(target_ranks)

    target_records = [sorted_records[index] for index in target_ranks]
    target_cells = [image.get_cell(rec[0]) for rec in target_records]

    return target_cells


def __main():
    image = util.Image('image2.txt')

    print('Q4 Result')
    for qua in get_quantizes(image, k=2):
        print (qua.index, qua.tuple())
    return

if __name__ =='__main__':
    __main()
