#!venv/bin/python
"""
Maze Generator

Usage:
    mazegen.py make [<height>] [<width>] [-o FILE]
    mazegen.py (-h | --help)

Options:
    -h --help   Show help
    -o FILE     Output to FILE
"""
from datetime import datetime
from pathlib import Path
from docopt import docopt
from maze import Maze
from gen import recursive_backtracking


def main():
    args = docopt(__doc__)

    if args["make"]:
        print("Creating maze...")
        height = int(args["<height>"]) if args["<height>"] else 50
        width = int(args["<width>"]) if args["<width>"] else 50
        m = Maze(height, width)
        m.generate(recursive_backtracking)

        if args["-o"]:
            output_path = Path(args["-o"])
        else:
            output_path = Path("maze_{0}.png".format(datetime.utcnow()))

        print("Rendering maze...")
        m.draw(str(output_path))

    elif args["create"]:
        print("Not implemented...")


if __name__ == '__main__':
    main()
