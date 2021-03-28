from numpy import *

A = 2
R = 1200
C = 0.000001
omega = linspace(10, 500, 1000)


def formula(A, R, C, omega):
    return A / (cos(arctan(-R * C * omega)) - R * C * omega * sin(arctan(-R * C * omega)))


print(formula(A, R, C, omega))
