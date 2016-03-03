#!venv/bin/python
from datetime import datetime
from pathlib import Path
from maze import Maze
from gen import recursive_backtracking

m = Maze()
m.generate(recursive_backtracking)
p = Path("maze_{0}.png".format(datetime.utcnow()))
m.draw(str(p))
