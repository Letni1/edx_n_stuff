from math import *


def polysum(n, s):
    area = (0.25*n*s**2)/tan(pi/n)
    per = (s*n)
    my_sum = area + per**2
    return round(my_sum, 4)


print(polysum(72, 79)) #check