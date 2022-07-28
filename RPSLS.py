import random
import os
from turtle import st

loopy = 'y'
clear = lambda: os.system('cls')
while loopy == 'y':
    clear()
    enemy = random.randint(0, 4)
    enemyc = ["rock","paper","scissors","lizard","spock"]

    playern = input("Enter player name \n")
    clear()
    playerc = int(input("rock = 0, paper = 1, scissors = 2, lizard = 3, spock = 4 \n"))
    clear()

    if playerc < 0 or playerc > 4:
        print("invalid move")
    else:
        print(playern + ": " + enemyc[playerc] + "\nBot: " + enemyc[enemy])
        if playerc == 0:                    #rock
            if enemy == 0 or enemy == 3:
                print(playern + " WIN")
            else:
                if enemy == 0:
                    print("draw")
                else:
                    print(playern + " LOSE")
        if playerc == 1:                    #paper
            if enemy == 1 or enemy == 4:
                print(playern + " WIN")
            else:
                if enemy == 1:
                    print("draw")
                else:
                    print(playern + " LOSE")
        if playerc == 2:                    #scissors
            if enemy == 2 or enemy == 3:
                print(playern + " WIN")
            else:
                if enemy == 2:
                    print("draw")
                else:
                    print(playern + " LOSE")
        if playerc == 3:                    #lizard
            if enemy == 2 or enemy == 4:
                print(playern + " WIN")
            else:
                if enemy == 3:
                    print("draw")
                else:
                    print(playern + " LOSE")
        if playerc == 4:                    #spock
            if enemy == 0 or enemy == 1:
                print(playern + " WIN")
            else:
                if enemy == 4:
                    print("draw")
                else:
                    print(playern + " LOSE")
    loopy = str(input("\nAgain? (y)es or (n)o \n"))  