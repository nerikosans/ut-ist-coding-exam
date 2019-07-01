import numpy as np
import scipy as sp
import math
import util

# (3) 解答です

def __main():
    image = util.Image('image1.txt')

    sorted_cells = image.sorted_on_brightness()
    cell_count = image.cell_count()

    target_index = sorted_cells[int(cell_count / 2)][0]
    target_cell = image.get_cell(target_index)

    print('Q3 Result: ', target_index, target_cell.tuple())

    return

if __name__ =='__main__':
    __main()
