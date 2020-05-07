# Implement a class to hold room information. This should have name and description attributes.
from textwrap import wrap
import data
from sys import exit


class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.items = []

    def __str__(self):
        response = f"You are located: {self.name} \n"
        for line in wrap(self.desc, width=100):
            response += line + "\n"

        return response.strip()


class Trap(Room):
    def __init__(self, name, desc, damage):
        super().__init__(name, desc)
        self.damage = damage

    def __str__(self):
        if self.name.lower() == "pitfall":
            return f"You encountered a {self.name} trap! {self.desc}"
        else:
            return f"You encountered a {self.name} trap!"
