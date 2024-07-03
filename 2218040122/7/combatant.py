"""
File: combatant.py
Description: Combatant classes for the arena combat game.
Author: 林师弘
StudentID: 2218040122
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Combatant:
    def __init__(self, name, max_health, strength, defence, magic, ranged):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.strength = strength
        self.defence = defence
        self.magic = magic
        self.ranged = ranged

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        damage = max(self.strength - other.defence, 0)
        other.take_damage(damage)
        return damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def reset(self):
        self.health = self.max_health

    def details(self):
        return f"{self.name} is a {self.__class__.__name__} and has the following stats:\nHealth: {self.health}\nStrength: {self.strength}\nDefence: {self.defence}\nMagic: {self.magic}\nRanged: {self.ranged}"

class Ranger(Combatant):
    def __init__(self, name, max_health, strength, defence, magic, ranged):
        super().__init__(name, max_health, strength, defence, magic, ranged)
        self.arrows = 3

    def attack(self, other):
        if self.arrows > 0:
            damage = self.ranged
            self.arrows -= 1
            print(f"{self.name} fires an arrow at {other.name} for {damage} damage!")
        else:
            damage = super().attack(other)
            print(f"{self.name} attacks {other.name} for {damage} damage!")
        other.take_damage(damage)
        return damage

    def reset(self):
        super().reset()
        self.arrows = 3

class Warrior(Combatant):
    def __init__(self, name, max_health, strength, defence, magic, ranged, armour_value):
        super().__init__(name, max_health, strength, defence, magic, ranged)
        self.armour_value = armour_value

    def take_damage(self, damage):
        if self.armour_value > 0:
            blocked = min(self.armour_value, damage)
            self.armour_value -= blocked
            damage -= blocked
            print(f"{self.name}'s armour blocked {blocked} damage")
            if self.armour_value == 0:
                print(f"{self.name}'s armour shattered!")
        super().take_damage(damage)

    def reset(self):
        super().reset()
        self.armour_value = 10

class Dharok(Warrior):
    def attack(self, other):
        bonus_damage = self.max_health - self.health
        damage = self.strength + bonus_damage
        print(f"The power of Dharok activates adding {bonus_damage} damage")
        other.take_damage(damage)
        return damage

class Guthans(Warrior):
    def attack(self, other):
        damage = self.strength
        heal = self.strength // 5
        self.health = min(self.max_health, self.health + heal)
        print(f"The power of Guthans activates healing {self.name} for {heal}")
        other.take_damage(damage)
        return damage

class Karil(Warrior):
    def attack(self, other):
        damage = self.strength + self.ranged
        print(f"The power of Karil activates adding {self.ranged} damage!")
        other.take_damage(damage)
        return damage

class Mage(Combatant):
    def __init__(self, name, max_health, strength, defence, magic, ranged):
        if self.__class__ == Mage:
            raise TypeError("Mages must be specialized!")
        super().__init__(name, max_health, strength, defence, magic, ranged)
        self.mana = magic
        self.regen_rate = magic // 4

    def cast_spell(self, other):
        raise NotImplementedError

    def reset(self):
        super().reset()
        self.mana = self.magic

class PyroMage(Mage):
    def __init__(self, name, max_health, strength, defence, magic, ranged):
        super().__init__(name, max_health, strength, defence, magic, ranged)
        self.flame_boost = 1

    def cast_spell(self, other):
        bonus_damage = 0
        if self.mana >= 40:
            self.mana -= 40
            self.flame_boost += 1
            print(f"{self.name} casts SuperHeat!")
        elif self.mana >= 10:
            self.mana -= 10
            bonus_damage = 10
            print(f"{self.name} casts FireBlast!")
        else:
            print(f"{self.name} has insufficient mana!")
        self.mana = min(self.magic, self.mana + self.regen_rate)
        damage = (self.strength * self.flame_boost) + bonus_damage
        other.take_damage(damage)
        return damage

class FrostMage(Mage):
    def __init__(self, name, max_health, strength, defence, magic, ranged):
        super().__init__(name, max_health, strength, defence, magic, ranged)
        self.ice_block = False

    def cast_spell(self, other):
        bonus_damage = 0
        if self.mana >= 50:
            self.mana -= 50
            self.ice_block = True
            print(f"{self.name} casts Ice Block!")
        elif self.mana >= 10:
            self.mana -= 10
            bonus_damage = 30
            print(f"{self.name} casts Ice Barrage!")
        else:
            print(f"{self.name} has insufficient mana!")
        self.mana = min(self.magic, self.mana + self.regen_rate)
        damage = (self.magic // 4) + bonus_damage
        other.take_damage(damage)
        return damage

    def take_damage(self, damage):
        if self.ice_block:
            print(f"{self.name}'s ice block absorbed all the damage!")
            self.ice_block = False
        else:
            super().take_damage(damage)
