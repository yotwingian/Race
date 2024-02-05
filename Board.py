import numpy as np

colors = ["\033[93m", "\033[92m", "\033[94m", "\033[96m", "\033[95m"]

def add_players():
    players = []
    while True:
        answer = input("How many players would like to play? (max 5pl)")
        try:
            nr_players = int(answer)
            if 1 <= nr_players <= 5:
                for player in range(nr_players):
                    name = input(f"Enter name for Player {player + 1}(max 10 characters): ")
                    name = name[:10]
                    players.append({"name": name, "score": 0})
                return players, nr_players,
            else:
                print(f"{nr_players}is invalid number. Please enter a number between 1 and 5")
        except ValueError:
            print(f"{answer} is not a number. Please enter a number between 1 and 5")


def draw_track(players):
    track_length = 30
    player_tracks = {}
    for player in players:
        track = np.full(track_length, '-')
        track[0] = 'X'
        player_tracks[player["name"]] = track
    return player_tracks


def print_tracks(player_tracks):
    for player, track in player_tracks.items():
        print(f"        0{player:<10}: {''.join(track)}")
