from random import random
from p5 import *


class Spot:
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j

        self.f = 0
        self.g = 0
        self.h = 0

        self.neighbors = []

        self.previous = None

        self.wall = False
        if random() < 0.3:
            self.wall = True

    def set_w_h(self, w_, h_):
        global w, h
        w = w_
        h = h_

    def show(self, col=(255, 255, 255)) -> None:
        if self.wall:
            fill(0)
            no_stroke()
            ellipse(
                self.i * w + w / 2,
                self.j * h + h / 2,
                w / 2,
                h / 2,
            )
        elif col:
            fill(*col)
            rect(self.i * w, self.j * h, w, h)

    def add_neighbors(self, grid, cols, rows):
        i = self.i
        j = self.j
        if i < cols - 1:
            self.neighbors.append(grid[i + 1][j])
        if i > 0:
            self.neighbors.append(grid[i - 1][j])
        if j < rows - 1:
            self.neighbors.append(grid[i][j + 1])
        if j > 0:
            self.neighbors.append(grid[i][j - 1])
        if i > 0 and j > 0:
            self.neighbors.append(grid[i - 1][j - 1])
        if i < cols - 1 and j > 0:
            self.neighbors.append(grid[i + 1][j - 1])
        if i > 0 and j < rows - 1:
            self.neighbors.append(grid[i - 1][j + 1])
        if i < cols - 1 and j < rows - 1:
            self.neighbors.append(grid[i + 1][j + 1])
