import Board

green = "\033[92m"
reset = "\033[0m"
bold = "\033[1m"


def main_menu():
    run = True
    while run:
        answer = input(green + bold + f"\n                         Escape from Earth \n" + reset + ""
                       + green + "                          1. Play The Game"
                                 "\n                          2. See Highscore"
                                 "\n                          3. How to play"
                                 "\n                          q. quitter"
                                 "\n                          -> " + reset + " ").strip()

        match answer.lower():
            case "1":
                Board.play_game()

            case "2":
                print("Not ready")

            case "3":
                print(" Not ready")

            case "q":
                print("Game shutting down!")
                return
            case _:
                print(f"'{answer}' is not a valid option pls chose between 1-5 or Q!")
