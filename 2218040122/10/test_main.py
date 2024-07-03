"""
File: test_main.py
Description: Unit tests for the arena combat game.
Author: 林师弘
StudentID: 2218040122
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import unittest
from combatant import *
from field import Field
from arena import Arena

class TestCombat(unittest.TestCase):
    """单元测试类，用于测试战斗系统的各个方面"""
    def test_combatant_attack(self):
        """测试基础战斗者的攻击方法"""
        c1 = Combatant("Attacker", 100, 20, 5, 10, 15)
        c2 = Combatant("Defender", 100, 15, 10, 20, 25)
        c1.attack(c2)
        self.assertEqual(c2.health, 90)

    def test_arena_battle(self):
        """测试竞技场中的战斗逻辑"""
        arena = Arena("Test Arena")
        c1 = Combatant("Combatant1", 50, 15, 5, 0, 0)
        c2 = Combatant("Combatant2", 50, 10, 5, 0, 0)
        arena.add_combatant(c1)
        arena.add_combatant(c2)
        arena.duel(c1, c2)
        self.assertTrue(c1.is_alive() and not c2.is_alive(), "Should be one combatant standing.")

    def test_pyro_mage_spell(self):
        """测试PyroMage的施法方法"""
        pyro = PyroMage("Pyro", 100, 15, 5, 40, 0)
        target = Combatant("Target", 100, 10, 5, 0, 0)
        pyro.cast_spell(target)
        self.assertEqual(target.health, 70)

    def test_frost_mage_spell(self):
        """测试FrostMage的施法方法"""
        frost = FrostMage("Frost", 100, 10, 5, 50, 0)
        target = Combatant("Target", 100, 10, 5, 0, 0)
        frost.cast_spell(target)
        self.assertEqual(target.health, 88)

    def test_armor_penetration(self):
        """测试战士的护甲防护效果"""
        attacker = Combatant("Attacker", 100, 20, 0, 0, 0)
        defender = Warrior("Defender", 100, 10, 5, 0, 0, 10)
        attacker.attack(defender)
        self.assertEqual(defender.health, 95)

    def test_critical_hit(self):
        """测试Dharok的攻击加成"""
        hero = Dharok("Hero", 100, 20, 5, 0, 0, 0)
        villain = Combatant("Villain", 100, 10, 5, 0, 0)
        hero.health = 50  # Hero is at half health
        hero.attack(villain)
        self.assertEqual(villain.health, 30)

if __name__ == "__main__":
    unittest.main()
