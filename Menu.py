import Board

yellow = "\033[93m"
green = "\033[92m"
blue = "\033[94m"
cyan = "\033[96m"
purple = "\033[95m"
reset = "\033[0m"
bold = "\033[1m"


def main_menu():
    run = True
    while run:
        answer = input(green + bold + f"\n                         Escape from Earth \n" + reset + ""
                       + green + "\n                          1. Play The Game"
                                 "\n                          2. See Highscore"
                                 "\n                          3. Options"
                                 "\n                          q. quitter"
                                 "\n                        -> "+reset+" ").strip()

        match answer.lower():
            case "1":
                Board.play_game()
                run = False
            case "2":
                # highscore()
                print("opt2")
                run = False
            case "3":
                # options()
                print(" 3.")
                run = False

            case "q":
                print("Game shutting down!")
                run = False
            case _:
                print(f"'{answer}' is not a valid option pls chose between 1-5 or Q!")
