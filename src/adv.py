# Import modules
from textwrap import wrap
from data import room
from player import Player
# todo create a REPL parser


welcome_message = "Welcome to the dungeon game, would you like to play? (yes/no)"

#! player = Player(input("Enter player name: "), room["outside"])
player = Player("Jack", room["outside"])
command = "null"
commands = ("q", "n", "e", "s", "w", "get", "take", "drop")


#! REPL
while(not command == "q"):
    print(f"You are located: {player.current_room}")
    for line in wrap(player.current_room.desc, width=150):
        print(line)

    command = input("# ").lower().strip()
    if command == "q":
        break

    # * Move player direction
    player.move(command)
