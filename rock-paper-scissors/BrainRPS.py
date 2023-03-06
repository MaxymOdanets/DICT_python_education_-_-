import random

class BrainRockPaperScissors:
    @staticmethod
    def start():
        bot_options_list = ['rock', 'paper', 'scissors']
        bot_options = random.choice(bot_options_list)
        option = input("type your symbol\n>")
        if bot_options == 'rock':
            return BrainRockPaperScissors.bot_choose_rock(bot_options, option), bot_options
        elif bot_options == 'paper':
            return BrainRockPaperScissors.bot_choose_paper(bot_options, option), bot_options
        elif bot_options == 'scissors':
            return BrainRockPaperScissors.bot_choose_scissors(bot_options, option), bot_options

    @staticmethod
    def bot_choose_rock(bot_options, option):
        if bot_options == option:
            win = 0
        elif bot_options == 'rock' and option == 'paper':
            win = 1
        elif bot_options == 'rock' and option == 'scissors':
            win = 2
        return win

    @staticmethod
    def bot_choose_paper(bot_options, option):
        if bot_options == option:
            win = 0
        elif bot_options == 'paper' and option == 'scissors':
            win = 1
        elif bot_options == 'paper' and option == 'rock':
            win = 2
        return win

    @staticmethod
    def bot_choose_scissors(bot_options, option):
        if bot_options == option:
            win = 0
        elif bot_options == 'scissors' and option == 'rock':
            win = 1
        elif bot_options == 'scissors' and option == 'paper':
            win = 2
        return win