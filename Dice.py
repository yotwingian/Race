import sys
from numpy.random import randint
import Color as C
def roll_dices():                                           # i denna func rullas tärningen , kan ha fler tärningar om jag vill
    dices = [randint(1, 7) for _ in range(1)]
    draw_dice(dices)                                        # varför inte rita ett par tärningar
    return dices

def draw_dice(dices):                                       # idenna func. som ursprungligen var skapad för min yatzy ritas tärningen eller tärningarna ut
    dice_faces = {
        1: [" _______ ", "|       |", "|   o   |", "|       |", "'-------'"],
        2: [" _______ ", "| o     |", "|       |", "|     o |", "'-------'"],
        3: [" _______ ", "| o     |", "|   o   |", "|     o |", "'-------'"],
        4: [" _______ ", "| o   o |", "|       |", "| o   o |", "'-------'"],
        5: [" _______ ", "| o   o |", "|   o   |", "| o   o |", "'-------'"],
        6: [" _______ ", "| o   o |", "| o   o |", "| o   o |", "'-------'"]
    }
    for i in range(5):       # denna Loop är skapad av gpt_n tack gode gud, den tar in vilken diceside det blir och använder "" för att skapa samman de olika delarna ovan på varandra
        line = C.yellow + '    '.join(line[i] for line in map(dice_faces.get, dices)) + C.reset
        sys.stdout.write(line + '\n')





