class Item:
    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity

    def __str__(self):
        return self.name

    def inspect(self):
        print(f"{self.name} - {self.description}")


class LightSource(Item):
    def __init__(self, name, description, rarity):
        super().__init__(name, description, rarity)

    def on_drop(self):
        print("Are you sure you want to leave behind your light source?")


class Weapon(Item):
    def __init__(self, name, description, rarity, damage, range):
        super().__init__(name, description, rarity)
        self.damage = damage


class Shield(Item):
    def __init__(self, name, description, rarity, block):
        super().__init__(name, description, rarity)
        self.block = block
