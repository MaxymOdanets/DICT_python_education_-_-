option = input("choose you option\n\
type 'rock' to choose rock\n\
type 'paper' to choose paper\n\
type 'scissors' to choose scissors\n>")
if option == 'rock':
    print("Sorry, but the computer chose paper")
elif option == 'paper':
    print("Sorry, but the computer chose scissors")
elif option == 'scissors':
    print("Sorry, but the computer chose rock")
else:
    print("invalid format")