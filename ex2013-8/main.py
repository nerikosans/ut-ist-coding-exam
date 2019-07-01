import numpy as np
import scipy as sp
import math

# (1)

# R0内のdーpoints
def A_0(d):
    points_on_edge = math.floor(10 / d) + 1
    return math.pow(points_on_edge, 2)
# print (A_0(1))

# (2)
# R1内のd-points
def A_1(d):
    points_on_edge = math.floor(10 / d) + 1

    return sum ( [
        1 if (math.pow(d*p-5, 2) + math.pow(d*q-5, 2) <= 25) else 0
        for p in range(points_on_edge)
        for q in range(points_on_edge)
    ] )

    # for p in range(points_on_edge):
    #     for q in range(points_on_edge):
    #         if (math.pow(d*p-5, 2) + math.pow(d*q-5, 2) <= 25):
    #             p_in_circle+=1
    #
    # return p_in_circle

print (A_1(1))

# 比を計算
def f_2(d):
    return A_1(d) / A_0(d) / 4

# print(f_2(1))

# (3)

# K_n の辺の数
def K_edge_count(n):
    return 3 * math.pow(4, n)

# K_n の辺の長さ
def K_edge_len(n):
    return 10 / math.pow(3, int(n))

# K_nの一番小さい三角形の面積
def K_child_area(n):
    return math.sqrt(3) / 4 * math.pow(K_edge_len(n), 2)

# K_nの面積
def A_K(n):
    if (n == 0):
        return K_child_area(0)
    else:
        return A_K(n-1) + K_child_area(n) * K_edge_count(n-1)

# print (K_edge_len(0))
# print (K_child_area(0))
# print (A_K(1) / A_K(0))
# print (A_K(2))

# (4)
def f_4(n):
    return(A_K(n))

print (f_4(50))
print (0.4 * math.sqrt(3) * 100)

# (5)
def is_in_triangle(x,y, X,Y,edge_len,upper=True):
    vec = (x-X, y-Y)
    if (upper):
        return (
            (0 <= vec[0] and vec[0] <= edge_len)
            and (
                (vec[0] <= edge_len/2 and vec[1] <= math.sqrt(3)*vec[0])
                or (vec[0] >= edge_len/2 and vec[1] <= math.sqrt(3)*(edge_len - vec[0]))
            )
        )
    else:
        return (
            (0 <= vec[0] and vec[0] <= edge_len)
            and (
                (vec[0] <= edge_len/2 and vec[1] >= (-1)*math.sqrt(3)*vec[0])
                or (vec[0] >= edge_len/2 and vec[1] >= (-1)*math.sqrt(3)*(edge_len - vec[0]))
            )
        )

def flake_children(X,Y, edge_len, upper=True):
    if (upper):
        return [
            (X + edge_len / 3, Y, edge_len/3, False),
            (X, Y + edge_len / math.sqrt(3), edge_len/3, False),
            (X + edge_len * 2 / 3, Y + edge_len / math.sqrt(3), edge_len/3, False)
        ]
    else:
        return [
            (X + edge_len / 3, Y, edge_len/3, True),
            (X, Y - edge_len / math.sqrt(3), edge_len/3, True),
            (X + edge_len * 2 / 3, Y - edge_len / math.sqrt(3), edge_len/3, True)
        ]

def nth_flake_children(n):
    if (n==0):
        return [(0,0,10,True)]
    else:
        children = [flake_children(*ch) for ch in nth_flake_children(n-1)]
        ret = []
        for ch_list in children:
            ret = ret + ch_list
        return ret

print (nth_flake_children(1))
print (nth_flake_children(2))

def is_in_K_0(x,y):
    return is_in_triangle(x,y, 0,0,10,True)

def is_in_K_1(x,y):
    if (is_in_K_0(x,y)):
        return True
    else:
        for child in flake_children(0,0,10,True):
            if (is_in_triangle(x,y,*child)):
                return True
        return False

def is_in_K(n, x, y):
    for i in range(n+1):
        for ch in nth_flake_children(i):
            if (is_in_triangle(x,y, *ch)):
                return True
    return False

def A_5(d, n):
    points = range(0 - d * (math.floor(20/d)), d * (math.floor(20/d) ), d)
    p_in = 0
    for p in points:
        for q in points:
            if (is_in_K(n, d*p, d*q)):
                p_in+=1
    return p_in

print (A_5(1,2))

# (6)
