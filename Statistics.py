import pandas as pd
import matplotlib.pyplot as plt
import Menu
import Color as C
import warnings                                                  
warnings.filterwarnings("ignore", category=UserWarning)   


def game_statistics(players):                                               
    game_data = {                                                           
        'Player': [player.name for player in players],
        'Score': [player.score for player in players],
        'Turns to Win': [player.turns_to_win for player in players],
        'Dice Values': [player.dice_values for player in players],
        'Date': [player.date for player in players]
            }
    df = pd.DataFrame(game_data)                                            
    # print(df)

    fig, axs = plt.subplots(3, 1, figsize=(15, 15))             

    # End Score                                                              
    axs[0].barh(df['Player'], df['Score'])
    axs[0].set_xlabel('Score')
    axs[0].set_ylabel('Player')
    axs[0].set_title('End Score')

    # Score Progress
    for player in players:                                                  
        axs[1].plot(range(len(player.accumulated_scores)), player.accumulated_scores, label=player.name)

    axs[1].set_xlabel('Turn')
    axs[1].set_ylabel('Score')
    axs[1].set_title('Score Progress by Turn')
    axs[1].legend()

    # Dice Counts                                                          
    total_dice_counts = {i: sum(player.dice_counts[i] for player in players) for i in range(1, 7)}
    axs[2].pie(list(total_dice_counts.values()), labels=range(1, 7), autopct='%1.1f%%')
    axs[2].set_title('Total Dice Roll Counts')

    plt.savefig('scores.png')                                               
    save_game_statistics(df, filename='game_statistics.csv')                
    plt.show()
    input("\nPress Enter to Continue"+C.reset)
    plt.close('all')                                                       
    Menu.main_menu()

def save_game_statistics(df, filename='game_statistics.csv'):               
    df.to_csv(filename, mode='a', index=False)

def update_high_scores(winner, filename='high_scores.txt'):                          
    high_scores = []

    try:
        with open(filename, 'r') as f:                                               
            for line in f:
                name, turns, date = line.strip().split(',')
                high_scores.append((name, int(turns), date))
    except FileNotFoundError:
        pass

    if not high_scores or winner.turns_to_win < max(turns for name, turns, date in high_scores):   
        high_scores.append((winner.name, winner.turns_to_win, winner.date.strftime("%Y-%m-%d")))

    high_scores.sort(key=lambda x: x[1])  

    high_scores = high_scores[:15]        

    with open(filename, 'w') as f:          
        for name, turns, date in high_scores:
            f.write(f'{name},{turns},{date}\n')



