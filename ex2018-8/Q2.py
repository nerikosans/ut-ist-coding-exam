import numpy as np
import scipy as sp
import math
import util

# (2) 解答です

def __main():

    # cell = util.Cell((255,255,255))
    # print(cell.is_white())

    image = util.Image('image1.txt')
    cell_count = image.cell_count()

    for width in range(1, cell_count):
        if (cell_count % width is not 0):
            continue

        result = None
        success = True
        # print('width ', width)
        for y in range(int(cell_count / width)):
            # print('y ', y)
            # print(image.get_cell((y+1) * width - 1).tuple())
            # print(image.get_cell((y+1) * width - 1).is_white())
            if not image.get_cell((y+1) * width - 1).is_white():
                success = False
                break

        if success:
            result = width
            print(result)

    return

if __name__ =='__main__':
    __main()
