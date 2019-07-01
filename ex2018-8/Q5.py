import numpy as np
import scipy as sp
import math
import util
import Q4

# (5) 解答です

def get_leaders(image, k=4):
    leaders = Q4.get_quantizes(image, k=k)

    leader_index = [l.index for l in leaders]

    print('p_0')

    for i in range(10):
        # クラスタ初期化
        clusters = [ [] for _ in range(k)]

        # 分類
        for cell in image.get_cells():
            if cell.index in leader_index:
                clus = leaders.index(cell)
            else:
                clus = util.find_nearest_index(cell, leaders)
            clusters[clus].append(cell)

        print([len(c) for c in clusters])

        # 平均を出す
        means = [util.calc_mean(clus) for clus in clusters]

        # 最近接画素決定
        new_leaders = []
        for (mean, cluster) in zip(means, clusters):
            mean_cell = util.Cell(mean, 0)
            nearest_index = util.find_nearest_index(mean_cell, cluster)
            new_leaders.append(cluster[nearest_index])

        # 代表値更新
        print('p_', i+1)
        # print(new_leaders[0].index)
        leaders = new_leaders
        leader_index = [l.index for l in leaders]

    return leaders

def __main():
    k = 2
    image = util.Image('image2.txt')
    leaders = get_leaders(image, k)

    print(leaders[0].tuple())
    print(leaders[1].tuple())
    # print(leaders[80].tuple())
    # print(leaders[120].tuple())
    # k = 8
    # image = util.Image('image3.txt')
    # leaders = get_leaders(image, k)
    #
    # print(leaders[2].tuple())
    # print(leaders[4].tuple())
    # print(leaders[6].tuple())

if __name__ =='__main__':
    __main()
