# 19/7/2017
# Text based adventure written in python 3, inspiration drawn from the game "Zork"

import time


def PlayIntro():
    print("Welcome to a text based adventure!")
    print()
    time.sleep(1)
    print("You awake in a forrest, surrounded by trees in all directions.")
    print()
    time.sleep(3)
    print("To the north lies a small cottage.")
    print()
    print("To the south there is a thicket of fur trees, far too dense")
    print("to traverse safely.")
    print()
    print("To the east there is a beaten path through the trees.")
    print()
    print("To the west there is a thicket of fur trees and a chasm of")
    print("unknown depth, much deeper than you care to fall.")
    print()


def playerInput():
    txtInput = ""

    with open("availableInput", "r") as i:
        commands = i.readlines()

    while txtInput not in commands:
        if txtInput not in commands and not "":
            print("I don't know the word " + txtInput)

        txtInput = input(">>")

    return txtInput

PlayIntro()
playerInput()
