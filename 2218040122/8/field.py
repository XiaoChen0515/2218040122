"""
File: field.py
Description: Field class for the arena combat game.
Author: 林师弘
StudentID: 2218040122
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random

class Field:
    def __init__(self, name):
        self.name = name
        self.field_type = self.change_field()

    def change_field(self):
        fields = ["Toxic Wasteland", "Healing Meadows", "Castle Walls"]
        return random.choice(fields)

    def apply_effect(self, combatant1, combatant2):
        if self.field_type == "Toxic Wasteland":
            print("The Toxic Wasteland damages both combatants for 5 health each.")
            combatant1.take_damage(5)
            combatant2.take_damage(5)
        elif self.field_type == "Healing Meadows":
            print("The Healing Meadows heals both combatants for 5 health each.")
            combatant1.health += 5
            combatant2.health += 5
            if combatant1.health > combatant1.max_health:
                combatant1.health = combatant1.max_health
            if combatant2.health > combatant2.max_health:
                combatant2.health = combatant2.max_health
        elif self.field_type == "Castle Walls":
            print("The Castle Walls have no effect.")
