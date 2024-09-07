# page 37 №6
import math

import matplotlib.pyplot as plt
import numpy as np


def plot_tailor(x_values, tailor_func, degree):
    y_values = []
    for x in x_values:
        y_values.append(tailor_func(x, degree))
    plt.plot(x_values, y_values)
    plt.show()


def sin_tailor(x, n=1):
    result = 0
    for k in range(n):
        result += pow(-1, k) * (pow(x, 2 * k + 1) / math.factorial(2 * k + 1))
    return result


degrees = [1, 3, 7, 20]
x_values = np.linspace(-2 * math.pi, 2 * math.pi, 1000)

for degree in degrees:
    plot_tailor(x_values, sin_tailor, degree)
