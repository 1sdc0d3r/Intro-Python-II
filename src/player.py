# Write a class to hold player information, e.g. what room they are in currently.
class Player:
    def __init__(self, name="Jack", current_room="outside"):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f"{', '.join(self.inventory)}"

    def move(self, direction):
        if f"{direction}_to" in self.current_room.__dict__:
            self.current_room = getattr(self.current_room, f"{direction}_to")
        else:
            print(f"This direction doesn't lead anywere. What would you like to do?")

    def pick_up(self):
        print("What item would you like to pickup?")  # todo parser
        item = input("# ").lower().strip()
        if item in self.current_room.items:
            self.inventory.append(item)
            self.current_room.items.remove(item)
            print(f"You added the {item} to your inventory.")
            print(f"Items currently in your bag: {self}")
        else:
            print(f"{item} was not found...")

    def drop(self):
        if self.inventory:
            print("Which item would you like to leave behind?")  # todo parser
            print(f"Items currently in your bag: {self}")
            item = input("# ").lower().strip()
            if item in self.inventory:
                self.inventory.remove(item)
                self.current_room.items.append(item)
                print(f"You dropped the {item}.")
                print(f"Items currently in your bag: {self}")
            else:
                print(f"{item} was not found in your bag...")
        else:
            print("There is nothing in your bag. See what you can find!")
