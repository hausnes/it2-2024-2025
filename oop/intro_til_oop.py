import random

class Character:

    def __init__(self, name, level, hp, mana):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana

    def __str__(self):
        return f"\nNavn: {self.get_name()}, Level: {self.get_level()}, HP: {self.get_hp()}, Mana: {self.get_mana()}\n"

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_level(self):
        return self.level

    def get_hp(self):
        return self.hp

    def set_hp(self, new_hp):
        self.hp = new_hp
    
    def is_alive(self):
        return self.hp > 0

    def get_mana(self):
        return self.mana

# Eksempel på bruk av klassen over:
fiende = Character("Rektor", 1, 100, 100)

print(fiende)

print(fiende.is_alive())

fiende.set_hp(0)
print(fiende.is_alive())

print("------------------------")

'''

class Player(Character):
    def __init__(self, name, level, hp, mana, strength, dexterity, intelligence):
        super().__init__(name, level, hp, mana)
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, HP: {self.hp}, Mana: {self.mana}, Strength: {self.strength}, Dexterity: {self.dexterity}, Intelligence: {self.intelligence}"
    
    def attack(self):
        return random.randint(1, self.strength)

spiller = Player("Jo Bjørnar", 1, 100, 100, 10, 10, 10)
print(spiller)

print(f"{spiller.get_name()} angriper: {spiller.attack()}")
'''