# https://adventofcode.com/2021/day/6

# %% Day 6 part 1

import numpy as np


def prep_input(input: list) -> list:
    return list(map(int, [i for i in input[0].split(",")]))


def lanternfish_spawner(state: list, days: int):
    def tick(state: np.array):
        spawners = np.where(state == 0)
        state = state - 1
        newfish = np.ones(len(spawners[0]), dtype=np.int) * 8
        state[spawners] = 6
        state = np.concatenate([state, newfish])

        return state

    state = np.array(state)

    #print("Initial state: ", state)
    for day in range(days):
        state = tick(state)
    return state


# %% Day 6 part 2

from typing import Counter


def lanternfish_spawner_dyn(state: list, days: int):
    fishies = {d: 0 for d in range(9)}
    fishies = {**fishies, **Counter(state)}

    for day in range(days):
        spawns = fishies.get(0, 0)
        for d in fishies.keys():  # lower count for all
            if d - 1 != -1:
                fishies[d - 1] = fishies[d]
        fishies[6] = fishies[6] + spawns  # spawners go to 6
        fishies[8] = spawns  # new fish

    return fishies


input = """3,4,3,1,2""".splitlines()

with open("input6.txt", "r") as f:
    input = f.readlines()
    result = lanternfish_spawner(prep_input(input), 80)
    # print(result)
    print(len(result))
    result = lanternfish_spawner_dyn(prep_input(input), 256)
    # print(result)
    print(sum(result.values()))
