class Item:
    def __init__(self, name, description, rarity):
        self.name = name
        self.description = description
        self.rarity = rarity

    def __str__(self):
        return self.name

    def inspect(self):
        print(
            f"{self.name} - {self.description}\n    [Type: {type(self).__name__}, Rarity: {self.rarity}]")


class LightSource(Item):
    def __init__(self, name, description, rarity):
        super().__init__(name, description, rarity)

    def on_drop(self):
        return input(
            "Are you sure you want to leave behind your light source?\n💡") in ("n", "no")


class Weapon(Item):
    def __init__(self, name, description, rarity, damage, range):
        super().__init__(name, description, rarity)
        self.damage = damage

    def inspect(self):
        print(
            f"{self.name} - {self.description}\n    [Type: {type(self).__name__}, Damage:{self.damage}, Rarity: {self.rarity}]")


class Shield(Item):
    def __init__(self, name, description, rarity, block):
        super().__init__(name, description, rarity)
        self.block = block

    def inspect(self):
        print(
            f"{self.name} - {self.description}\n    [Type: {type(self).__name__}, Block:{self.block}, Rarity: {self.rarity}]")
