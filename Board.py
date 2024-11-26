import numpy as np
import Dice
import Win_scene
import Color as C
from datetime import datetime
class Player:                                              
    def __init__(self, name, color):                        
        self.name = name
        self.color = color
        self.colored_name = f"{color}{name}"
        self.score = 0
        self.turns_to_win = 0
        self.dice_values = []
        self.accumulated_scores = []
        self.dice_counts = {i: 0 for i in range(1, 7)}      
        self.date = datetime.now()
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
                    color = C.colors[player % len(C.colors)]                                            
                    players.append(Player(name, color))                                                 
                return players                                                                          
            else:
                print(f"   {nr_players}is invalid number. Please enter a number between 1 and 5")
        except ValueError:
            print(f"   {answer} is not a number. Please enter a number between 1 and 5")


def draw_track(players):                                                                              
    print(C.reset)
    print(C.bold + C.green + "\n" * 50 + "                           ---Welcome to the Race!---")
    print("        START          :> ============================== <: FINISHED\n" + C.reset)
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
    player.dice_values.append(dice_roll)                                        
    player.score += sum(dice_roll)                                              
    player.turns_to_win += 1                                                    
    player.accumulated_scores.append(player.score)                              
    player.dice_counts[dice_roll[0]] += 1                                       
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
                winner = player                                                             
                Win_scene.win(players, winner)                                              
                game_over = True
                break

