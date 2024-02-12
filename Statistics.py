import pandas as pd
import matplotlib.pyplot as plt
import Menu
import Color as C
import warnings                                                  #Nu tror jag det funkar uten dessa men, Jag hade stora problem med matplotten som handlade förmodligen om att keylistener inte var korrekt avstängd
warnings.filterwarnings("ignore", category=UserWarning)   # och deras threads krockde på nåt sätt eller så var det nåt annat, fick warningar fast spelet kördes ändå, låter det vara på ett tag till


def game_statistics(players):                                               #statitstik som tar in player som inparameter
    game_data = {                                                           #Här kommer all data från player klassen som jag samlat på och läggas in i denna geme data dictoryn
        'Player': [player.name for player in players],
        'Score': [player.score for player in players],
        'Turns to Win': [player.turns_to_win for player in players],
        'Dice Values': [player.dice_values for player in players],
        'Date': [player.date for player in players]
            }
    df = pd.DataFrame(game_data)                                            #och framas in så att pandas älskar den
    # print(df)

    fig, axs = plt.subplots(3, 1, figsize=(15, 15))             # Skapar tre plots på ett "papper" för att få en bättre överblick och för att kunna presentera statistiken på ett finare sätt,

    # End Score                                                              # ett horizontelt stapel diagram som visar summan av alla tärningslagen för varje spelare
    axs[0].barh(df['Player'], df['Score'])
    axs[0].set_xlabel('Score')
    axs[0].set_ylabel('Player')
    axs[0].set_title('End Score')

    # Score Progress
    for player in players:                                                  # ett linje diagram som visar sammanlagda tärningsumman efter varje drag
        axs[1].plot(range(len(player.accumulated_scores)), player.accumulated_scores, label=player.name)

    axs[1].set_xlabel('Turn')
    axs[1].set_ylabel('Score')
    axs[1].set_title('Score Progress by Turn')
    axs[1].legend()

    # Dice Counts                                                           # ett cirkel diagram som visar alla tärningsutfall som slagits fördelade i procent
    total_dice_counts = {i: sum(player.dice_counts[i] for player in players) for i in range(1, 7)}
    axs[2].pie(list(total_dice_counts.values()), labels=range(1, 7), autopct='%1.1f%%')
    axs[2].set_title('Total Dice Roll Counts')

    plt.savefig('scores.png')                                               # här sparas en bild av den  senaste game statistiken , ta en kik
    save_game_statistics(df, filename='game_statistics.csv')                # hör startar func som sparar datafremet för varje game som spelats, den är underdådig just nu i framtiden ska den ha game id  so man särskillia de olika gamsen på ett bättre sätt
    plt.show()
    input("\nPress Enter to Continue"+C.reset)
    plt.close('all')                                                        #stänga ner all matplott , annars gillar den strula
    Menu.main_menu()

def save_game_statistics(df, filename='game_statistics.csv'):               #här är functionen som savar datafrem till csv fil
    df.to_csv(filename, mode='a', index=False)

def update_high_scores(winner, filename='high_scores.txt'):                          #Denna func sparar highscore i txt fil, jag fick den skriven av gpt förstår vad den görish, vilkorsdelen får ens huve att snurra runt
    high_scores = []

    try:
        with open(filename, 'r') as f:                                               #först laddas den in och bryts ner till strängar
            for line in f:
                name, turns, date = line.strip().split(',')
                high_scores.append((name, int(turns), date))
    except FileNotFoundError:
        pass

    if not high_scores or winner.turns_to_win < max(turns for name, turns, date in high_scores):   # om vilkoren tillgode ses så lägger vi till ny highscore
        high_scores.append((winner.name, winner.turns_to_win, winner.date.strftime("%Y-%m-%d")))

    high_scores.sort(key=lambda x: x[1])  #sortera efter index 1 alltså turns

    high_scores = high_scores[:15]        #bara 15 st får vara med

    with open(filename, 'w') as f:          #skriva det nya till fil
        for name, turns, date in high_scores:
            f.write(f'{name},{turns},{date}\n')



