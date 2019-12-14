"""Второе задание третей недели первого курса."""
import numpy as np
from scipy import optimize


def func(x: np.array) -> np.array:
    """Расчет значения функции для элементов массива."""
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)


def rounded_rez() -> str:
    """Округленный результат оптимизации."""
    result = optimize.differential_evolution(func, [(1, 30)])
    print(result)
    result = round(result["fun"][0], 2)
    return str(result)


if __name__ == '__main__':
    with open("submission-2.txt", "w") as file:
        file.write(rounded_rez())
