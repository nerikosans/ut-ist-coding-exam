import numpy as np
import scipy as sp
import math
import util

# (6) 解答です

def __main():
    image = util.Image('image2.txt')

    with open('header.txt') as f:
        header = f.read()

    header = header.replace('\n', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ',')

    header = header.split(',')
    # print(header)

    # print([hex(int(h)) for h in header])
    print(''.join([format(int(h), 'x') for h in header]))

    # print(image.cell_count())
    # 160000
    # 400 x 400

    return

if __name__ =='__main__':
    __main()

def update(self, values):
    self.r = int(values[0])
    self.g = int(values[1])
    self.b = int(values[2])
