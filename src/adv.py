# Import modules
from sys import exit
from os import sys, path
from textwrap import wrap
from player import Player
from data import room, items, welcome_message, quit_message, game_objective, commands
from parser import parser
import pickle  # to save

print(chr(27) + "[2J")  # * clear terminal

if input(f"{welcome_message}\n🎲 ").lower().strip() in ("n", "no"):
    print(quit_message)
    exit()

elif input(f"Load Game?(yes/no) ♻️ ").strip().lower() in ("y", "yes"):
    if path.exists("savefile.p"):
        player = pickle.load(open("savefile.p", "rb"))
        print(chr(27) + "[2J")  # * clear terminal
    else:
        print("😱 No game saved...")
else:
    player = Player(input("🧞‍♂️ Enter player name: "), room["outside"])
    print(chr(27) + "[2J")  # * clear terminal


welcome = f"Welcome {player.name}\n\n"
for line in wrap(game_objective, width=100):
    welcome += f"{line}\n"
print(f"{welcome}\n\n{player.current_room}\nFor help type 'Help'.")

#! REPL
while True:
    # * Prompt User Command
    print("\n")
    command = input("🎲 ").lower().strip()
    parsedCommand = parser(command)

    # * Move Direction Commands
    if parsedCommand["v"] in commands["direction"]:
        player.move(parsedCommand["v"])

    # * Item Commands
    elif parsedCommand["v"] in commands["item"]:
        if parsedCommand["v"] in ("pickup", "get", "take"):
            player.pick_up(parsedCommand["n"])

        elif parsedCommand["v"] in ("drop", "leave"):
            player.drop(parsedCommand["n"])

# todo fix item not found here
        elif parsedCommand["v"] == "inspect":
            if not parsedCommand["n"]:
                parsedCommand["n"] = input(
                    f"What Item would you like to inspect?\n🎲 ").lower().strip()
            for item in player.current_room.items:
                if parsedCommand["n"] == getattr(item, "name").lower():
                    item.inspect()
                    break

                else:
                    for item in player.inventory:
                        if parsedCommand["n"] == getattr(item, "name").lower():
                            item.inspect()
                            break

                        else:
                            print("Item was not found...")

    # * Action Commands
    elif parsedCommand["v"] in commands["actions"]:
        if parsedCommand["v"] in ("search", "look"):
            response = "Looking around you find: "
            for item in player.current_room.items:
                response += f"{item}, "
            print(response.strip(", "))

        else:
            print("not sure what to do yet...")

    # * Player Commands
    elif parsedCommand["v"] in commands["player"]:
        if parsedCommand["v"] == "inventory":
            print(player)

    # * Help Command
    elif parsedCommand["v"] in commands["gameplay"]:
        if parsedCommand["v"] == "help":
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

        elif parsedCommand["v"] in ("q", "quit"):
            break
    else:
        print("unknown command, for help type 'help'")

if input("Save Game? 🏁 ").lower().strip() in ("y", "yes"):
    if path.exists("savefile.p"):
        if input("Existing save. Overwrite data? (yes/no) # ") in ("y", "yes"):
            pickle.dump(player, open("savefile.p", "wb"))
            print("Game Saved!")
        else:
            print("🚩 Game not saved...")
    else:
        pickle.dump(player, open("savefile.p", "wb"))
        print("✅ Game Saved!")

print(quit_message)
exit()
