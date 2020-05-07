from textwrap import wrap
from sys import exit
from data import messages


class Player:
    def __init__(self, name="Jack", current_room="outside"):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        if self.inventory:
            response = "🎒Items currently in your bag: "
            for item in self.inventory:
                response += f"{getattr(item, 'name')}, "
            return response.rstrip(", ")
        else:
            return "🎒Your bag is empty..."

    def move(self, direction):
        direction = direction[0]
        if hasattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print(f"This direction doesn't lead anywere. What would you like to do?")

    def pick_up(self, commandItem):
        if not commandItem:
            commandItem = input(
                "What item would you like to pickup?\n🎲 ").lower().strip()
        for item in self.current_room.items:
            if commandItem in getattr(item, "name").lower().split(" "):
                self.inventory.append(item)
                self.current_room.items.remove(item)
                print(f"You added the {item} to your inventory.\n{self}")
                if getattr(item, "name") == "Golden Cookie":
                    print(messages["cookie"])
                    exit()
                else:
                    break
        else:
            print(f"{commandItem} was not found...")

    def drop(self, commandItem):
        if self.inventory:
            if not commandItem:
                commandItem = input(
                    f"Which item would you like to leave behind?\n{self}\n🎲 ").lower().strip()
            for item in self.inventory:
                if commandItem in getattr(item, "name").lower().split(" "):
                    self.inventory.remove(item)
                    self.current_room.items.append(item)
                    print(
                        f"You dropped the {item}. \nItems currently in your bag: {self}")
                    break
                elif item == self.inventory[-1]:
                    print(f"{item} was not found in your bag...")
        else:
            print("🎒There is nothing in your bag. See what you can find!")
