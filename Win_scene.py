import Statistics
def win(players, winner):                           #vinnare scenen printas här och sedan går vi till statistik filen
    print("\n" *50 +f"                {winner.name} YOU HAVE ESCAPED!!!")
    print("     /\\")
    print("    //\\\\")
    print("   ///\\\\\\")
    print("  ////\\\\\\\\")
    print(" /////\\\\\\\\\\")
    print("//////\\\\\\\\\\\\")
    print("||||||||||||")
    print("|||    ||| ||")
    print("|||    ||| ||")
    print("|||    ||| ||")
    print("|||    ||| ||")
    print("|||    ||| ||")
    print("|||    ||| ||")
    print("|||    ||| ||")
    print("|||    ||| ||")
    print("|||    ||| ||")
    print("|||    ||| ||")
    print("|||    ||| ||")
    print("|||    ||| ||")
    print("|||   ...")

    input("\nPress ENTER to see Game Statistics\n")
    Statistics.update_high_scores(winner)                   #Här startar func som savar high score
    Statistics.game_statistics(players)



