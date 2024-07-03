"""
File: arena.py
Description: Arena class for the arena combat game.
Author: 林师弘
StudentID: 2218040122
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from field import Field

class Arena:
    def __init__(self, name):
        self.name = name
        self.field = Field(name)
        self.combatants = []

    def add_combatant(self, combatant):
        if combatant not in self.combatants:
            self.combatants.append(combatant)
            print(f"{combatant.name} has been added to the arena.")
        else:
            print(f"{combatant.name} is already in the arena.")

    def remove_combatant(self, combatant):
        if combatant in self.combatants:
            self.combatants.remove(combatant)
            print(f"{combatant.name} has been removed from the arena.")
        else:
            print(f"{combatant.name} was not found in the arena.")

    def list_combatants(self):
        for combatant in self.combatants:
            print(combatant.details())

    def restore_combatants(self):
        for combatant in self.combatants:
            combatant.reset()
        print("All combatants have been restored.")

    def duel(self, combatant1, combatant2):
        if combatant1 not in self.combatants or combatant2 not in self.combatants:
            print("Both combatants must be in the arena to duel.")
            return
        if not combatant1.is_alive() or not combatant2.is_alive():
            print("Both combatants must be alive to duel.")
            return

        print(f"----- Battle has taken place in {self.name} on the {self.field.field_type} between {combatant1.name} and {combatant2.name} -----")
        rounds = 0
        while combatant1.is_alive() and combatant2.is_alive() and rounds < 10:
            self.field.apply_effect(combatant1, combatant2)
            damage1 = combatant1.attack(combatant2)
            print(f"{combatant1.name} attacks {combatant2.name} for {damage1} damage.")
            if not combatant2.is_alive():
                break
            damage2 = combatant2.attack(combatant1)
            print(f"{combatant2.name} attacks {combatant1.name} for {damage2} damage.")
            rounds += 1

        if not combatant1.is_alive():
            print(f"{combatant1.name} has been knocked out!")
        if not combatant2.is_alive():
            print(f"{combatant2.name} has been knocked out!")
        if rounds >= 10:
            print("The duel ended in a draw due to time limit.")
