from room import Room
from item import Item

#! Declare all rooms
room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    "kitchen": Room("Kitchen", "This is where the food magic happens, and it looks like no one has used this for a long time. There is a blood smatter on the South wall. There is a set of spiral stairs going deep to the North, and a old cracking oak door to the West."),
    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm. To the East and West the Wall looms high."),

    'narrow': Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! There appears to have been a massecure here. There are skeletons and bones scattered around. The only exit is to the south."),
}
item = {
    "torch": Item("torch", "Length of wood with tar rags wrapped around one end."),
    "key": Item("key", "Small golden key. There is an inscription in the handle but its faded."),
    "sword": Item("Sword of Fernwood", "Sword with a bronze handle and cross. It isn't as sharp as it once was, but is better than a stick!"),
    "shield": Item("Shield of Fernwood", "Battered and scarred round shield. It has seen many battles. It may break with a mighty blow.")
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

#! Add items to rooms
# ? Is there a way to 'reach in' to the item class for the name?
# room["foyer"].items = ["torch"]
# room["overlook"].items = ["key"]
# room["treasure"].items = ["sword", "shield"]

# todo change items to classes

room["foyer"].items.append(item["torch"])
room["overlook"].items.append(item["key"])
room["treasure"].items.append(item["sword"])
room["treasure"].items.append(item["shield"])
# print(f"{room['foyer'].items[0].print_desc()}")
# print(room["narrow"].n_to)

welcome_message = "Welcome to the dungeon game, would you like to play? (yes/no)"
quit_message = "Sorry to see you go..."
game_objective = "This game is a choose your own adventure game. Use your wits to navigate and discover the lost kingdom of Shalooma. Your quest is to find exotic treasures, fight monstors, and to find the Golden Cookie. This cookie is said to be guarded by fierce monsters, but gives the user eternal life and fame. Good luck on your quest Adventurer!"
