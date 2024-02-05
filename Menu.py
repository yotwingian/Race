import Board
def main_menu():
    run = True
    while run:
        answer = input(f"\nWelcome  What would you like to do \n"
                       "\n1. Play The Game"
                       "\n2. See Highscore"
                       "\n3. Options"
                       "\nq. quitter"
                       "\n-> ").strip()

        match answer.lower():
            case "1":
                players, nr_players = Board.add_players()
                player_tracks = Board.draw_track(players)
                Board.print_tracks(player_tracks)
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
