# Import modules
from sys import exit
import os.path
from os import sys, path
from textwrap import wrap
from data import room, items, welcome_message, quit_message, game_objective, commands
from player import Player
from parser import parser
import pickle

print(chr(27) + "[2J")  # * clear terminal

if input(f"{welcome_message}\n🎲 ").lower().strip() in ("n", "no"):
    print(quit_message)
    exit()

elif input(f"Load Game?(yes/no) ♻️ ").strip().lower() in ("y", "yes"):
    if path.exists("savefile.p"):
        player = pickle.load(open("savefile.p", "rb"))
    else:
        print("No game saved...")
else:
    player = Player(input("Enter player name: "), room["outside"])

for line in wrap(game_objective, width=120):
    print(line)
print(f"\n{player.current_room}\nUse n, s, e, w to move.")

#! REPL
while True:
    # * Prompt User Command
    command = input("🎲 ").lower().strip()
    parsedCommand = parser(command)

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
                if parsedCommand["noun"] in getattr(item, "name").lower():
                    item.inspect()

                else:
                    for item in player.inventory:
                        if parsedCommand["noun"] in getattr(item, "name").lower():
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

                if command in ("1", "game objective"):
                    print("\n")
                    for line in wrap(game_objective, width=100):
                        print(line)
                    print("\n")

                elif command in ("2", "commands"):
                    print("\n")
                    for key in commands:
                        print(f"{key}: {', '.join(commands[key])}")
                    print("\n")

                elif command in ("9", "exit"):
                    break

                else:
                    print("Command not found...")
            print(player.current_room)

        elif parsedCommand["verb"] in ("q", "quit"):
            break
    else:
        print("unknown command, for help type 'help'")

# todo add save functionality
if input("Save Game? 🏁 ").lower().strip() in ("y", "yes"):
    if path.exists("savefile.p"):
        if input("Existing save. Overwrite data? (yes/no) # ") in ("y", "yes"):
            pickle.dump(player, open("savefile.p", "wb"))
            print("Game Saved!")
        else:
            print("Game not saved...")
    else:
        pickle.dump(player, open("savefile.p", "wb"))
        print("Game Saved!")

print(quit_message)
exit()
