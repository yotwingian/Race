import pandas as pd
import matplotlib.pyplot as plt


def game_statistics(players):
    game_data = {
        'Player': [player.colored_name for player in players],
        'Score': [player.score for player in players],
        'Turns to Win': [player.turns_to_win for player in players],
        'Dice Values': [player.dice_values for player in players]
    }

    df = pd.DataFrame(game_data)
    print(df)

    df['Player'] = df['Player'].str.replace('\033.*?m', '')

    plt.bar(df['Player'], df['Score'])
    plt.xlabel('Player')
    plt.ylabel('Score')
    plt.title('Scores by Player')
    plt.show()


    # print(stipped_df)
    # stipped_df['Player'] = stipped_df['Player'].str.replace('\033.*?m', '')
    stipped_df = pd.DataFrame(game_data)
    # plt.bar(df['Player'], df['Score'])
    # plt.xlabel('Player')
    # plt.ylabel('Score')
    # plt.title('Scores by Player')
    # plt.show()
 # Remove color codes from player names
