# Write a class to hold player information, e.g. what room they are in currently.
class Player:
    def __init__(self, name="Jack", current_room="outside"):
        self.name = name
        self.current_room = current_room
        self.inventory = None

    def __str__(self):
        return f"{self.name}"

    def move(self, direction):
        if f"{direction}_to" in self.current_room.__dict__:
            self.current_room = getattr(self.current_room, f"{direction}_to")
        else:
            print(f"This direction doesn't lead anywere. What would you like to do?")
