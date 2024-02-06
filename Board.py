import numpy as np
from pynput import keyboard
import Dice
import Win_scene

colors = ["\033[95m", "\033[92m", "\033[94m", "\033[96m", "\033[93m"]
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
                    colored_name = f"{color}{name}"
                    players.append({"name": name, "score": 0, "color": color, "colored_name": colored_name})
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
        track[0] = f"{player['color']}X"
        colored_name = player['colored_name']
        player_tracks[colored_name] = track
    return player_tracks


def print_tracks(player_tracks):
    for player, track in player_tracks.items():
        print(f"        {player:<20}:> {''.join(track)}")

def player_turn(player, player_tracks):
    print(f"\nIt's {player['colored_name']}'s\033[0m turn! Press ENTER to roll")
    input()
    dice_roll = Dice.roll_dices()
    print(f"{player['colored_name']}\033[0m rolled a {dice_roll}!")
    update_position(player, dice_roll, player_tracks)



             # Update player's position on the track based on the dice roll
def update_position(player, dice_roll, player_tracks):
    # Use the player's colored name as the key
    colored_name = player['colored_name']
    colored_X = f"{player['color']}X"
    # Find the current position of the player
    current_position = np.where(player_tracks[colored_name] == colored_X)[0][0]
    # Remove the 'X' from the current position
    player_tracks[colored_name][current_position] = '-'
    # Update the player's position based on their roll
    new_position = current_position + dice_roll
    # If the new position is beyond the end of the track, the player wins
    if new_position >= len(player_tracks[colored_name]):
        input(f"{colored_name} wins!"
              f"\nPress ENTER to continue")
        player_tracks[colored_name][-1] = colored_X  # Keep the 'X' at the last position
    else:
        # Otherwise, update the player's position on their track
        player_tracks[colored_name][new_position] = colored_X



def play_game():
    players, nr_players = add_players()
    player_tracks = draw_track(players)
    print_tracks(player_tracks)
    game_over = False
    while not game_over:
        for player in players:
            player_turn(player, player_tracks)
            print_tracks(player_tracks)
            colored_name = player['colored_name']
            if 'X' in player_tracks[colored_name][-1]:
                Win_scene.win()

                game_over = True
                break

            # if player_tracks[player] >=30:
            #     game_over = True

            # Check if the game is over
            # if game_over_condition:  # Replace with your game over condition
            #     game_over = True
            #     break


