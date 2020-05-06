from textwrap import wrap


class Player:
    def __init__(self, name="Jack", current_room="outside"):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        if self.inventory:
            return f"Inside your bag: {', '.join(self.inventory)}"
        else:
            return "Your bag is empty..."

    def move(self, direction):
        # self.current_room = getattr(self.current_room, f"{direction}_to") if f"{direction}_to" in self.current_room.__dict__ else print(
        #     f"This direction doesn't lead anywere. What would you like to do?")
        if f"{direction}_to" in self.current_room.__dict__:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)

        else:
            print(f"This direction doesn't lead anywere. What would you like to do?")

    def pick_up(self):
        print("What item would you like to pickup?")  # todo parser
        item = input("# ").lower().strip()
        # ? how to check class item name
        print("items", self.current_room.items[0].name)
        if item in self.current_room.items:
            self.inventory.append(item)
            self.current_room.items.remove(item)
            print(
                f"You added the {item} to your inventory. \n  Items currently in your bag: {self}")
        else:
            print(f"{item} was not found...")

    def drop(self):
        if self.inventory:
            # todo parser
            print(
                f"Which item would you like to leave behind? \n  Items currently in your bag: {self}")
            item = input("# ").lower().strip()
            if item in self.inventory:
                self.inventory.remove(item)
                self.current_room.items.append(item)
                print(
                    f"You dropped the {item}. \n  Items currently in your bag: {self}")
            else:
                print(f"{item} was not found in your bag...")
        else:
            print("There is nothing in your bag. See what you can find!")
