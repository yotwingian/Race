def play_game():
    pass
def add_players():
    players = []
    while True:
        answer = input("How many players would like to play? (max 5pl)")
        try:
            nr_players = int(answer)
            if 1 <= nr_players <= 5:
                for player in range(nr_players):
                    name = input(f"Enter name for Player {player + 1}: ")
                    players.append({"name": name})
                return players, nr_players, print(players)
            else:
                print(f"{nr_players}is invalid number. Please enter a number between 1 and 5")
        except ValueError:
            print(f"{answer} is not a number. Please enter a number between 1 and 5")


add_players()

def start_game():
    pass






