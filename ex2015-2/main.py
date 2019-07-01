import numpy as np
import scipy as sp
import math
from decimal import *
getcontext().prec = 64
context = Context(prec=64)

# 16:08
# (1)

# f(0) ~ f(n) までを計算
# 再帰するとオーバーフローとかしないかな..?
def f_list(n):
    nums = [1]
    mod = math.pow(2,24)

    while len(nums) <= n:
        nums.append(
            (161 * nums[len(nums) - 1] + 2457)
            % mod
        )
    return nums

# f(n) を計算
def f_1(n):
    return f_list(n)[n]

# print(f_1(100))

# (2)
# f(0) ~ f(99) までで偶数をカウント
# 毎回f(n) を計算するとO(n^2)
def f_2():
    return sum([
        1 if n % 2 == 0 else 0
        for n in f_list(99)
    ])

# print(f_2())

# (3)
# (f(0), 0) ~ (f(99), 99) まででカウント
# f(0) ~ f(99) => f_list(99)
# 0 ~ 99 => range(100)
def f_3():
    return sum([
        1 if (n % 2 == 0) and (i % 2 == 1) else 0
        for (n,i) in zip(f_list(99), range(100))
    ])

# print(f_3())

# (4)
# print(f_1(1000000))

# (5)
# g(0) ~ g(n) までを計算
def g_list(n):
    nums = [Decimal(1)]
    mod = context.power(2, 26)

    A = Decimal(1103515245)
    B = Decimal(12345)

    while len(nums) <= n:
        A_mul = context.multiply(A, nums[len(nums) - 1])
        A_mul_plus_B = context.add(A_mul, B)
        nums.append( context.power(A_mul_plus_B, 1, modulo=mod) )
    return nums
#
# print(g_list(2)[2])
# print(g_list(3)[3])

# (6)

# g(i) = 1 となる i を見つける
def find_1_in_g(n):
    prev = Decimal(1)
    mod = context.power(2, 26)

    A = Decimal(1103515245)
    B = Decimal(12345)

    for i in range(n):
        A_mul = context.multiply(A, prev)
        A_mul_plus_B = context.add(A_mul, B)
        prev = context.power(A_mul_plus_B, 1, modulo=mod)
        if (context.compare(Decimal(1), prev) == 0):
            return i + 1

        if (context.remainder(i, 10000000) == 0):
            print('Calc: ' + str(i))

    return None

# print(find_1_in_g(70000000))
# => 67108864

# (7)

def h_list(n):
    nums = [Decimal(1)]
    mod = context.power(2, 10)

    A = Decimal(1103515245)
    B = Decimal(12345)

    while len(nums) <= n:
        A_mul = context.multiply(A, nums[len(nums) - 1])
        A_mul_plus_B = context.add(A_mul, B)
        nums.append( context.power(A_mul_plus_B, 1, modulo=mod) )
    return nums

def verify_gh(n):
    for (g,h) in zip(g_list(n), h_list(n)):
        g_rem = context.remainder(g, Decimal(1024))
        # if (context.compare(Decimal(1), rem)) == 0:
        #     print('! :' + str(_))
        print(str(g_rem) + '\t' + str(h))

# h(i) = 1 となる i を見つける
def find_1_in_h(n):
    prev = Decimal(1)
    mod = context.power(2, 10)

    A = Decimal(1103515245)
    B = Decimal(12345)

    for i in range(n):
        A_mul = context.multiply(A, prev)
        A_mul_plus_B = context.add(A_mul, B)
        prev = context.power(A_mul_plus_B, 1, modulo=mod)
        if (context.compare(Decimal(1), prev) == 0):
            return i + 1
    return None

print(find_1_in_h(2000))
