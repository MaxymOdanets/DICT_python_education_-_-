import random
from random import choice

print("HANGMAN\nThe game will be available soon.")
words = ["python" , "java" , "javascript" , "html"]
word = random.choice(words)
length = '-' * len(word)
a = input("Guess the word :" + word[:3] + "-".join([''for _ in range (len(word)-3)]) + "-\n>")
if a == word:
    print("You survive!")
else:
    print("You lose!")

