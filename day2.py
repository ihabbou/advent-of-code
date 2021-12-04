# https://adventofcode.com/2021/day/2

# %% Day 2 part 1


def move(instructions, position=(0, 0)):
    moves = [inst.split(" ") for inst in instructions]

    horizontal = [int(val) for move, val in moves if move == "forward"]
    depth = [(int(val) if move == "down" else -int(val)) for move, val in moves
             if move == "up" or move == "down"]
    return sum(horizontal), sum(depth)


# %% Day 2 part 2

from functools import reduce


def move_aim(instructions, position=[0, 0], aim=0):
    moves = [(inst.split(" ")[0], int(inst.split(" ")[1]))
             for inst in instructions]

    def adjust_pos(move, aim):
        mv, val = move
        if mv == "down":
            aim = aim + val
        elif mv == "up":
            aim = aim - val
        elif mv == "forward":
            pass
            #position[0] = position[0] + magnitude
            #position[1] = position[1] + (magnitude * aim)
        #return x, y, aim

    #(reduce(adjust_pos, moves, (*position, aim)))

    for move, val in moves:

        if move == "down":
            aim = aim + val
        elif move == "up":
            aim = aim - val
        elif move == "forward":
            position[0] += val  # hor
            position[1] += val * aim  # dept

    return position, aim
