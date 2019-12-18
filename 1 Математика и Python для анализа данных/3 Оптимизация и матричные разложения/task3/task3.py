"""Третее задание третей недели первого курса."""
import numpy as np
from scipy import optimize


def func(x: np.array) -> np.array:
    """Расчет значения функции для элементов массива."""
    return int(np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2))


def rounded_rez_bfgs(x: int) -> str:
    """Округленный результат оптимизации BFGS."""
    result = optimize.minimize(func, np.array(x), method="BFGS")
    print(result)
    result = round(result["fun"], 2)
    return str(result)


def rounded_rez_evolution() -> str:
    """Округленный результат эволюционной оптимизации."""
    result = optimize.differential_evolution(func, [(1, 30)])
    print(result)
    result = round(result["fun"], 2)
    return str(result)


if __name__ == '__main__':
    with open("submission-3.txt", "w") as file:
        file.write(f"{rounded_rez_bfgs(30)} {rounded_rez_evolution()}")
