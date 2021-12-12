# https://adventofcode.com/2021/day/4

# %% Day 4 part 1


def prep_bingo(input: str):
    import re
    bingo = [int(i) for i in input.splitlines()[0].split(",")]

    boards = [[int(i) for i in re.split("\W+", ln.strip())]
              for ln in input.splitlines()[1:] if ln != ""]

    return bingo, boards


import numpy as np


def bingo(bingo: list, boards: list):
    bingo = np.array(bingo)
    boards = np.array(boards)

    boards = boards.reshape(-1, 5, 5)
    marks = np.zeros(boards.shape)

    def calc_bingo(board, mark, last_num):
        board[np.where(mark == 1)] = 0
        return board.sum() * last_num

    for bing in bingo:

        marks[np.where(boards == bing)] = 1
        for board_idx, mark in enumerate(marks):

            # bingo in mark or mark.T
            if sum([
                    np.array_equal(ln, np.ones(5)) +
                    np.array_equal(lt, np.ones(5))
                    for ln, lt in zip(mark, mark.T)
            ]) > 0:
                return calc_bingo(boards[board_idx], mark, bing)

    return


input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
with open("input4.txt", "r") as f:
    input = "\n".join(f.readlines())
    print(bingo(*prep_bingo(input)))

# %%
