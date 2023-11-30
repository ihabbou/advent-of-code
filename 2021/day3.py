# https://adventofcode.com/2021/day/3

# %% Day 3 part 1


def gamma_and_epsilon(input):

    import numpy as np
    input = [list(i) for i in input]

    cols = np.array(input).T
    cols = cols.astype(np.int)

    gamma = int("".join([str(np.bincount(row).argmax()) for row in cols]), 2)
    epsilon = int("".join([str(np.bincount(row).argmin()) for row in cols]), 2)

    return (gamma, epsilon)


with open(r"input.txt", "r") as f:
    inputs = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    inputs = [m.strip() for m in f.readlines()]
    result = gamma_and_epsilon(inputs)
    print(result[0] * result[1])
