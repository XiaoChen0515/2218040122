"""
File: test_main.py
Description: Unit tests for the arena combat game.
Author: 林师弘
StudentID: 2218040122
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import unittest
from main import PyroMage, FrostMage, Combatant, Arena, Field

class TestMageCombat(unittest.TestCase):
    def test_pyro_mage_spell(self):
        pyro = PyroMage("Pyro", 100, 20, 5, 100)
        target = Combatant("Target", 100, 10, 5)
        pyro.cast_spell(target)
        self.assertEqual(target.health, 60)  # 100 - (20 + 20)

    def test_frost_mage_spell(self):
        frost = FrostMage("Frost", 100, 15, 10, 100)
        target = Combatant("Target", 100, 10, 5)
        frost.cast_spell(target)  # Assuming no damage due to Ice Block
        self.assertEqual(target.health, 100)  # No damage taken due to Ice Block

if __name__ == "__main__":
    unittest.main()
