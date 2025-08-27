# rock, paper, and scissor game

import random

system = random.choice([-1, 0, 1])

yourChoice = input("Enter your choice (Rock: r, Paper: p, Scissors: s): ")

youDict = {"r": 1, "p": 0, "s": -1}
revDict = {1: "Rock", 0: "Paper", -1:"Scissors"}

you = youDict[yourChoice]

print(f"You Choose: {revDict[you]}\nComputer Choose: {revDict[system]}")

if ((system == you)):
    print("It's a draw!")
else:
    if((system == 1) and (you == 0)):
        print("You Win")
    elif ((system == 1) and (you == -1)):
        print("You lose")
    elif ((system == 0) and (you == 1)):
        print("You lose")
    elif ((system == 0) and (you == -1)):
        print("You Win")
    elif ((system == -1) and (you == 0)):
        print("You lose")
    elif ((system == -1) and (you == 1)):
        print("You Win")
    else:
        print("ERROR! SOMETHING WENT WRONG")