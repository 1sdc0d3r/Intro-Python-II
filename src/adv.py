# Import modules
from sys import exit
from os import system, path
from textwrap import wrap
from player import Player
from data import messages, rooms, items,  commands
from parser import parser
import pickle  # to save

system("clear")
if input(f"{messages['welcome']}\n🎲 ").lower().strip() in ("n", "no"):
    print(messages["quit"])
    exit()

elif input(f"Load Game?(yes/no) ♻️ ").strip().lower() in ("y", "yes"):
    if path.exists("savefile.p"):
        player = pickle.load(open("savefile.p", "rb"))
        system("clear")
    else:
        print("😱 No game saved...")
else:
    player = Player(input("🧞‍♂️ Enter player name: "), rooms["outside"])
    system("clear")

welcome = f"Welcome {player.name}\n\n"
for line in wrap(messages["objective"], width=100):
    welcome += f"{line}\n"
print(
    f"{welcome}\n\n{player.current_room}\nFor help type 'Help'.")

#! REPL
while True:
    print("\n")
    command = input("🎲 ").lower().strip()
    parsedCommand = parser(command)

    # * Move Direction
    if parsedCommand["v"] in commands["direction"]:
        player.move(parsedCommand["v"])

    # * Items
    elif parsedCommand["v"] in commands["item"]:
        if parsedCommand["v"] in ("pickup", "get", "take"):
            player.pick_up(parsedCommand["n"])

        elif parsedCommand["v"] in ("drop", "leave"):
            player.drop(parsedCommand["n"])

        elif parsedCommand["v"] == "inspect":
            if not parsedCommand["n"]:
                parsedCommand["n"] = input(
                    f"What Item would you like to inspect?\n🎲 ").lower().strip()
            for item in player.inventory + player.current_room.items:
                if parsedCommand["n"] in getattr(item, "name").lower().strip().split():
                    item.inspect()
                    break
                elif item == player.current_room.items[-1]:
                    print(f"{item} was not found...")

    # * Actions
    elif parsedCommand["v"] in commands["actions"]:
        if parsedCommand["v"] in ("search", "look"):
            response = "Looking around you find: "
            for item in player.current_room.items:
                response += f"{item}, "
            print(response.strip(", "))

        else:
            print("not sure what to do yet...")

    # * Player
    elif parsedCommand["v"] in commands["player"]:
        if parsedCommand["v"] == "inventory":
            print(player)
        elif parsedCommand["v"] in commands["player"]:
            if parsedCommand["v"] in ("room", "location"):
                print(player.current_room)

    # * Help
    elif parsedCommand["v"] in commands["gameplay"]:
        if parsedCommand["v"] == "help":
            while True:
                command = input(
                    "What would you like help with?\n[1] Game Objective [2] Commands [9] Exit\n🎲 ").lower().strip()

                if command in ("1", "game objective"):
                    print("\n")
                    for line in wrap(messages["objective"], width=100):
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

print(messages["quit"])
exit()
