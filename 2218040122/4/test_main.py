"""
File: test_main.py
Description: Unit tests for the arena combat game.
Author: 林师弘
StudentID: 2218040122
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import unittest
from main import Combatant, Ranger, Arena, Field

class TestCombatGame(unittest.TestCase):
    def test_ranger_attack_with_arrows(self):
        """测试游侠使用箭矢攻击是否正常工作。"""
        field = Field("Neutral", 0)
        ranger = Ranger("Robin", 50, 15, 2, 3)
        combatant = Combatant("Knight", 50, 10, 1)
        ranger.attack(combatant, field.apply_effect())
        self.assertEqual(combatant.health, 26)  # 50 - (15 + 10 - 1)

    def test_ranger_attack_without_arrows(self):
        """测试游侠在没有箭矢时进行普通攻击。"""
        field = Field("Neutral", 0)
        ranger = Ranger("Robin", 50, 15, 2, 0)
        combatant = Combatant("Knight", 50, 10, 1)
        ranger.attack(combatant, field.apply_effect())
        self.assertEqual(combatant.health, 36)  # 50 - (15 - 1)

if __name__ == "__main__":
    unittest.main()
