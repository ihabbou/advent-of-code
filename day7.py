# https://adventofcode.com/2021/day/7

# %% Day 7 part 1

import numpy as np


def prep_input(input: list) -> list:
    return list(map(int, [i for i in input[0].split(",")]))


def crab_alignment(subs: list):

    med = np.median(subs)

    # print("Median: ", med)
    fuel = list(map(lambda x: abs(x - med), subs))

    return fuel


# %% Day 7 part 2


def crab_alignment_exp(subs: list):

    subs = np.array(subs)

    fueling = lambda x: np.sum(np.abs(subs - x) * (np.abs(subs - x) + 1) / 2)

    all_fueling = np.vectorize(fueling)(np.arange(0, len(subs)))

    return np.min(all_fueling)


def main():
    input = """16,1,2,0,4,2,7,1,2,14""".splitlines()
    with open("input7.txt", "r") as f:
        input = f.readlines()
        result = crab_alignment(prep_input(input))
        print(sum(result))
        result = crab_alignment_exp(prep_input(input))
        print(result)


if __name__ == "__main__":
    main()
