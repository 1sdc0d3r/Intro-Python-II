# Import modules
from textwrap import wrap

#! Import classes
from room import Room, List
from player import Player

#! Declare all rooms
room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow': Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}


#! Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Main
# todo create a REPL parser

# Make a new player object that is currently in the 'outside' room.
player = Player(input("Enter player name: "), room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
user = "null"

#! REPL
while(not user == "q"):
    print(f"You are located: {player.current_room}")
    for line in wrap(player.current_room.desc, width=50):
        print(line)
    user = input("#")

# todo if there is not direction from that location, prompt again
    if user == "n":
        player.current_room = player.current_room.n_to

    elif user == "e":
        player.current_room = player.current_room.e_to

    elif user == "s":
        player.current_room = player.current_room.s_to

    elif user == "w":
        player.current_room = player.current_room.w_to
