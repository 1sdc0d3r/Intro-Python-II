class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name+self.description


class ListSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print("Are you sure you want to leave behind your light source?")
