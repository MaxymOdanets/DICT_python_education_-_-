import random

num_list = [2, 3, 4, 5, 6, 7, 8, 9]
sign_list = ['+', '-', '*']

a = random.choice(num_list)
b = random.choice(num_list)
sign = random.choice(sign_list)
print(a, sign, b)

Input = int(input(">"))
addition = 0
subtraction = 0
multiplication = 0

if sign == "+":
    addition = int(a) + int(b)
elif sign == "-":
    subtraction = int(a) - int(b)
elif sign == "*":
    multiplication = int(a) * int(b)

if Input == addition:
    print("Right!")
elif Input == subtraction:
    print("Right!")
elif Input == multiplication:
    print("Right!")
else:
    print("Wrong")

