from utils import monte_carlo, plot


if __name__ == '__main__':
    def f(x):
        return x ** 2

    print("Значення інтегралу методом Монте-Карло:", monte_carlo(f))
    plot(f)