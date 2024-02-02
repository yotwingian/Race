def play_game():
    pass
def add_players():
    players = []
    while True:
        answer = input("How many players would like to play? (max 5pl)")
        try:
            answer = int(answer)
            if 1 <= answer <= 5:
                for player in range(answer):
                    players.append({"name": f"Player {player + 1}"})

                return players, print(players)
            else:
                print(f"{answer}is invalid number. Please enter a number between 1 and 5")
        except ValueError:
            print(f"{answer} is not a number. Please enter a number between 1 and 5")


add_players()
def draw_track():
    pass
def start_game():
    pass






