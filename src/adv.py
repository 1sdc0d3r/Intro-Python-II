# Import modules
import sys
from textwrap import wrap
from data import room, items, welcome_message, quit_message, game_objective
from player import Player

# player = Player(input("Enter player name: "), room["outside"])
player = Player("Jack", room["outside"])

# ? allow new commands to be added as they 'unlock' them
commands = {
    "movement": {"n", "e", "s", "w"},
    "item": {"pickup", "drop", "use", "inspect"},
    "actions": {"search", "block", "attack"},
    "player": {"inventory"}
}
# get, take, replace
# todo create a REPL parser
# ? verb/noun?
# ? Beautiful soup/selenium
# split, check for verb/nouns, dictionary command


parsedCommand = {
    "verb": None,
    "noun": None
}


def parser(command):
    parsedCommand["verb"] = None
    parsedCommand["noun"] = None
    for word in command.split(" "):
        for values in commands.values():
            if word in values:
                parsedCommand["verb"] = word
                break
            else:
                for item in items.values():
                    if word in str(item).lower():
                        parsedCommand["noun"] = word
                        break

    # print("parsed", parsedCommand)


#! command = input(f"{welcome_message}\n🎲 ").lower().strip()
command = None

#! if command == "no":
#     print(quit_message)
#     sys.exit()
#! else:
#     for line in wrap(game_objective, width=120):
#         print(line)
#     print(f"\n{player.current_room}\nUse n, s, e, w to move")
#! REPL
while True:
    # * Prompt User Command
    command = input("🎲 ").lower().strip()
    parser(command)

    # * Move Direction Commands
    if parsedCommand["verb"] in commands["movement"]:
        player.move(command)

    # * Item Commands
    elif parsedCommand["verb"] in commands["item"]:
        if parsedCommand["verb"] == "pickup":
            if parsedCommand["noun"] == None:
                parsedCommand["noun"] = input(
                    "What item would you like to pickup?\n🎲 ").lower().strip()
            player.pick_up(parsedCommand["noun"])
        elif parsedCommand["verb"] == "drop":
            player.drop()
        elif parsedCommand["verb"] == "inspect":
            inspectItem = input(f"What Item would you like to inspect?\n🎲 ")
            for item in player.current_room.items:
                if inspectItem == item.__dict__["name"]:
                    item.inspect()
                else:
                    for item in player.inventory:
                        if inspectItem == item.__dict__["name"]:
                            item.inspect()
                        else:
                            print("Item was not found...")

    # * Action Commands
    elif parsedCommand["verb"] in commands["actions"]:
        if parsedCommand["verb"] == "search":
            response = "Looking around you find: "
            for item in player.current_room.items:
                response += f"{item} "
            print(response.strip())
        else:
            print("not sure what to do yet...")

    # * Player Commands
    elif parsedCommand["verb"] in commands["player"]:
        if parsedCommand["verb"] == "inventory":
            print(player)

    # * Help Command
    elif command == "help":
        while True:
            command = input(
                "What would you like help with?\n  [1] Game Objective [2] Commands [9] Exit\n🎲 ").lower().strip()
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

# todo add save functionality
print(quit_message)
