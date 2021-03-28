from numpy import *
import matplotlib.pyplot as plt

v = 2  # Vitesse
a = 2  # Rayon aimant
b = 2  # Rayon bobine
t = linspace(-10, 10, 1000)


def d(t, v=v):
    return abs(v * t)


def d_prime(v):
    return v


def h(a, b, d, t):
    return sqrt(a**2 - ((a**2 - b**2 + (d(t))**2) / (2 * d(t))))


def h_prime(a, b, d, d_prime, t):
    return (d_prime(t) * ((a**2 - b**2)**2 - (d(t))**4))/(2*(d(t))**3 * sqrt(2*(a**2-b**2) - ((a**2-b**2)**2 - ((d(t))**4))/((d(t))**4)))


def aire(a, b, d, d_prime, t):
    return ((h(a, b, d, t))**2 * h_prime(a, b, d, d_prime, t))/(sqrt(a**2 - (h(a, b, d, t))**2)) - \
           sqrt(a**2 - (h(a, b, d, t))**2) * h_prime(a, b, d, d_prime, t) \
        + (a * h_prime(a, b, d, d_prime, t))/(sqrt(1-((h(a, b, d, t))**2)/(a**2))) + \
        ((h(a, b, d, t)) ** 2 * h_prime(a, b, d, d_prime, t)) / (sqrt(b ** 2 - (h(a, b, d, t)) ** 2)) - \
           sqrt(b ** 2 - (h(a, b, d, t)) ** 2) * h_prime(a, b, d, d_prime, t) \
           + (b * h_prime(a, b, d, d_prime, t)) / (sqrt(1 - ((h(a, b, d, t)) ** 2) / (b ** 2)))


aire = -100 * 1.5 * aire(a, b, d, d_prime, t)

plt.plot(t, aire, label="$V_L$")
plt.xticks([])
plt.yticks([])
plt.xlabel("Temps")
plt.ylabel('Tension')
plt.legend()
plt.show()
