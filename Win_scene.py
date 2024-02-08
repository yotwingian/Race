import Statistics
reset = "\033[0m"
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

    input("\nPress ENTER to see Game Statistics\n"+reset)
    Statistics.game_statistics(players)


