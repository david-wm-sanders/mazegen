#!venv/bin/python
import random
import numpy as np
from enum import IntEnum
from datetime import datetime
from pathlib import Path
from PIL import Image

class Direction(IntEnum):
    Up = 1
    Down = 1 << 1
    Left = 1 << 2
    Right = 1 << 3

    def reverse(self):
        if self == Direction.Up:
            return Direction.Down
        elif self == Direction.Down:
            return Direction.Up
        elif self == Direction.Left:
            return Direction.Right
        elif self == Direction.Right:
            return Direction.Left
        else:
            return None

    @classmethod
    def from_num(cls, num):
        dirs = []
        for mask in cls:
            if num & mask == mask:
                dirs.append(mask)
        if dirs:
            return dirs
        else:
            return None

def get_tiles():
    p = Path("tiles")
    p_crossroad = p / "crossroad_10c.png"
    p_deadend = p / "deadend_10c.png"
    p_straight = p / "straight_10c.png"
    p_tjunction = p / "tjunction_10c.png"
    p_turn = p / "turn_10c.png"

    crossroad = Image.open(str(p_crossroad))
    deadend = Image.open(str(p_deadend))
    straight = Image.open(str(p_straight))
    tjunction = Image.open(str(p_tjunction))
    turn = Image.open(str(p_turn))

    tiles = {1: deadend, 2: deadend.rotate(180), 3: straight,
             4: deadend.rotate(90), 5: turn.rotate(180),
             6: turn.rotate(270), 7: tjunction.rotate(180),
             8: deadend.rotate(270), 9: turn.rotate(90), 10: turn,
             11: tjunction, 12: straight.rotate(270),
             13: tjunction.rotate(90), 14: tjunction.rotate(270),
             15: crossroad}

    return tiles

def within_bounds(grid, y, x):
    h, w = grid.shape
    if y >= 0 and y < h and x >= 0 and x < w:
        return True
    else:
        return False

def recursive_backtracking(grid, cy=0, cx=0):
    """
    Method:
    1. Choose a starting point in the field.
    2. Randomly choose a wall at that point and carve a passage through to the adjacent cell,
    but only if the adjacent cell has not been visited yet. This becomes the new current cell.
    3. If all adjacent cells have been visited, back up to the last cell that has uncarved walls and repeat.
    4. The algorithm ends when the process has backed all the way up to the starting point.
    """
    directions = list(Direction)
    transform = {Direction.Up: {"y": -1, "x": 0},
                 Direction.Down: {"y": 1, "x": 0},
                 Direction.Left: {"y": 0, "x": -1},
                 Direction.Right: {"y": 0, "x": 1}}
    cells = []
    cells.append((cy, cx))

    while cells:
        y, x = cells.pop()
        random.shuffle(directions)
        for direction in directions:
            ny = y + transform[direction]["y"]
            nx = x + transform[direction]["x"]

            if within_bounds(grid, ny, nx) and grid[ny, nx] == 0:
                grid[y, x] += direction
                grid[ny, nx] += direction.reverse()
                cells.append((y, x))
                cells.append((ny, nx))
                break

class Maze:
    def __init__(self, h=50, w=50, mazegenf=recursive_backtracking):
        g = (h, w)
        self.mazegenf = mazegenf
        self.grid = np.zeros(g, dtype=np.uint8)

    def generate(self):
        h, w = self.grid.shape
        self.mazegenf(self.grid)
        self.grid[0, 0] += Direction.Up
        self.grid[h-1, w-1] += Direction.Down

    def draw(self, output):
        h, w = self.grid.shape
        img = Image.new("RGB", (w*10, h*10), "white")
        tiles = get_tiles()
        for y in range(h):
            for x in range(w):
                v = self.grid[y, x]
                t = tiles[v]
                img.paste(t, (x*10, y*10))
        img.save(output)


m = Maze()
m.generate()
p = Path("maze_{0}.png".format(datetime.utcnow()))
m.draw(str(p))
