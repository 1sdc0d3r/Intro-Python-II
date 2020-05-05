# Implement a class to hold room information. This should have name and description attributes.
from textwrap import wrap


class Room:
    # ? params include directions?
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.items = []

    def __str__(self):
        response = f"You are located: {self.name} \n"
        for line in wrap(self.desc, width=100):
            response += line + "\n"

        return response.strip()

        # class List(Room):
        #     def __init__(self, name, desc, items):
        #         super().__init__(name, desc)
        #         self.items = items

        #     def __str__(self):
        #         return f"You are in the {self.name}. {self.desc}. Items in the room are: {self.items}"


kitchen = {
    "name": "Kitchen",
    "desc": "This is where the food magic happens!",
    "items": ["knife", "bottle", "carrot"]
}

# room = Room(kitchen["name"], kitchen["desc"])
