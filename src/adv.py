# Import modules
from textwrap import wrap
from data import room
from player import Player

# Main
# todo create a REPL parser

player = Player(input("Enter player name: "), room["outside"])

# Write a loop that:
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
user = "null"
commands = ("q", "n", "e", "s", "w", "get", "take", "drop", "use")

#! REPL
while(not user == "q"):
    print(f"You are located: {player.current_room}")
    for line in wrap(player.current_room.desc, width=150):
        print(line)

    user = input("#")

    if user in commands:
        print("command exists")
        continue
    else:
        print("invalid command. Try again...")
        print(f"{player.current_room.desc}")
        user = input("#")

    print(f"user: {user}_to")
    if f"{user}_to" in player.current_room.__dict__:
        print("valid direction")
        continue
    else:
        print("Invalid direction please try again...")
        print(f"{player.current_room.desc}")
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


# if __name__ == '__main__':
#     dungeon_game()
