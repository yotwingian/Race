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
        # Write the line to the standard output
        sys.stdout.write(line + '\n')

roll_dices()


# def roll(r):
#     print(bold, green + "                    Press space for roll!")
#
#     def on_press(key):
#         if key == keyboard.Key.space:
#             output = roll_dices(r)
#             print(green + '  keep 1       keep 2       keep 3       keep 4       keep 5')
#             print(
#                 reset + "\n     Chose witch dices to keep" + green + " use keys 1-5 to keep " + reset + "your dicees"
#                                                                                                         "\n                Press space for another roll"
#                                                                                                         "\n                Press Enter to submit result"
#                                                                                                         "\n                                                    q = quitter" + reset)
#             print(roll)
#             roll_choice(output)
#             return False
#         elif key == keyboard.KeyCode(char='q'):
#             print('Quitting...')
#             return False
#
#     with keyboard.Listener(suppress=True, on_press=on_press) as listener:
#         listener.join()
