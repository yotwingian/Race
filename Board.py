import numpy as np
import Dice
import Win_scene

colors = ["\033[96m", "\033[93m", "\033[94m", "\033[95m", "\033[92m"]
reset = "\033[0m"
bold = "\033[1m"
magenta = "\033[35m"
green = "\033[32m"


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.colored_name = f"{color}{name}"
        self.score = 0
        self.turns_to_win = 0


def add_players():
    players = []
    while True:
        answer = input("\n" * 3 + "\n | How many players would like to play? (max 5pl) -> ")
        try:
            nr_players = int(answer)
            if 1 <= nr_players <= 5:
                for player in range(nr_players):
                    name = input(f" | Enter name for Player {player + 1}: -> ")
                    name = name[:10]
                    color = colors[player % len(colors)]
                    players.append(Player(name, color))
                return players
            else:
                print("   {nr_players}is invalid number. Please enter a number between 1 and 5")
        except ValueError:
            print(f"   {answer} is not a number. Please enter a number between 1 and 5")


def draw_track(players):
    print(reset)
    print(bold + green + "\n" * 50 + "                             ---Welcome to Race!---")
    print("\n        START          :> ============================== <: FINNISHED" + reset)
    track_length = 30
    player_tracks = {}
    for player in players:
        track = np.full(track_length, '-', dtype=object)
        track[0] = f"{player.color}X"
        player_tracks[player.colored_name] = track
    return player_tracks


def print_tracks(player_tracks):
    for player, track in player_tracks.items():
        print(f"        {player:<20}:> {''.join(track)}")


def player_turn(player, player_tracks):
    print(f"\nIt's {player.colored_name}'s\033[0m turn! Press ENTER to roll")
    input()
    dice_roll = Dice.roll_dices()
    print(f"{player.colored_name}\033[0m rolled a {dice_roll}!")
    update_position(player, dice_roll, player_tracks)


def update_position(player, dice_roll, player_tracks):
    colored_X = f"{player.color}X"
    current_position = np.where(player_tracks[player.colored_name] == colored_X)[0][0]
    player_tracks[player.colored_name][current_position] = '-'
    new_position = current_position + dice_roll
    if new_position >= len(player_tracks[player.colored_name]):
        input(f"{player.colored_name} wins!"
              f"\nPress ENTER to continue")
        player_tracks[player.colored_name][-1] = colored_X
    else:
        player_tracks[player.colored_name][new_position] = colored_X


def play_game():
    players = add_players()
    player_tracks = draw_track(players)
    print_tracks(player_tracks)
    game_over = False
    while not game_over:
        for player in players:
            player_turn(player, player_tracks)
            print_tracks(player_tracks)
            if 'X' in player_tracks[player.colored_name][-1]:
                Win_scene.win()
                game_over = True
                break

            # if player_tracks[player] >=30:
            #     game_over = True

            # Check if the game is over
            # if game_over_condition:  # Replace with your game over condition
            #     game_over = True
            #     break
