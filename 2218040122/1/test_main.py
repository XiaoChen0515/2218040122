"""
File: test_main.py
Description: Unit tests for the arena combat game.
Author: 林师弘
StudentID: 2218040122
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import unittest
from main import Combatant, Arena

class TestCombatGame(unittest.TestCase):
    def test_combatant_attack(self):
        """测试战斗者攻击是否正常工作。"""
        c1 = Combatant("Combatant1", 50)
        c2 = Combatant("Combatant2", 50)
        c1.attack(c2)
        self.assertEqual(c2.health, 40)

    def test_arena_battle(self):
        """测试竞技场战斗是否按预期进行。"""
        arena = Arena()
        c1 = Combatant("Combatant1", 50)
        c2 = Combatant("Combatant2", 50)
        arena.add_combatant(c1)
        arena.add_combatant(c2)
        arena.battle()
        self.assertTrue(not (c1.is_alive() and c2.is_alive()), "Should not have both combatants standing.")

if __name__ == "__main__":
    unittest.main()
