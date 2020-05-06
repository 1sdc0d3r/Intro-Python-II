from textwrap import wrap


class Player:
    def __init__(self, name="Jack", current_room="outside"):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        if self.inventory:
            response = "🎒Items currently in your bag: "
            for item in self.inventory:
                response += f"{item.__dict__['name']}, "
            return response.rstrip(", ")
        else:
            return "🎒Your bag is empty..."

    def move(self, direction):
        direction = direction[0]
        if f"{direction}_to" in self.current_room.__dict__:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print(f"This direction doesn't lead anywere. What would you like to do?")

    def pick_up(self, commandItem):
        for item in self.current_room.items:
            if commandItem == item.__dict__["name"].lower():
                self.inventory.append(item)
                self.current_room.items.remove(item)
                print(f"You added the {item} to your inventory.\n{self}")
                break
        else:
            print(f"{commandItem} was not found...")

    def drop(self, commandItem):
        if self.inventory:
            print("item", commandItem)
            if commandItem == None:
                commandItem = input(
                    f"Which item would you like to leave behind?\n{self}\n🎲 ").lower().strip()
            for item in self.inventory:
                if commandItem == item.__dict__["name"].lower():
                    self.inventory.remove(item)
                    self.current_room.items.append(item)
                    print(
                        f"You dropped the {item}. \nItems currently in your bag: {self}")
                    break
                elif commandItem == item.__dict__["name"].lower():
                    print(f"{item} was not found in your bag...")
        else:
            print("🎒There is nothing in your bag. See what you can find!")
