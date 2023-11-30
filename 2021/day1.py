# %% Day 1

from functools import reduce


#reduce(lambda x, y: 1 if x < y else 0, measurements, 0)
def increase_amount(measurements):
    increased = [
        measurements[i] - measurements[i - 1] > 0
        for i in range(1, len(measurements))
    ]
    return sum(increased)


with open(r"C:\Users\Ihabb\Downloads\input.txt", "r") as f:
    measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    measurements = [int(m) for m in f.readlines()]
    result = increase_amount(measurements)
    print(result)

# %% Day 1 part 2


def increase_amount_window(measurements, window_size=3):
    increased = [
        measurements[i] < measurements[i + window_size]
        for i in range(len(measurements) - window_size)
    ]
    return sum(increased)
