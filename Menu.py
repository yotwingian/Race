import Board
import Color as C


def main_menu():                                                                                                # Min huvudmenu här körs en loop men matchcases som leder till olika ställen
    run = True
    while run:                                                                                                  # Nör loopen körs gäller detta
        answer = input(C.green + C.bold + f"\n                         Escape from Earth \n" + C.reset + ""     #användaren får säga vad den vill och trycka på enter för att gå vidare med sitt val
                       + C.green + "                          1. Play The Game"
                                   "\n                          2. See Highscore"
                                   "\n                          3. How to play"
                                   "\n                          q. quitter"
                                   "\n                          -> " + C.reset + " ").strip()

        match answer.lower():                                                                                   # Valen sorteras som casese och olika funktoner startar vid olika val  + att while loopen avslutas
            case "1":
                Board.play_game()                                                                               # hit går vi efter denna fil
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

            case _:                                                                                                # felhantering ifall man inte väljer det som ör angivet
                print(f"'{answer}' is not a valid option pls chose between 1-3 or q!")


def how_to_play():                                                                                                  #en liten en func som med hjölp av input håller programmet stilla till enter trycks och lite info text visas sen går vi tbx till huvumenyn
    input(C.bold + "\n     In this race game your goal is to reach the finish before anyone else."
                   "\n     When your turn comes you roll the dice and your piece marked by an X moves."
                   "\n     After each game you can enjoy some cool game statistics\n"
          + C.green + "\n                     Press Enter to continue..." + C.reset)
    main_menu()


def show_high_scores(filename='high_scores.txt'):                                                     # Här visas highscore func. laddar in filen HS.txt som sparats vid tidigare games
    try:                                                                                              # felhantering tillsamans med except om filen eller innehållet i filen ör fel
        with open(filename, 'r') as f:                                                                #läser filen och ger den variabeln f
            print(C.cyan + "\nHigh Scores:")
            print("{:<20} {:<15} {:<10}".format('Player', 'Turns to Win', 'Date'))              # fick hjölp av gpt_n för att formatera en tabell fint
            for line in f:
                name, turns, date = line.strip().split(',')
                print("{:<20} {:<15} {:<10}".format(name, turns, date))                         # filen görs om till stängar och tilldelas de rätta attribsen
    except FileNotFoundError:
        print("No high scores yet!")

    input(C.green + "\n       Press Enter to return" + C.reset)
    main_menu()
