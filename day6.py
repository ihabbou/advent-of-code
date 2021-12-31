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
        #print(newfish)
        state = np.concatenate([state, newfish])
        #print(f"spawner = {spawners}")
        #print(f"After +1 days:\t{state} \t {spawners[0]}")

        return state

    state = np.array(state)

    print("Initial state: ", state)
    for day in range(days):
        state = tick(state)
        print(f"After {day+1} days:\t{state}")
    return state


# %% Day 6 part 2

input = """3,4,3,1,2""".splitlines()

with open("input6.txt", "r") as f:
    input = f.readlines()
    result = lanternfish_spawner(prep_input(input), 80)
    print(result)
    print(len(result))
