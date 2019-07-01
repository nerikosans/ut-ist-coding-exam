import numpy as np
import scipy as sp
import math
import util

# (4) 解答です

def __main():
    image = util.Image('image2.txt')

    sorted_records = image.sorted_on_brightness()
    cell_count = image.cell_count()

    print(cell_count)

    k = 4
    target_ranks = [ int(i * cell_count / 4) for i in range(k)]
    print(target_ranks)

    target_records = [sorted_records[index] for index in target_ranks]
    target_cells = [(rec[0], image.get_cell(rec[0])) for rec in target_records]

    print('Q4 Result')
    for cell in target_cells:
        print(cell[0], cell[1].tuple())
    return

if __name__ =='__main__':
    __main()
