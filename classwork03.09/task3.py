from scipy.integrate import quad

A = 2
def impulse(x):
    if 0 <= x <= 1:
        return A
    else:
        return 0


I = quad(impulse, -1, 2)
print(I)
