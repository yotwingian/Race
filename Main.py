import Intro
import Menu


def main():
    first_game = True
    while True:
        if first_game:
            Intro.game_intro()
            first_game = False
        else:
            Menu.main_menu()


if __name__ == "__main__":
    main()
