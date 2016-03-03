import random
from maze import Direction

def recursive_backtracking(maze, cy=0, cx=0):
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

            if maze.within_bounds(ny, nx) and maze.grid[ny, nx] == 0:
                maze.grid[y, x] += direction
                maze.grid[ny, nx] += direction.reverse()
                cells.append((y, x))
                cells.append((ny, nx))
                break
