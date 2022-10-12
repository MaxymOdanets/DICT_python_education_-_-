import random
from random import choice

print("HANGMAN\nThe game will be available soon.")
words = ["python" , "java" , "php" , "html"]
word = random.choice(words)
a = input("Guess the word :\n>")
while True:
    if a == word:
        print("You survived!")
        break
    else:
        print("You lost!")
        break
