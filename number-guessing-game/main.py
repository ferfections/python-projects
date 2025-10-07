import random


number = random.randint(1,100)
guessed = False

print("The number has been generated")

while guessed is False:
    x = input("Make a guess: ")
    if int(x) > int(number):
        print("Lower")
    elif int(x) < int(number):
        print("Higher")
    elif int(x) == int(number):
        print("YESSS!!")
        guessed = True


