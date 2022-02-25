from tkinter import Grid
from tracemalloc import start
from numpy import absolute
from p5 import *
from typing import List
from spot import Spot


global cols, rows
cols = 50
rows = 50

global grid
grid = [[0 for i in range(rows)] for j in range(cols)]

global open_set, closed_set, path
open_set, closed_set, path = [], [], []


def heuristic(a, b):
    return absolute(a.i - b.i) + absolute(a.j - b.j)


def setup():
    width, height = 800, 800
    size(width, height)

    global w, h
    w, h = width / cols, height / rows

    for i in range(cols):
        for j in range(rows):
            grid[i][j] = Spot(i, j)

    for i in range(cols):
        for j in range(rows):
            grid[i][j].add_neighbors(grid, cols, rows)

    global start, end
    start = grid[0][0]
    end = grid[cols - 1][rows - 1]
    start.wall = False
    end.wall = False

    start.set_w_h(w, h)
    open_set.append(start)


def draw():
    no_solution = False
    if len(open_set) > 0:
        winner = 0
        for i in range(len(open_set)):
            if open_set[i].f < open_set[winner].f:
                winner = i

        current = open_set[winner]

        if current == end:
            no_loop()
            print("DONE!!")

        open_set.remove(current)
        closed_set.append(current)

        neighbors = current.neighbors
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            if neighbor not in closed_set and not (neighbor.wall):
                temp_g = current.g + 1

                new_path = False
                if neighbor in open_set:
                    if temp_g < neighbor.g:
                        neighbor.g = temp_g
                        new_path = True
                else:
                    neighbor.g = temp_g
                    new_path = True
                    open_set.append(neighbor)

                if new_path:
                    neighbor.h = heuristic(neighbor, end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.previous = current
    else:
        no_solution = True
        print("No Solution!!")
        no_loop()

    background(0)

    for i in range(cols):
        for j in range(rows):
            grid[i][j].show()

    for i in closed_set:
        i.show((255, 0, 0))

    for i in open_set:
        i.show((0, 255, 0))

    if not (no_solution):
        path = []
        temp = current
        path.append(temp)
        while temp.previous:
            path.append(temp.previous)
            temp = temp.previous
        for i in path:
            i.show((0, 0, 255))


if __name__ == "__main__":
    run(frame_rate=35)
