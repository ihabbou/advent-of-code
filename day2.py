# %% Day 2


def move(instructions, position=(0, 0)):
    moves = [inst.split(" ") for inst in instructions]

    horizontal = [int(val) for move, val in moves if move == "forward"]
    depth = [(int(val) if move == "down" else -int(val)) for move, val in moves
             if move == "up" or move == "down"]
             
    return sum(horizontal), sum(depth) 
