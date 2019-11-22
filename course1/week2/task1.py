"""Решение первого задания."""
import re
import itertools

import numpy as np
from scipy.spatial import distance

if __name__ == '__main__':
    with open("sentences.txt") as file:
        lines = file.readlines()
        lines = map(lambda x: x.lower(), lines)
        lines = map(lambda x: re.split("[^a-z]", x), lines)
        lines = map(lambda sentence: list(filter(lambda word: word, sentence)), lines)
        lines = list(lines)

    words = list(set(itertools.chain.from_iterable(lines)))

    matrix = np.zeros((len(lines), len(words)))
    for row, line in enumerate(lines):
        for col, word in enumerate(words):
            matrix[row, col] = len(list(filter(lambda x: x == word, line)))

    first = matrix[0]
    rez = []
    for row in matrix[1:]:
        rez.append(distance.cosine(first, row))

    rez = np.array(rez)
    rez = rez.argsort()[:2] + 1
    rez = " ".join(map(str, rez))

    with open("submission-1.txt", "w") as file:
        file.write(rez)
