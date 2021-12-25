# https://adventofcode.com/2021/day/5

# %% Day 5 part 1

from typing import Counter


def intesection_points(input: str):

    pointpairs = [[tuple(map(int, p.split(","))) for p in l.split(" -> ")]
                  for l in input]

    def line_points(pair: tuple):
        (x1, y1), (x2, y2) = pair

        if x1 != x2 and y1 != y2:
            return []

        xrange = range(min(x1, x2), max(x1, x2) + 1)
        yrange = range(min(y1, y2), max(y1, y2) + 1)

        return [(x, y) for x in xrange for y in yrange]

    coverage = [line_points(pair) for pair in pointpairs]

    coverage = [pts for line in coverage for pts in line]

    ccount = Counter(coverage)
    return {k: v for k, v in ccount.items() if v >= 2}


input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".splitlines()

with open("input5.txt", "r") as f:
    input = f.readlines()
    result = intesection_points(input)
    print(result)
    print(len(result))
