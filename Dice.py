
import pandas as pd
import sys
import numpy as np
from numpy.random import randint
from pynput import keyboard
yellow = "\033[93m"
reset = "\033[0m"
green = "\033[92m"
bold = "\033[1m"
def roll_dices(a, kept_values=None):
    if kept_values is None:
        kept_values = [None] * a
    dices = [kept if kept is not None else randint(1, 7) for kept in kept_values]
    draw_dice(dices)
    return dices

def draw_dice(dices, kept=None):
    if kept is None:
        kept = [False] * len(dices)  # By default, no dice are kept
    dice_faces = {
        1: [" _______ ", "|       |", "|   o   |", "|       |", "'-------'"],
        2: [" _______ ", "| o     |", "|       |", "|     o |", "'-------'"],
        3: [" _______ ", "| o     |", "|   o   |", "|     o |", "'-------'"],
        4: [" _______ ", "| o   o |", "|       |", "| o   o |", "'-------'"],
        5: [" _______ ", "| o   o |", "|   o   |", "| o   o |", "'-------'"],
        6: [" _______ ", "| o   o |", "| o   o |", "| o   o |", "'-------'"]
    }
    for i in range(5):
        line = '    '.join(
            (green if keep else yellow) + line[i] + reset for line, keep in zip(map(dice_faces.get, dices), kept))
        sys.stdout.write(line + '\n')


def roll(r):
    print(bold, green + "                    Press space for roll!")

    def on_press(key):
        if key == keyboard.Key.space:
            output = roll_dices(r)
            print(green + '  keep 1       keep 2       keep 3       keep 4       keep 5')
            print(
                reset + "\n     Chose witch dices to keep" + green + " use keys 1-5 to keep " + reset + "your dicees"
                                                                                                        "\n                Press space for another roll"
                                                                                                        "\n                Press Enter to submit result"
                                                                                                        "\n                                                    q = quitter" + reset)
            print(roll)
            roll_choice(output)
            return False
        elif key == keyboard.KeyCode(char='q'):
            print('Quitting...')
            return False

    with keyboard.Listener(suppress=True, on_press=on_press) as listener:
        listener.join()