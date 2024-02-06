import numpy as np
import Dice
colors = ["\033[93m", "\033[92m", "\033[94m", "\033[96m", "\033[95m"]
reset = "\033[0m"


def add_players():
    players = []
    while True:
        answer = input("\n How many players would like to play? (max 5pl) -> ")
        try:
            nr_players = int(answer)
            if 1 <= nr_players <= 5:
                for player in range(nr_players):
                    name = input(f"Enter name for Player {player + 1}: -> ")
                    name = name[:10]
                    color = colors[player % len(colors)]
                    players.append({"name": name, "score": 0, "color": color})
                return players, nr_players,
            else:
                print("{nr_players}is invalid number. Please enter a number between 1 and 5")
        except ValueError:
            print(f"{answer} is not a number. Please enter a number between 1 and 5")


def draw_track(players):
    print(reset)
    track_length = 30
    player_tracks = {}
    for player in players:
        track = np.full(track_length, '-', dtype=object)
        track[0] = f"{player['color']}X" + reset
        colored_name = f"{player['color']}{player['name']}"
        player_tracks[colored_name] = track
    return player_tracks


def print_tracks(player_tracks):
    for player, track in player_tracks.items():
        print(f"        {player:<20}:> {''.join(track)}")

def player_turn(player, player_tracks):
    print(f"It's {player['color']}{player['name']}'s\033[0m turn!")
    dice_roll = Dice.roll_dices()
    print(f"{player['color']}{player['name']}\033[0m rolled a {dice_roll}!")
    # Update player's position on the track based on the dice roll
    # update_position(player, dice_roll, player_tracks)
def update_position(player, dice_roll, player_tracks):
    # Implement the logic for moving the player's marker on the track
    # based on the dice roll
    pass

def play_game():
    players, nr_players = add_players()
    player_tracks = draw_track(players)
    print_tracks(player_tracks)
    game_over = False
    while not game_over:
        for player in players:
            player_turn(player, player_tracks)
            print_tracks(player_tracks)
            # Check if the game is over
            # if game_over_condition:  # Replace with your game over condition
            #     game_over = True
            #     break


