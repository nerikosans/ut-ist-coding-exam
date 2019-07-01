import math
import numbers
import numpy as np
import decimal

decimal.getcontext().prec = 32

# (1)
def f_1 (x):
    if x <= 2:
        return 1
    else:
        return f_1(x-1) + f_1(x-2)

# print(f_1(10))

# (2)
def f_2(x):
    fib = [1,1]
    for i in range(2,x):
        fib.append(fib[i-1] + fib[i-2])

    return fib[x-1]

# print(f_2(50))

# (3)
def f_3(str1, str2):
    return int(str1) + int(str2)

input_3 = (
    '00123456789012345678901234567890',
    '00987654321098765432109876543210'
)

# print(f_3(*input_3))

# (4)
# print(f_2(140))

# (5)
input_5 = (
    '12345678901234567890123456789012',
    '02'
)
context = decimal.Context(prec=32)

def f_5(num, pow):
    num = decimal.Decimal(num)
    arr_pow = np.array([10])
    return context.multiply(num, context.power(10, int(pow) - 31))

# print (f_5(*input_5))

# (6)
def phi():
    ret = context.sqrt(5)
    ret = context.add(1, ret)
    ret = context.divide(ret, 2)
    return ret

# print(phi())

# (7)
def g_7(x):
    return (context.divide(context.power(phi(), int(x)), context.sqrt(5)))

# (8)
def f_8(x):
    fib = [1,1]
    diff = decimal.Decimal(0)
    diff_i = 0

    for i in range(2,x):
        fib.append(fib[i-1] + fib[i-2])
        diff_temp = context.abs(
            context.subtract(fib[i], g_7(i+1))
        )

        if (context.compare(diff_temp, diff) == 1):
            diff = diff_temp
            diff_i = i

    return diff_temp, diff_i

print(f_8(140))

print(f_2(140))
print(g_7(140))
