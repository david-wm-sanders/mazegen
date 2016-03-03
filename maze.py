import numpy as np
from enum import IntEnum
from PIL import Image
from tiles import get_tiles


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


class Maze:
    def __init__(self, h=50, w=50):
        g = (h, w)
        self.grid = np.zeros(g, dtype=np.uint8)

    def generate(self, mazegenf):
        h, w = self.grid.shape
        mazegenf(self)
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

    def within_bounds(self, y, x):
        h, w = self.grid.shape
        if y >= 0 and y < h and x >= 0 and x < w:
            return True
        else:
            return False
