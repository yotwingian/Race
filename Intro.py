from pynput import keyboard
import sys
import time
import Menu

yellow = "\033[93m"
green = "\033[92m"
blue = "\033[94m"
cyan = "\033[96m"
purple = "\033[95m"
reset = "\033[0m"
bold = "\033[1m"


def print_slow(text, delay=0.1):
    # This function prints the text slowly with a given delay
    for char in text:
        sys.stdout.write(char)  # Write one character at a time
        sys.stdout.flush()  # Make sure it appears immediately
        time.sleep(delay)  # Wait for some time before printing the next character


intro = bold + "\n    Earth 2078.......\n \n    Pollution has made Earth almost uninhabitable, and people are literally choking to death.\n    But there is a way out: the new Tesla colony at Alpha Centauri.\n    The decadent Earth society is arranging monthly competitions,\n    and the prize is a ticket on the last ship from Earth heading for Alpha Proxima.\n    You have been chosen for the escape race.\n    Are you ready?.........\n                                          Press space"


# Print the intro slowly with a delay of 0.05 seconds
def game_intro():
    print_slow(intro, 0.05)

    listener = keyboard.Listener(suppress=True, on_press=None)

    def on_press(key):
        if key == keyboard.Key.space:
            print("\n" * 100 + blue + "                                                                            "
                                      "\n                      , v y va88   8 v  8,,                              "
                                      "\n      "+yellow+"*"+blue+"            ,gd 88b,_  Y8, ___`    Ybga,                 "+yellow+"*"+blue+"              "
                                      "\n                 ,gd   8888888baa,.""8b      888g,                        "
                                      "\n               ,dP      ]888888888P'   Y     `888Yb,     "+yellow+"*"+blue+"                 "
                                      "\n    *        ,dP       ,88888888P   db,        8P  Yb,                   "
                                      "\n            ,8        ,888888888b, d8888a            8,                   "
                                      "\n "+yellow+"*"+blue+"         ,8'        d88888888888,88P ' a,          `8,                  "
                                      "\n          ,8'         88888888888888PP                `8,                 "+yellow+"*"+blue+""
                                      "\n          d'          I88888888888P                    `b                 "
                                      "\n          8           `8 88P  Y8P'                      8                 "
                                      "\n          8            Y 8[  _                          8                 "
                                      "\n   *      8               Y8d8b   Y a                   8                 "
                                      "\n          8                    8d,   __                 8                 "
                                      "\n          Y,                    ` 8bd888b,             ,P      /|         "
                                      "\n          `8,                     ,d8888888baaa       ,8'     /  |        "
                                      "\n           `8,                    888888888888'      ,8'     / RO |       "
                                      "\n            `8a                    8888888888I      a8'       | ||        "
                                      "\n             `Yba                  `Y8888888P'    adP'        | ||        "
                                      "\n                Yba                 `888888P'   adY           | ||        "
                                      "\n                 ` Yba,             d8888P  ,adP '            |_||        "
                                      "\n                    ` Y8baa,      ,d888P,ad8P '              / 0 |        "
                                      "\n                         ``  YYba8888P  ''                  / ooo |       "
                                      "\n " + reset + "                                                            ")
            Menu.main_menu()
            listener.stop()

    listener.on_press = on_press
    listener.start()
    listener.join()
