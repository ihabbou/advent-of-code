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


## %% Day 7 part 2

input = """16,1,2,0,4,2,7,1,2,14""".splitlines()

with open("input7.txt", "r") as f:
    input = f.readlines()
    result = crab_alignment(prep_input(input))
    #print(result)
    print(sum(result))
