from pynput import keyboard 
import sys
import time
import Menu
import Color as C


def print_slow(text, delay=0.08):  

    for char in text:
        sys.stdout.write(char)  
        sys.stdout.flush() 
        time.sleep(delay)  


intro = C.bold + "\n    Earth 2078.......\n \n    Pollution has made Earth almost uninhabitable, and people are literally choking to death.\n    But there is a way out: the new Tesla colony at Alpha Centauri.\n    The decadent Earth society is arranging monthly competitions,\n    and the prize is a ticket on the last ship from Earth heading for Alpha Proxima.\n    You have been chosen for the escape race.\n    Are you ready?.........\n                                          Press space"


def game_intro():                       
    print_slow(intro,
               0.08)              
    listener = keyboard.Listener(suppress=True, on_press=None)  
    def on_press(
            key):                     
        if key == keyboard.Key.space:
            print("\n" * 100 + C.blue + "                                                                            "
                                        "\n                      , v y va88   8 v  8,,                              "
                                        "\n      " + C.yellow + "*" + C.blue + "            ,gd 88b,_  Y8, ___`    Ybga,                 " + C.yellow + "*" + C.blue + "              "
                                                                                                                                                                       "\n                 ,gd   8888888baa,.""8b      888g,                        "
                                                                                                                                                                       "\n               ,dP      ]888888888P'   Y     `888Yb,     " + C.yellow + "*" + C.blue + "                 "
                                                                                                                                                                                                                                                                 "\n    *        ,dP       ,88888888P   db,        8P  Yb,                   "
                                                                                                                                                                                                                                                                 "\n            ,8        ,888888888b, d8888a            8,                   "
                                                                                                                                                                                                                                                                 "\n " + C.yellow + "*" + C.blue + "         ,8'        d88888888888,88P ' a,          `8,                  "
                                                                                                                                                                                                                                                                                                   "\n          ,8'         88888888888888PP                `8,                 " + C.yellow + "*" + C.blue + ""
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
                                                                                                                                                                                                                                                                                                                                                                                                              "\n                         ``  YYba8888P  ''                  / ooo |  " + C.reset + "     ")

            listener.stop()

    listener.on_press = on_press
    listener.start()
    listener.join()                   
    Menu.main_menu()                  
