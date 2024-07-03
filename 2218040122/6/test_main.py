"""
File: test_main.py
Description: Unit tests for the arena combat game.
Author: 林师弘
StudentID: 2218040122
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import unittest
from main import Combatant, PyroMage, Arena, Field

class TestCombatGame(unittest.TestCase):
    def test_critical_hit(self):
        """确保暴击逻辑正确无误。"""
        combatant = Combatant("Hero", 100, 20, 5, 1.0, 0)  # Guaranteed crit
        opponent = Combatant("Villain", 100, 15, 10)
        combatant.attack(opponent)
        # self.assertEqual(opponent.health, 70)
        self.assertEqual(opponent.health, 80)

    def test_armor_penetration(self):
        """确保防御穿透逻辑正确无误。"""
        attacker = Combatant("Attacker", 100, 10, 5, 0, 5)
        defender = Combatant("Defender", 100, 15, 10)
        attacker.attack(defender)
        self.assertEqual(defender.health, 95)

if __name__ == "__main__":
    unittest.main()
