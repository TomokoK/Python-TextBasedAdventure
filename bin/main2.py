# 19/7/2017
# Text based adventure written in python 3, inspiration drawn from the game "Zork"

import time


# Player constructor
class Player:
    def __init__(self):
        self.playing = True
        self.inventory = []
        self.current_room = "room0"


# Intro
print("Welcome to a text based adventure!")
print()
time.sleep(1)
print("You awake in a forest, surrounded by trees in all directions.")
print()
time.sleep(3)


# MOVEMENT AND LOOK FUNCTIONS -----------------------------------------

# ROOM LOOK ---------------------------

def room0_look(player):
    #description
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


def room1_look(player):
    #description
    print("You are facing the cottage. The windows are boarded up and")
    print("the door is blocked by a pile of rubble.")
    print()


def room2_look(player):
    #desc.
    if "Ruby Egg" in player.inventory:
        print("You are in a small clearing in the forest.")
        print()
    else:
        print("You are in a small clearing in the forest. A ruby egg is")
        print("laying on the ground.")
        print()


def room3_look(player):
    #desc.
    print("stuff")


def room4_look(player):
    #desc.
    print("stuff")


def room5_look(player):
    #desc.
    print("stuff")


def room6_look(player):
    #desc.
    print("stuff")


def room7_look(player):
    #desc.
    print("stuff")


def room8_look(player):
    #desc.
    print("stuff")


def room9_look(player):
    #desc.
    print("stuff")


def room10_look(player):
    #desc.
    print("stuff")


# MOVE NORTH ----------------------


def room0_movenorth(player):
    player.current_room = "room1"


def room4_movenorth(player):
    player.current_room = "room6"


def room5_movenorth(player):
    player.current_room = "room7"


def room6_movenorth(player):
    player.current_room = "room8"


def room7_movenorth(player):
    player.current_room = "room9"


# MOVE SOUTH ----------------------

def room6_movesouth(player):
    player.current_room = "room4"


def room7_movesouth(player):
    player.current_room = "room5"


def room8_movesouth(player):
    player.current_room = "room6"


def room9_movesouth(player):
    player.current_room = "room7"


# MOVE EAST -----------------------

def room0_moveeast(player):
    player.current_room = "room3"


def room1_moveeast(player):
    player.current_room = "room4"


def room2_moveeast(player):
    player.current_room = "room0"


def room5_moveeast(player):
    player.current_room = "room1"


def room9_moveeast(player):
    player.current_room = "room10"


def room10_moveeast(player):
    player.current_room = "room8"


# MOVE WEST ------------------------

def room0_movewest(player):
    player.current_room = "room2"


def room1_movewest(player):
    player.current_room = "room5"


def room3_movewest(player):
    player.current_room = "room0"


def room4_movewest(player):
    player.current_room = "room1"


def room8_movewest(player):
    player.current_room = "room10"


def room10_movewest(player):
    player.current_room = "room9"


# END MOVEMENT / LOOK FUNCTIONS ----------------------------------------------------------------

# Misc. Functions
def room2_pickupegg(player):
    if "Ruby Egg" not in player.inventory:
        player.inventory.insert(0, "Ruby Egg")


# Dictionary that calls the function linked to the input dependent on
# what room you are in(e.g. look while in room0)

rooms = {
    "room0": {"look": room0_look, "go north": room0_movenorth, "go east": room0_moveeast,
              "go west": room0_movewest},
    "room1": {"look": room1_look, "go east": room1_moveeast, "go west": room1_movewest},
    "room2": {"look": room2_look, "go east": room2_moveeast, 'take egg': room2_pickupegg},
    "room3": {"look": room3_look, "go west": room3_movewest},
    "room4": {"look": room4_look, "go north": room4_movenorth, "go west": room4_movewest},
    "room5": {"look": room5_look, "go north": room5_movenorth, "go east": room5_moveeast},
    "room6": {"look": room6_look, "go north": room6_movenorth, "go south": room6_movesouth},
    "room7": {"look": room7_look, "go north": room7_movenorth, "go south": room7_movesouth},
    "room8": {"look": room8_look, "go south": room8_movesouth, "go west": room8_movewest},
    "room9": {"look": room9_look, "go east": room9_moveeast, "go south": room9_movesouth},
    "room10": {"look": room10_look, "go east": room10_moveeast, "go west": room10_movewest}
}


# Room check and print logic

myPlayer = Player()
last_room = ""

while myPlayer.playing:

    if last_room != myPlayer.current_room:
        rooms[myPlayer.current_room]["look"](myPlayer)
        last_room = myPlayer.current_room
    print("The actions available to you are: ", end='')
    first = True

    for action in rooms[myPlayer.current_room]:
        if not first:
            print(", ", end='')
        else:
            first = False
        print(action, end='')
    print("")

    action = input(">> ")

    try:
        rooms[myPlayer.current_room][action](myPlayer)
    except KeyError:
        print("I don't know the word " + action)
