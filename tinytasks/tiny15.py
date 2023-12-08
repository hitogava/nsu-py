import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

size = 100
players = 100 * 10
iterations = 128


def alive(field, i, j):
    cnt = 0
    if i > 0:
        for k in range(j - 1, j + 2):
            if 0 <= k < size:
                cnt += field[i - 1][k]
    if i < size - 1:
        for k in range(j - 1, j + 2):
            if 0 <= k < size:
                cnt += field[i + 1][k]
    for k in range(j - 1, j + 2):
        if 0 <= k < size and k != j:
            cnt += field[i][k]

    return cnt


def iterate(f, prev: list):
    config = []
    for i in range(size):
        for j in range(size):
            n = alive(f, i, j)
            if f[i][j] == 0 and n == 3:
                f[i][j] = 1
                config.append((i, j, 1))
            elif f[i][j] == 1 and (n < 2 or n > 3):
                f[i][j] = 0
                config.append((i, j, 0))
    if all(f[i][j] == 0 for i in range(size)
           for j in range(size)) or config in prev:
        return 0
    prev.append(config)


def init_field():
    field = list()
    for i in range(size):
        field.append(list())
        field[i] = [0] * size
    for i in range(players):
        random.seed()
        x = random.randrange(0, size)
        y = random.randrange(0, size)
        field[x][y] = 1
    return field


def start_game(field):
    prev = [[]]
    for it in range(iterations):
        iterate(field, prev)


def benchmark(python_list, numpy_array):
    time_start = time.perf_counter()
    iterate(python_list, [[]])
    time_end = time.perf_counter()
    print(f"Python lists: {time_end - time_start}")
    time_start = time.perf_counter()
    iterate(numpy_array, [[]])
    time_end = time.perf_counter()
    print(f"Numpy lists: {time_end - time_start}")


field = init_field()
np_field = np.array(field)

fig, ax = plt.subplots()
matrix = ax.matshow(np_field)


def update(frame):
    if iterate(np_field, [[]]) == 0 or frame == iterations - 1:
        plt.pause(3)
        exit()
    matrix.set_data(np_field)


def animate():
    ani = FuncAnimation(fig, func=update, frames=iterations, interval=0.1)
    plt.show()


benchmark(field, np_field)
animate()
