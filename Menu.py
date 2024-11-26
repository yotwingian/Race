import Board
import Color as C


def main_menu():                                                                                                
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
                show_high_scores()
                run = False

            case "3":
                how_to_play()
                run = False

            case "q":
                print("Game shutting down!")
                return False

            case _:                                                                                                
                print(f"'{answer}' is not a valid option pls chose between 1-3 or q!")


def how_to_play():                                                                                                  
    input(C.bold + "\n     In this race game your goal is to reach the finish before anyone else."
                   "\n     When your turn comes you roll the dice and your piece marked by an X moves."
                   "\n     After each game you can enjoy some cool game statistics\n"
          + C.green + "\n                     Press Enter to continue..." + C.reset)
    main_menu()


def show_high_scores(filename='high_scores.txt'):                                                     
    try:                                                                                              
        with open(filename, 'r') as f:                                                                
            print(C.cyan + "\nHigh Scores:")
            print("{:<20} {:<15} {:<10}".format('Player', 'Turns to Win', 'Date'))              
            for line in f:
                name, turns, date = line.strip().split(',')
                print("{:<20} {:<15} {:<10}".format(name, turns, date))                         
    except FileNotFoundError:
        print("No high scores yet!")

    input(C.green + "\n       Press Enter to return" + C.reset)
    main_menu()
