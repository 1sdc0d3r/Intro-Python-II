# Import modules
import sys
from textwrap import wrap
from data import room, welcome_message, quit_message, game_objective
from player import Player

# todo create a REPL parser

# player = Player(input("Enter player name: "), room["outside"])
player = Player("Jack", room["outside"])

# ? allow new commands to be added as they 'unlock' them
commands = {
    "move": {"n", "e", "s", "w"},
    "item": {"pickup", "drop", "use", "inventory"},
    "actions": {"search", "block", "attack"}
}
# get, take, inspect

#! print(welcome_message)
#! command = input("# ").lower().strip()

#! if command == "no":
#     print(quit_message)
#     sys.exit()
#! else:
#     for line in wrap(game_objective, width=120):
#         print(line)
#     print(f"\n{player.current_room}\nUse n, s, e, w to move")
command = None
#! REPL
while True:
    # * Prompt User Command
    command = input("# ").lower().strip()

    # * Move Direction Commands
    if command in commands["move"]:
        player.move(command)

    # * Item Commands
    elif command in commands["item"]:
        if command == "pickup":
            player.pick_up()
        elif command == "drop":
            player.drop()
        elif command == "inventory":
            print(player)

    # * Action Commands
    elif command in commands["actions"]:
        if command == "search":
            response = "Looking around you find: "
            for item in player.current_room.items:
                response += item
            print(response)

    # * Help Command
    elif command == "help":
        while True:
            print(
                "What would you like help with?\n  [1] Game Objective [2] Commands [9] Exit")
            command = input("# ").lower().strip()
            if command == "game objective" or command == "1":
                for line in wrap(game_objective, width=100):
                    print(line)

            elif command == "commands" or command == "2":
                for key in commands:
                    print(f"{key}: {', '.join(commands[key])}")

            elif (command == "exit" or command == "9"):
                break
            else:
                print("Command not found...")
        print(player.current_room)

    elif (command == "q" or command == "quit"):
        break
    else:
        print("unknown command, for help type 'help'")

print(quit_message)
# todo add save functionality
