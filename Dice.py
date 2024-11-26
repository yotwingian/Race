import sys
from numpy.random import randint
import Color as C
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
        line = C.yellow + '    '.join(line[i] for line in map(dice_faces.get, dices)) + C.reset
        sys.stdout.write(line + '\n')





