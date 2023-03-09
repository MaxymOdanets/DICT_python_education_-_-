import random

class BrainRockPaperScissors:
    @staticmethod
    def start():
        user_list = ['rock', 'paper', 'scissors', '!exit']
        bot_options_list = ['rock', 'paper', 'scissors']
        while True:
            option = input("type your symbol\n>")
            if option == '!exit':
                print("exiting game...")
                return -1, None
            elif option not in user_list:
                print("Invalid input, try again")
                continue
            bot_options = random.choice(bot_options_list)
            if bot_options == 'rock':
                return BrainRockPaperScissors.bot_choose_rock(bot_options, option), bot_options
            elif bot_options == 'paper':
                return BrainRockPaperScissors.bot_choose_paper(bot_options, option), bot_options
            elif bot_options == 'scissors':
                return BrainRockPaperScissors.bot_choose_scissors(bot_options, option), bot_options

    @staticmethod
    def bot_choose_rock(bot_options, option):
        win = None
        if bot_options == option:
            win = 0
        elif bot_options == 'rock' and option == 'paper':
            win = 1
        elif bot_options == 'rock' and option == 'scissors':
            win = 2
        return win

    @staticmethod
    def bot_choose_paper(bot_options, option):
        win = None
        if bot_options == option:
            win = 0
        elif bot_options == 'paper' and option == 'scissors':
            win = 1
        elif bot_options == 'paper' and option == 'rock':
            win = 2
        return win

    @staticmethod
    def bot_choose_scissors(bot_options, option):
        win = None
        if bot_options == option:
            win = 0
        elif bot_options == 'scissors' and option == 'rock':
            win = 1
        elif bot_options == 'scissors' and option == 'paper':
            win = 2
        return win