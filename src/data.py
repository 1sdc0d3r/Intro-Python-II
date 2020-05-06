from room import Room
from item import Item, LightSource, Weapon, Shield

#! Declare all rooms
room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    "kitchen": Room("Kitchen", "This is where the food magic happens, and it looks like no one has used this for a long time. There is a blood smatter on the South wall. There is a set of spiral stairs going deep to the North, and a old cracking oak door to the West."),
    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm. To the East and West the Wall looms high."),

    'narrow': Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! There appears to have been a massecure here. There are skeletons and bones scattered around. The only exit is to the south."),
}
# ⚔️🛡🗝
items = {
    "torch": LightSource("Torch", "Length of wood with tar rags wrapped around one end.", "common"),
    "key": Item("Key", "Small golden key. There is an inscription in the handle but its faded.", "common"),
    "sword": Weapon("Sword of Fernwood", "Sword with a bronze handle and cross. It isn't as sharp as it once was, but is better than a stick!", "common", 5, 3),
    "shield": Shield("Shield of Fernwood", "Battered and scarred round shield. It has seen many battles. It may break with a mighty blow.", "common", 7)
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
room["foyer"].items.append(items["torch"])
room["foyer"].items.append(items["key"])
room["overlook"].items.append(items["key"])
room["treasure"].items.append(items["sword"])
room["treasure"].items.append(items["shield"])
# print(room["foyer"].items)

welcome_message = "Welcome to the dungeon game, would you like to play? (yes/no)"
quit_message = "Sorry to see you go..."
game_objective = "This game is a choose your own adventure game. Use your wits to navigate and discover the lost kingdom of Shalooma. Your quest is to find exotic treasures, fight monstors, and to find the Golden Cookie. This cookie is said to be guarded by fierce monsters, but gives the user eternal life and fame. Good luck on your quest Adventurer!"
