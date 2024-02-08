import sys
from numpy.random import randint
yellow = "\033[93m"
green = "\033[92m"
blue = "\033[94m"
cyan = "\033[96m"
purple = "\033[95m"
reset = "\033[0m"

bold = "\033[1m"
def roll_dices():
    dices = [randint(1, 7) for _ in range(1)]
    draw_dice(dices)
    return dices

def draw_dice(dices):
    dice_faces = {
        1: [" _______ ", "|       |", "|   o   |", "|       |", "'-------'"],
        2: [" _______ ", "| o     |", "|       |", "|     o |", "'-------'"],
        3: [" _______ ", "| o     |", "|   o   |", "|     o |", "'-------'"],
        4: [" _______ ", "| o   o |", "|       |", "| o   o |", "'-------'"],
        5: [" _______ ", "| o   o |", "|   o   |", "| o   o |", "'-------'"],
        6: [" _______ ", "| o   o |", "| o   o |", "| o   o |", "'-------'"]
    }
    for i in range(5):
        line = yellow + '    '.join(line[i] for line in map(dice_faces.get, dices)) + reset
        sys.stdout.write(line + '\n')





