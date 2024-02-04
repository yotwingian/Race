import numpy as np
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
                return players, nr_players,
            else:
                print(f"{nr_players}is invalid number. Please enter a number between 1 and 5")
        except ValueError:
            print(f"{answer} is not a number. Please enter a number between 1 and 5")


players, nr_players = add_players() # för att få ut dessa variablar ur funktionen


def draw_track(players):
    track_length = 30
    player_tracks = {}
    for player in players:
        track = np.full(track_length, '-')
        track[3] = 'X'
        player_tracks[player["name"]] = track
    return player_tracks


def print_tracks(player_tracks):
    for player, track in player_tracks.items():
        # Replace the player's current position with 'X'
        print(f"{player}: {''.join(track)}")


player_tracks = draw_track(players)
print_tracks(player_tracks)


def start_game():
    pass




