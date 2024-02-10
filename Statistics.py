import pandas as pd
import matplotlib.pyplot as plt
import Menu


def game_statistics(players):
    game_data = {
        'Player': [player.name for player in players],
        'Score': [player.score for player in players],
        'Turns to Win': [player.turns_to_win for player in players],
        'Dice Values': [player.dice_values for player in players]
    }
    df = pd.DataFrame(game_data)
    print(df)

    fig, axs = plt.subplots(3, 1, figsize=(15, 15))  # Create a figure with 2 subplots

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
    plt.show()

    plt.savefig('scores.png')
    plt.show()

    # plt.subplots_adjust(hspace=5)
    # plt.tight_layout(pad=2)  # Adjust the padding between and around the subplots

    # plt.bar(df['Player'], df['Score'])
    # plt.xlabel('Player')
    # plt.ylabel('Score')
    # plt.title('Scores by Player')
    # # plt.show()
    #
    # # plt.style.use('dark_background')
    # # New code to plot score progress for each player
    # for player in players:
    #     flat_dice_values = [item for sublist in player.dice_values for item in sublist]
    #     plt.plot(range(len(flat_dice_values)), [sum(flat_dice_values[:i + 1]) for i in range(len(flat_dice_values))],
    #              label=player.name)
    #
    # plt.xlabel('Turn')
    # plt.ylabel('Score')
    # plt.title('Score Progress by Turn')
    # plt.legend()
    # plt.show()

    input("\nPress Enter to exit")
    Menu.main_menu()
# If you want to see the plots in the correct size within PyCharm, you could try using an external viewer for matplotlib plots. You can change this setting in PyCharm as follows:
#
# Go to File > Settings > Tools > Python Scientific.
# Uncheck the box that says Show plots in tool window.
