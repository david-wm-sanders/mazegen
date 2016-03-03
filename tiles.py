from pathlib import Path
from PIL import Image

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

    tiles = {1: deadend,
             2: deadend.rotate(180),
             3: straight,
             4: deadend.rotate(90),
             5: turn.rotate(180),
             6: turn.rotate(270),
             7: tjunction.rotate(180),
             8: deadend.rotate(270),
             9: turn.rotate(90),
             10: turn,
             11: tjunction,
             12: straight.rotate(270),
             13: tjunction.rotate(90),
             14: tjunction.rotate(270),
             15: crossroad}

    return tiles
