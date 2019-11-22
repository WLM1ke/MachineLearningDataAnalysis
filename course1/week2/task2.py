"""Решение второго задания второй недели первого курса."""
import numpy as np
from scipy import linalg


def func(x: np.array) -> np.array:
    """Расчет значения функции для элементов массива."""
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)


def approx(x: np.array) -> np.array:
    """Приближение значений функции с помощью многочлена."""
    power = x.size
    a = (x.reshape(-1, 1) * np.ones(power)) ** np.arange(power)
    b = func(x)
    return linalg.solve(a, b)


if __name__ == '__main__':
    rez = approx(np.array([1, 4, 10, 15]))
    rez = " ".join(map(str, rez))

    with open("submission-2.txt", "w") as file:
        file.write(rez)
