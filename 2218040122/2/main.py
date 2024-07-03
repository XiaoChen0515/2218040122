"""
File: main.py
Description: Unit tests for the arena combat game.
Author: 林师弘
StudentID: 2218040122
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Combatant:
    """基础战斗者类，定义所有战斗者的共有属性和方法。"""

    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, other):
        """根据攻击力和对方的防御力计算实际伤害。"""
        damage = max(self.attack_power - other.defense, 0)
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage.")

    def is_alive(self):
        """检查战斗者是否还活着（健康值大于0）。"""
        return self.health > 0


class Arena:
    """竞技场类，管理战斗者和战斗逻辑。"""

    def __init__(self):
        self.combatants = []

    def add_combatant(self, combatant):
        """向竞技场添加一个战斗者。"""
        self.combatants.append(combatant)
        print(f"{combatant.name} has been added to the arena.")

    def remove_combatant(self, combatant):
        """从竞技场中移除一个战斗者。"""
        self.combatants.remove(combatant)
        print(f"{combatant.name} has been removed from the arena.")

    def battle(self):
        """两个战斗者进行战斗，直到其中一个倒下。"""
        if len(self.combatants) < 2:
            print("Not enough combatants to start a battle.")
            return

        combatant1, combatant2 = self.combatants[:2]
        while combatant1.is_alive() and combatant2.is_alive():
            combatant1.attack(combatant2)
            if combatant2.is_alive():
                combatant2.attack(combatant1)

        if combatant1.is_alive():
            print(f"{combatant1.name} wins the battle!")
        else:
            print(f"{combatant2.name} wins the battle!")


class Field:
    """场地类，定义竞技场的环境。目前没有特别功能。"""

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    # 示例代码
    arena = Arena()
    combatant1 = Combatant("Warrior", 100, 20, 5)
    combatant2 = Combatant("Mage", 100, 15, 3)
    arena.add_combatant(combatant1)
    arena.add_combatant(combatant2)
    arena.battle()
