# Import modules
from sys import exit
import os
from textwrap import wrap
from data import room, items, welcome_message, quit_message, game_objective
from player import Player


# ? allow new commands to be added as they 'unlock' them
commands = {
    "direction": {"n", "e", "s", "w", "north", "east", "south", "west"},
    "item": {"pickup", "get", "take", "drop", "use", "inspect"},
    "actions": {"search", "look", "block", "attack"},
    "player": {"inventory"},
    "gameplay": {"q", "quit", "help"}
}


parsedCommand = {
    "verb": None,
    "noun": None
}


def parser(command):
    if not command:
        print("Please enter a command...")
    else:
        parsedCommand.clear()
        for word in command.split(" "):
            for values in commands.values():
                if word in values:
                    parsedCommand["verb"] = word
                    break
                elif len(command.split(" ")) > 1:
                    parsedCommand["noun"] = word
                else:
                    parsedCommand["noun"] = None

    # print("parsed", parsedCommand)


# * clear terminal
print(chr(27) + "[2J")
# os.system("cls")

command = input(f"{welcome_message}\n🎲 ").lower().strip()

# * Check to see if the player wants to play
if command in ("n", "no"):
    print(quit_message)
    exit()
else:
    player = Player(input("Enter player name: "), room["outside"])
    # player = Player("Jack", room["outside"])
    for line in wrap(game_objective, width=120):
        print(line)
    print(f"\n{player.current_room}\nUse n, s, e, w to move.")

#! REPL
while True:
    # * Prompt User Command
    command = input("🎲 ").lower().strip()
    parser(command)

    # * Move Direction Commands
    if parsedCommand["verb"] in commands["direction"]:
        player.move(parsedCommand["verb"])

    # * Item Commands
    elif parsedCommand["verb"] in commands["item"]:
        if parsedCommand["verb"] in ("pickup", "get", "take"):
            player.pick_up(parsedCommand["noun"])

        elif parsedCommand["verb"] in ("drop", "leave"):
            player.drop(parsedCommand["noun"])

# todo fix parsed command here
        elif parsedCommand["verb"] == "inspect":
            # inspectItem = input(f"What Item would you like to inspect?\n🎲 ")
            if parsedCommand["noun"] == None:
                parsedCommand["noun"] = input(
                    f"What Item would you like to inspect?\n🎲 ").lower().strip()
            for item in player.current_room.items:
                if parsedCommand["noun"] == getattr(item, "name").lower():
                    item.inspect()

                else:
                    for item in player.inventory:
                        if parsedCommand["noun"] == getattr(item, "name").lower():
                            item.inspect()

                        else:
                            print("Item was not found...")

    # * Action Commands
    elif parsedCommand["verb"] in commands["actions"]:
        if parsedCommand["verb"] in ("search", "look"):
            response = "Looking around you find: "
            for item in player.current_room.items:
                response += f"{item}, "
            print(response.strip(", "))

        else:
            print("not sure what to do yet...")

    # * Player Commands
    elif parsedCommand["verb"] in commands["player"]:
        if parsedCommand["verb"] == "inventory":
            print(player)

    # * Help Command
    elif parsedCommand["verb"] in commands["gameplay"]:
        if parsedCommand["verb"] == "help":
            while True:
                command = input(
                    "What would you like help with?\n[1] Game Objective [2] Commands [9] Exit\n🎲 ").lower().strip()

                if command == "game objective" or command == "1":
                    print("\n")
                    for line in wrap(game_objective, width=100):
                        print(line)
                    print("\n")

                elif command == "commands" or command == "2":
                    print("\n")
                    for key in commands:
                        print(f"{key}: {', '.join(commands[key])}")
                    print("\n")

                elif (command == "exit" or command == "9"):
                    break

                else:
                    print("Command not found...")
            print(player.current_room)

        elif parsedCommand["verb"] in ("q", "quit"):
            break
    else:
        print("unknown command, for help type 'help'")

# todo add save functionality
print(quit_message)
