from room import Room

#! Declare all rooms
room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    "kitchen": Room("Kitchen", "This is where the food magic happens, and it looks like no one has used this for a long time. There is a blood smatter on the South wall. There is a set of spiral stairs going deep to the North, and a old cracking oak door to the West."),
    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm. To the East and West the Wall looms high."),

    'narrow': Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! There appears to have been a massecure here. There are skeletons and bones scattered around. The only exit is to the south."),
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
room["foyer"].items = ["torch"]
room["overlook"].items = ["key"]
room["treasure"].items = ["sword", "shield"]
