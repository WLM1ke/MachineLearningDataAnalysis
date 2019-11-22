"""Первое задание третей недели первого курса."""
import numpy as np
from scipy import optimize


def func(x: np.array) -> np.array:
    """Расчет значения функции для элементов массива."""
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)


def rounded_rez(x: int) -> str:
    """Округленный результат оптимизации."""
    result = optimize.minimize(func, np.array(x), method="BFGS")
    print(result)
    result = round(result["fun"], 2)
    return str(result)


if __name__ == '__main__':
    rez = " ".join(map(rounded_rez, [2, 30]))
    with open("submission-1.txt", "w") as file:
        file.write(rez)
