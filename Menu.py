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
                print(" Not ready")

            case "3":
                how_to_play()
                run = False

            case "q":
                print("Game shutting down!")
                return False

            case _:
                print(f"'{answer}' is not a valid option pls chose between 1-5 or Q!")


def how_to_play():
    input(C.bold + "\n     In this race game your goal is to reach the finish before anyone else."
                   "\n     When your turn comes you roll the dice and your piece marked by an X moves."
                   "\n     After each game you can enjoy some cool game statistics\n"
          + C.green + "\n                     Press Enter to continue..."+C.reset)
    main_menu()
