# Implement a class to hold room information. This should have name and description attributes.
class Room():
    # ? params include directions?
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        return f"You are in the {self.name}. {self.desc}"


class List(Room):
    def __init__(self, name, desc, items):
        super().__init__(name, desc)
        self.items = items

    def __str__(self):
        return f"You are in the {self.name}. {self.desc}. Items in the room are: {self.items}"


kitchen = {
    "name": "Kitchen",
    "desc": "This is where the food magic happens!",
    "items": ["knife", "bottle", "carrot"]
}

print(Room(kitchen["name"], kitchen["desc"]))
print(List(kitchen["name"], kitchen["desc"], kitchen["items"]))
