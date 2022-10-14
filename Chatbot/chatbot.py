print("Hello! My name is Garik \nI was created in 2022")
print("Please remind me your name: ")
name = input(">")
print(f"What a great name you have,{name}")
print("Let me guess your age? \nEnter remainders of dividing your age by 3, 5 and 7")
remainder3 = int(input(">"))
remainder5 = int(input(">"))
remainder7 = int(input(">"))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is", age, "that's a good time to start programming!")
a = int(input("Now I will prove to you that I can count to any number you want.\n"))
for i in range(a + 1):
    print(str(i) + "!")
print("Completed,Have a nice day!")
print("Let's test you.\nDo tou love KhAI? ")
print("1.Of course! \n2.No:(")
while True:
    k = int(input(">"))
    if k == 1:
        print("Cool,KHAI love you too!\nCongratulations,have a nice day!")
        break
    else:
        print("Please try again")
