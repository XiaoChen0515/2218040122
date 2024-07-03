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

    def attack(self, other, field_effect=0):
        """根据攻击力、对方的防御力和场地效果计算实际伤害。"""
        damage = max(self.attack_power + field_effect - other.defense, 0)
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage.")

    def is_alive(self):
        """检查战斗者是否还活着（健康值大于0）。"""
        return self.health > 0


class Ranger(Combatant):
    """游侠类，继承自Combatant，具有使用箭矢攻击的特殊能力。"""

    def __init__(self, name, health, attack_power, defense, arrows=3):
        super().__init__(name, health, attack_power, defense)
        self.arrows = arrows

    def attack(self, other, field_effect=0):
        """如果有箭矢，使用箭矢进行攻击，造成额外伤害。"""
        if self.arrows > 0:
            self.arrows -= 1
            arrow_damage = self.attack_power + 10  # 箭矢提供额外10点伤害
            damage = max(arrow_damage + field_effect - other.defense, 0)
            other.health -= damage
            print(f"{self.name} shoots an arrow at {other.name} for {damage} damage. Arrows left: {self.arrows}")
        else:
            super().attack(other, field_effect)


class Field:
    """场地类，定义竞技场的环境效果。"""

    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def apply_effect(self):
        """根据场地的不同返回不同的效果值。"""
        return self.effect


class Arena:
    """竞技场类，管理战斗者和场地效果。"""

    def __init__(self, field):
        self.combatants = []
        self.field = field

    def add_combatant(self, combatant):
        """向竞技场添加一个战斗者。"""
        self.combatants.append(combatant)
        print(f"{combatant.name} has been added to the arena.")

    def remove_combatant(self, combatant):
        """从竞技场中移除一个战斗者。"""
        self.combatants.remove(combatant)
        print(f"{combatant.name} has been removed from the arena.")

    def battle(self):
        """两个战斗者进行战斗，直到其中一个倒下，场地效果被考虑在内。"""
        if len(self.combatants) < 2:
            print("Not enough combatants to start a battle.")
            return

        field_effect = self.field.apply_effect()
        combatant1, combatant2 = self.combatants[:2]
        while combatant1.is_alive() and combatant2.is_alive():
            combatant1.attack(combatant2, field_effect)
            if combatant2.is_alive():
                combatant2.attack(combatant1, field_effect)

        if combatant1.is_alive():
            print(f"{combatant1.name} wins the battle!")
        else:
            print(f"{combatant2.name} wins the battle!")


if __name__ == "__main__":
    field = Field("Healing Meadows", 5)
    arena = Arena(field)
    combatant1 = Ranger("Robin", 100, 20, 5)
    combatant2 = Combatant("Knight", 100, 15, 10)
    arena.add_combatant(combatant1)
    arena.add_combatant(combatant2)
    arena.battle()
