"""
File: main.py
Description: Unit tests for the arena combat game.
Author: 林师弘
StudentID: 2218040122
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random

class Combatant:
    """基础战斗者类，定义所有战斗者的共有属性和方法。"""
    def __init__(self, name, health, attack_power, defense, crit_chance=0.1, armor_penetration=0):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.crit_chance = crit_chance
        self.armor_penetration = armor_penetration

    def attack(self, other, field_effect=0):
        """计算伤害，考虑场地效果、暴击和防御穿透。"""
        base_damage = self.attack_power + field_effect
        effective_defense = max(other.defense - self.armor_penetration, 0)
        if random.random() < self.crit_chance:
            damage = 2 * (base_damage - effective_defense)
            print(f"{self.name} hits a critical strike on {other.name} for {damage} damage.")
        else:
            damage = base_damage - effective_defense
            print(f"{self.name} attacks {other.name} for {damage} damage.")
        damage = max(damage, 0)
        other.health -= damage

    def is_alive(self):
        return self.health > 0


class Field:
    """场地类，定义竞技场的环境效果。"""
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def apply_effect(self):
        return self.effect


class Mage(Combatant):
    """法师类，继承自Combatant，具有法术攻击的能力。"""
    def __init__(self, name, health, attack_power, defense, mana):
        super().__init__(name, health, attack_power, defense)
        self.mana = mana


class PyroMage(Mage):
    """火焰法师类，专注于攻击型法术。"""
    def cast_spell(self, other):
        if self.mana >= 40:
            self.mana -= 40
            damage = 20 + self.attack_power
            other.health -= damage
            print(f"{self.name} casts a powerful fire spell on {other.name} for {damage} damage.")
        elif self.mana >= 10:
            self.mana -= 10
            damage = 10 + self.attack_power
            other.health -= damage
            print(f"{self.name} casts a moderate fire spell on {other.name} for {damage} damage.")


class FrostMage(Mage):
    """冰霜法师类，专注于防御型法术和控制。"""

    def cast_spell(self, other):
        if self.mana >= 50:
            self.ice_block = True
            self.mana -= 50
            print(f"{self.name} uses Ice Block, negating the next attack.")
        elif self.mana >= 10 and not self.ice_block:
            self.mana -= 10
            damage = self.attack_power + 30
            other.health -= damage
            print(f"{self.name} casts Ice Barrage on {other.name} for {damage} damage.")
        if self.ice_block:
            self.ice_block = False  # Reset the ice block after it blocks an attack


class Arena:
    """竞技场类，管理战斗者和场地效果。"""
    def __init__(self, field):
        self.combatants = []
        self.field = field

    def add_combatant(self, combatant):
        self.combatants.append(combatant)
        print(f"{combatant.name} has been added to the arena.")

    def remove_combatant(self, combatant):
        self.combatants.remove(combatant)
        print(f"{combatant.name} has been removed from the arena.")

    def battle(self):
        if len(self.combatants) < 2:
            print("Not enough combatants to start a battle.")
            return
        field_effect = self.field.apply_effect()
        combatant1, combatant2 = self.combatants[0], self.combatants[1]
        while combatant1.is_alive() and combatant2.is_alive():
            combatant1.attack(combatant2, field_effect)
            if combatant2.is_alive():
                combatant2.attack(combatant1, field_effect)
        winner = combatant1 if combatant1.is_alive() else combatant2
        print(f"The winner is {winner.name}!")

if __name__ == "__main__":
    field = Field("Neutral Ground", 0)
    arena = Arena(field)
    warrior = Combatant("Warrior", 100, 25, 5, 0.15, 3)
    mage = PyroMage("Mage", 80, 30, 2, 100)
    arena.add_combatant(warrior)
    arena.add_combatant(mage)
    arena.battle()