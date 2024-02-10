import Board
import Color as C



def main_menu():
    run = True
    while run:
        answer = input(C.green + C.bold + f"\n                         Escape from Earth \n" + C.reset + ""
                       + C.green + "                          1. Play The Game"
                                 "\n                          2. See Highscore"
                                 "\n                          3. How to play"
                                 "\n                          q. quitter"
                                 "\n                          -> " + C.reset + " ").strip()

        match answer.lower():
            case "1":
                Board.play_game()
                run = False

            case "2":
                print("Not ready")

            case "3":
                print(" Not ready")

            case "q":
                print("Game shutting down!")
                return False


            case _:
                print(f"'{answer}' is not a valid option pls chose between 1-5 or Q!")
