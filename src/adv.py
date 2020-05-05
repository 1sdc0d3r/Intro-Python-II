# Import modules
from textwrap import wrap
from data import room
from player import Player
# todo create a REPL parser


welcome_message = "Welcome to the dungeon game, would you like to play? (yes/no)"

#! player = Player(input("Enter player name: "), room["outside"])
player = Player("Jack", room["outside"])
command = "null"
# todo allow new commands to be added as they 'unlock' them
# get, take, inspect
commands = {
    "move": ("n", "e", "s", "w"),
    "item": ("pickup", "drop", "use"),
    "actions": ("attack", "search")
}


#! REPL
while(not command == "q"):
    print(f"You are located: {player.current_room}")
    for line in wrap(player.current_room.desc, width=150):
        print(line)
    print(player.current_room.items)  # todo print on search
    command = input("# ").lower().strip()
    if command == "q":
        break

    # * Move Player Direction
    if command in commands["move"]:
        print("move command")
        player.move(command)
    # * Player Item Commands
    elif command in commands["item"]:
        print("item command")
        if command == "pickup":
            player.pick_up()
        elif command == "drop":
            player.drop()
    else:
        print("unknown command")
