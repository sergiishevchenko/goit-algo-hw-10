import matplotlib.pyplot as plt
import numpy as np


def plot(f, a=0, b=2, n=1000):
    x = np.linspace(a - 1, b + 1, n)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Integral of f(x) between {a} and {b}')
    plt.grid()
    plt.show()


def monte_carlo(f, a=0, b=2, number_points=1000000):
    random_x = np.random.uniform(a, b, number_points)
    random_y = np.random.uniform(0, max(f(random_x)), number_points)

    area_under_curve = sum(random_y <= f(random_x))
    rectangle_area = (b - a) * max(f(random_x))

    return rectangle_area * (area_under_curve / number_points)