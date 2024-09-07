import math

import numpy as np
from scipy.integrate import nquad


def f(z, y, x):
    return (x + y + z) / math.sqrt((2 * np.pow(x, 2) + 4 * np.pow(y, 2) + 5 * np.pow(z, 2)))


def zbounds(x, y):
    return [0, math.sqrt(1 - math.pow(x, 2) - math.pow(y, 2))]


def ybounds(x):
    return [0, math.sqrt(1 - math.pow(x, 2))]


def xbounds():
    return [0, 1]


I = nquad(lambda z, y, x: f(z, y, x), [zbounds, ybounds, xbounds])
print(I)
print(type(I))
