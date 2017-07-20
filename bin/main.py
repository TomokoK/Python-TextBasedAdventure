# 19/7/2017
# Text based adventure written in python 3, inspiration drawn from the game "Zork"

import time


def playIntro():
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


def room0Function():
    #Starting room
    current_pos = 'room0'
    print("To the north lies a small cottage.")
    print()
    print("To the south there is a thicket of fur threes, far too dense")
    print("to traverse safely.")
    print()
    print("To the east there is a beaten path through the trees.")
    print()
    print("To the west there is a thicket of fur trees and a chasm of")
    print("unknown depth, much deeper than you care to fall.")
    print()
    playerInput()


def room1Function():
    #Cottage porch
    current_pos = 'room1'
    print()
    playerInput()


def room2Function():
    #Beaten path
    current_pos = 'room2'
    print()
    playerInput()


def room3Function():
    #Chasm
    current_pos = 'room3'
    print()
    playerInput()


def playerInput(txtInput=None):

    current_pos = 'room0'

    with open("availableInput", "r") as i:
        commands = i.readlines()

    while txtInput not in commands:
        if txtInput not in commands and txtInput is not None:
            print("I don't know the word " + txtInput)

        txtInput = input(">>")

        if txtInput in commands and txtInput is not None:
            if txtInput == "go north":
                current_pos = 'room1'
                goDirection()
            elif txtInput == "go south":
                current_pos = 'room2'
                goDirection(room2Function())
            elif txtInput == "go west":
                current_pos = 'room3'
                goDirection(room3Function())

        #return txtInput


def goDirection(current_pos):

    possible_moves = {
        'room0' : room0Function(),
        'room1' : room1Function(),
        'room2' : room2Function(),
        'room3' : room3Function()
    }

playIntro()
playerInput()
