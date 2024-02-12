import numpy as np
import Dice
import Win_scene
import Color as C
from datetime import datetime
class Player:                                               #player började som en lista med en egenskap name men det bara växte och växte fick motviligt byta till class, men det visade sig vara väldigt användbart
    def __init__(self, name, color):                        #attributen för player class listas här de flesta behövs senare för statestiken
        self.name = name
        self.color = color
        self.colored_name = f"{color}{name}"
        self.score = 0
        self.turns_to_win = 0
        self.dice_values = []
        self.accumulated_scores = []
        self.dice_counts = {i: 0 for i in range(1, 7)}      #för att underlätta statestiken sparas antalet av varie tärningsutfall ist'lle för att räkna ut det från dice_value senare
        self.date = datetime.now()
def add_players():                                          #Här tas spelarna in och den viktiga returnen "players" som sedan används överallt
    players = []
    while True:
        answer = input("\n" * 3 + "\n | How many players would like to play? (max 5pl) -> ")            # hur många ska spela
        try:                                                                                            #felhantering om man anger annat än nummer
            nr_players = int(answer)                                                                    #svaret blir en ny variabel och en integer
            if 1 <= nr_players <= 5:                                                                    # vilkor ges på antalsintervallet
                for player in range(nr_players):                                                        # en liten loop som itererar för varje spelare av antalet man angav
                    name = input(f" | Enter name for Player {player + 1}: -> ")                         #varje spelare får namn
                    name = name[:10]                                                                    # max 10 bostäver
                    color = C.colors[player % len(C.colors)]                                            # färg tilldelas från variabeln colors som ligger i filen Color.py (% operatorn går genom färgerna i variabeln gpt_ns hjälp)
                    players.append(Player(name, color))                                                 #Lista av players skapas med player objekt och dess attribut
                return players                                                                          # listan till export till de behövande
            else:
                print(f"   {nr_players}is invalid number. Please enter a number between 1 and 5")
        except ValueError:
            print(f"   {answer} is not a number. Please enter a number between 1 and 5")


def draw_track(players):                                                                              #Varje spelare får sin bana att raca på och i denna func skapas de,
    print(C.reset)
    print(C.bold + C.green + "\n" * 50 + "                           ---Welcome to the Race!---")
    print("        START          :> ============================== <: FINISHED\n" + C.reset)
    track_length = 30                                                                                    #varibel för banans längd
    player_tracks = {}                                                                                   # i denna dictonary ska all banor sparas
    for player in players:
        track = np.full(track_length, '-', dtype=object)                                         # hör skapas tom numpy array - representerar en tom bana
        track[0] = f"{player.color}X"                                                                    # start position som ett X på index 0 för varje spelare
        player_tracks[player.colored_name] = track                                                       # Här appendas dictonaryn
    return player_tracks


def print_tracks(player_tracks):                                                    # i denna lilla func skrivs varje spelares bana ut
    for player, track in player_tracks.items():
        print(f"        {player:<20}:> {''.join(track)}")


def player_turn(player, player_tracks):                                         #Här är allt som händer under en spelares "drag"
    print(f"\nIt's {player.colored_name}'s\033[0m turn! Press ENTER to roll")
    input()
    dice_roll = Dice.roll_dices()                                               #tärnings kast hämtas från filen dice.py
    player.dice_values.append(dice_roll)                                        # tärningskastet sparas
    player.score += sum(dice_roll)                                              # poängen räknas
    player.turns_to_win += 1                                                    # dragen räknas
    player.accumulated_scores.append(player.score)                              # samlar sammanlagd score för att lättare göra statestik
    player.dice_counts[dice_roll[0]] += 1                                       # samlar all spelarnas sammalagda tärnings utfall
    print(f"{player.colored_name}\033[0m rolled a {dice_roll}!")
    update_position(player, dice_roll, player_tracks)                           # Nästa funktion körs


def update_position(player, dice_roll, player_tracks):                                      #i denne func flyttas pjäserna X
    colored_X = f"{player.color}X"                                                          # X med spelarens förg
    current_position = np.where(player_tracks[player.colored_name] == colored_X)[0][0]      #np.where används för att hitta spelarens pos i arrayen
    player_tracks[player.colored_name][current_position] = '-'                              # den hittade pos. ersätts med -
    new_position = current_position + dice_roll                                             # ny index beräknas
    if new_position >= len(player_tracks[player.colored_name]):                             # kontroll görs om spelaren har gåt förbi max index
        input(f"{player.colored_name} wins!"
              f"\nPress ENTER to continue")
        player_tracks[player.colored_name][-1] = colored_X                                  # om vinst sätts X på sista pos
    else:
        player_tracks[player.colored_name][new_position] = colored_X                        # annars på den beräknade positionen

def play_game():                                                                            # Här sker själva spel loopen som startas i menyn Functionerna kalles efter hand
    players = add_players()
    player_tracks = draw_track(players)
    print_tracks(player_tracks)
    game_over = False
    while not game_over:
        for player in players:
            player_turn(player, player_tracks)
            print_tracks(player_tracks)
            if 'X' in player_tracks[player.colored_name][-1]:                               #Kontroll när spelet är slut
                winner = player                                                             # vinnare definieras
                Win_scene.win(players, winner)                                              # Här går vi vidare när spelet är slut
                game_over = True
                break

