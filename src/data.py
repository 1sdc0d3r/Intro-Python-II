from room import Room, Trap
from item import Item, LightSource, Weapon, Shield

commands = {
    "direction": {"n", "e", "s", "w", "north", "east", "south", "west"},
    "item": {"pickup", "get", "take", "drop", "use", "inspect"},
    "actions": {"search", "look", "block", "attack"},
    "player": {"inventory", "room", "location", "hp", "health"},
    "gameplay": {"q", "quit", "help"}
}

#! Declare all rooms
rooms = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons."),

    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east. There appears to be a kitchen to the West."),

    "kitchen": Room("Kitchen", "This is where the food magic happens, and it looks like no one has used this for a long time. There is a blood smatter on the South wall. There is a set of spiral stairs going deep to the North, and a old cracking oak door to the West."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm. To the East and West the Wall looms high."),

    'narrow': Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! There appears to have been a massecure here. There are skeletons and bones scattered around. The only exit is to the south."),
}
traps = {
    "pitfall": Trap("Pitfall", "You fall down to your death...", 100)
}
# ⚔️🛡🗝🍪
items = {
    "golden cookie": Item("🍪 Golden Cookie", "This cookie is said to provide immortality and great powers. It is said to be guarded by the 'Cookie Monster'.", "Legendary"),

    "torch": LightSource("Torch", "Length of wood with tar rags wrapped around one end.", "common"),

    "key": Item("Key", "🗝 Small golden key. There is an inscription in the handle but its faded.", "common"),

    "sword": Weapon("⚔️ Sword of Ironwood", "Sword with a bronze handle and cross. It isn't as sharp as it once was, but is better than a stick!", "common", 5, 3),

    "shield": Shield("🛡 Shield of Fernwood", "Battered and scarred round shield. It has seen many battles. It may break with a mighty blow.", "common", 7)
}

messages = {
    "begin": "Welcome to the dungeon game, would you like to play? (yes/no)",
    "objective": "This game is a choose your own adventure game. Use your wits to navigate and discover the lost kingdom of Shalooma. Your quest is to find exotic treasures, fight monstors, and to find the Golden Cookie. This cookie is said to be guarded by fierce monsters, but gives the user eternal life and fame. Good luck on your quest Adventurer!",
    "quit": "Sorry to see you go...",
    "death": "☠️ You died... Better luck next time!",
    "cookie": "🏁 You have found the Golden Cookie! You may have found eternal life and power beyond your knowledge!",
    "instructions": "Move North, South, East, West. Look around and find items. For more information use 'inspect'. If you ever need help type 'Help'."
}


#! Link rooms together
rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].w_to = rooms['kitchen']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']
rooms['kitchen'].e_to = rooms['foyer']
rooms['kitchen'].w_to = traps['pitfall']

#! Add items to rooms
rooms["foyer"].items.append(items["torch"])
rooms["foyer"].items.append(items["key"])
rooms["overlook"].items.append(items["key"])
rooms["treasure"].items.append(items["sword"])
rooms["treasure"].items.append(items["shield"])
rooms["treasure"].items.append(items["golden cookie"])
# print(rooms["foyer"].items)

welcome_message = "Welcome to the dungeon game, would you like to play? (yes/no)"
quit_message = "Sorry to see you go..."
game_objective = "This game is a choose your own adventure game. Use your wits to navigate and discover the lost kingdom of Shalooma. Your quest is to find exotic treasures, fight monstors, and to find the Golden Cookie. This cookie is said to be guarded by fierce monsters, but gives the user eternal life and fame. Good luck on your quest Adventurer!"
