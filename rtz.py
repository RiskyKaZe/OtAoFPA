import math


def rtz(num, m):

    if num > 0:
        rounded_num = math.floor(num)
        if rounded_num >= (2 ** (m + 1)):
            rounded_num = rounded_num - (rounded_num % 2)

    elif num < 0:
        rounded_num = math.ceil(num)
        if rounded_num <= (2 ** (m + 1)):
            rounded_num = rounded_num + (rounded_num % 2)

    else:
        rounded_num = 0

    return rounded_num
