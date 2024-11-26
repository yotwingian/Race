import Statistics
def win(players, winner):                           
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
    Statistics.update_high_scores(winner)                   
    Statistics.game_statistics(players)



