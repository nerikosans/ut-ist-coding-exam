import numpy as np
import scipy as sp
import math

WHITE = (255,255,255)

# utilです 解答です
def load_image(filename):
    with open(filename, 'r') as f:
        text = f.read()

    nums = text.split(' ')
    cell_count = int(len(nums) / 3)
    image = []
    for i in range(cell_count):
        image.append(Cell(nums[3*i : 3*i + 3], i))
    return image

# 画素
class Cell(object):
    """docstring for Cell."""
    def __init__(self, values, index):
        super(Cell, self).__init__()
        self.r = int(values[0])
        self.g = int(values[1])
        self.b = int(values[2])
        self.index = index

    def tuple(self):
        return (self.r, self.g, self.b)

    def is_white(self):
        return self.tuple() == WHITE

    def brightness(self):
        return (self.r * self.r + self.g * self.g + self.b * self.b)

    # 距離
    def distance(self, cell):
        return (
            abs(self.r - cell.r) +
            abs(self.g - cell.g) +
            abs(self.b - cell.b)
        )

# 画像
class Image(object):
    """docstring for Image."""
    def __init__(self, filename):
        super(Image, self).__init__()
        self.image = load_image(filename)

    # 画素数
    def cell_count(self):
        return len(self.image)

    # ある位置の画素
    def get_cell(self, index):
        return self.image[index]

    def get_cells(self):
        return self.image

    # 輝度ソート
    def sorted_on_brightness(self):
        cells = self.image.copy()
        cells = list(zip(range(self.cell_count()), cells))

        brights = [
            (i, c.brightness())
            for (i, c) in cells
        ]

        brights.sort(key=lambda v: v[0], reverse=True)
        brights.sort(key=lambda v: v[1])

        return brights

class Cluster(object):
    """docstring for Cluster."""
    def __init__(self, cells):
        super(Cluster, self).__init__()
        self.cells = cells

# 与えられたなかで一番近いもの
def find_nearest_index(cell, leaders):
    min_dist_leader = min(leaders, key=lambda l: cell.distance(l))
    min_dist = cell.distance(min_dist_leader)

    near_leaders = list(filter(lambda l: cell.distance(l) == min_dist, leaders))

    near_leaders.sort(key=lambda l: l.index, reverse=True)
    nearest = near_leaders[0]

    return leaders.index(nearest)

def calc_mean(cluster):
    count = len(cluster)

    res = (0,0,0)

    for cell in cluster:
        res = (res[0] + cell.r, res[1] + cell.g, res[2] + cell.b)

    return tuple([
        math.floor(res[0] / count),
        math.floor(res[1] / count),
        math.floor(res[2] / count),
        ])
