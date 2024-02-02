def game_intro():
    run = True
    while run:

      print("\n                                                        "
            "\n                                                          "
            "\n            ,agd888b,_  Y8, ___`  Ybga,                   "
            "\n           ,gdP""88888888baa,.""8b     888g,              "
            "\n         ,dP      ]888888888P'   Y     `888Yb,            "
            "\n       ,dP       ,88888888P   db,        8P  Yb,          "
            "\n      ,8        ,888888888b, d8888a            8,         "
            "\n     ,8'        d88888888888,88P ' a,          `8,        "
            "\n    ,8'         88888888888888PP                `8,       "
            "\n    d'          I88888888888P                    `b       "
            "\n    8           `8 88P  Y8P'                      8       "
            "\n    8            Y 8[  _                          8       "
            "\n    8               Y8d8b   Y a                   8       "
            "\n    8                    8d,   __                 8       "
            "\n    Y,                    ` 8bd888b,             ,P       "
            "\n    `8,                     ,d8888888baaa       ,8'       "
            "\n     `8,                    888888888888'      ,8'        "
            "\n      `8a                    8888888888I      a8'         "
            "\n       `Yba                  `Y8888888P'    adP'          "
            "\n          Yba                 `888888P'   adY             "
            "\n           ` Yba,             d8888P  ,adP '              "
            "\n              ` Y8baa,      ,d888P,ad8P '                 "
            "\n                   ``  YYba8888P  ''                      "
            "\n                                                          "
            "\n                 Escape from Earth                        ")

      answer = input(f"\nWelcome  What would you like to do \n"
                     "\n1. Play The Game"
                     "\n2. See Highscore"
                     "\n3. Options"
                     "\nq. quitter"
                     "\n-> ").strip()

      match answer.lower():
            case "1":
                  # game_start()
                  print("op1")
                  run = False
            case "2":
                  # highscore()
                  print("opt2")
                  run = False
            case "3":
                  # options()
                  print(" 3.")
                  run = False

            case "q":
                  print("Game shutting down!")
                  run = False
            case _:
                  print(f"'{answer}' is not a valid option pls chose between 1-5 or Q!")

game_intro()
