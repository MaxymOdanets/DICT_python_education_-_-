from BrainRPS import BrainRockPaperScissors

while True:
    win, bot_options = BrainRockPaperScissors.start()

    if win == -1:
        break
    elif win == 0:
        print("There is a draw {}".format(bot_options))
    elif win == 1:
        print("Well done. The computer chose {} and failed".format(bot_options))
    elif win == 2:
        print("Sorry, but the computer chose {}".format(bot_options))