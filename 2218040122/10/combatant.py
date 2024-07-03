"""
File: combatant.py
Description: Combatant classes for the arena combat game.
Author: 林师弘
StudentID: 2218040122
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Combatant:
    """基础战斗者类，定义所有战斗者的共有属性和方法。"""
    def __init__(self, name, max_health, strength, defence, magic, ranged):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.strength = strength
        self.defence = defence
        self.magic = magic
        self.ranged = ranged

    def is_alive(self):
        """判断战斗者是否存活"""
        return self.health > 0

    def attack(self, other):
        """进行攻击，计算伤害并扣除对方生命值"""
        damage = max(self.strength - other.defence, 0)
        other.take_damage(damage)
        return damage

    def take_damage(self, damage):
        """受到伤害，减少生命值"""
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def reset(self):
        """重置生命值"""
        self.health = self.max_health

    def details(self):
        """返回战斗者的详细信息"""
        return f"{self.name} is a {self.__class__.__name__} and has the following stats:\nHealth: {self.health}\nStrength: {self.strength}\nDefence: {self.defence}\nMagic: {self.magic}\nRanged: {self.ranged}"

class Ranger(Combatant):
    """游侠类，继承自战斗者，增加了箭矢数量属性"""
    def __init__(self, name, max_health, strength, defence, magic, ranged):
        super().__init__(name, max_health, strength, defence, magic, ranged)
        self.arrows = 3

    def attack(self, other):
        """游侠的攻击方法，优先使用箭矢"""
        if self.arrows > 0:
            damage = self.ranged
            self.arrows -= 1
            print(f"{self.name} fires an arrow at {other.name} for {damage} damage!")
        else:
            damage = super().attack(other)
            print(f"{self.name} attacks {other.name} for {damage} damage!")
        other.take_damage(damage)
        return damage

    def reset(self):
        """重置生命值和箭矢数量"""
        super().reset()
        self.arrows = 3

class Warrior(Combatant):
    """战士类，继承自战斗者，增加了护甲值属性"""
    def __init__(self, name, max_health, strength, defence, magic, ranged, armour_value):
        super().__init__(name, max_health, strength, defence, magic, ranged)
        self.armour_value = armour_value

    def take_damage(self, damage):
        """战士的受伤方法，考虑护甲的防护效果"""
        if self.armour_value > 0:
            blocked = min(self.armour_value, damage)
            self.armour_value -= blocked
            damage -= blocked
            print(f"{self.name}'s armour blocked {blocked} damage")
            if self.armour_value == 0:
                print(f"{self.name}'s armour shattered!")
        super().take_damage(damage)

    def reset(self):
        """重置生命值和护甲值"""
        super().reset()
        self.armour_value = 10

class Dharok(Warrior):
    """Dharok类，继承自战士，增加了基于生命值的攻击加成"""
    def attack(self, other):
        """Dharok的攻击方法，增加低生命值时的攻击加成"""
        bonus_damage = self.max_health - self.health
        damage = self.strength + bonus_damage
        print(f"The power of Dharok activates adding {bonus_damage} damage")
        other.take_damage(damage)
        return damage

class Guthans(Warrior):
    """Guthans类，继承自战士，增加了攻击时的治疗效果"""
    def attack(self, other):
        """Guthans的攻击方法，增加治疗效果"""
        damage = self.strength
        heal = self.strength // 5
        self.health = min(self.max_health, self.health + heal)
        print(f"The power of Guthans activates healing {self.name} for {heal}")
        other.take_damage(damage)
        return damage

class Karil(Warrior):
    """Karil类，继承自战士，增加了攻击时的额外伤害"""
    def attack(self, other):
        """Karil的攻击方法，增加额外的远程伤害"""
        damage = self.strength + self.ranged
        print(f"The power of Karil activates adding {self.ranged} damage!")
        other.take_damage(damage)
        return damage

class Mage(Combatant):
    """基础法师类，不能直接实例化，必须通过子类进行实例化"""
    def __init__(self, name, max_health, strength, defence, magic, ranged):
        if self.__class__ == Mage:
            raise TypeError("Mages must be specialized!")
        super().__init__(name, max_health, strength, defence, magic, ranged)
        self.mana = magic
        self.regen_rate = magic // 4

    def cast_spell(self, other):
        raise NotImplementedError

    def reset(self):
        """重置生命值和法力值"""
        super().reset()
        self.mana = self.magic

class PyroMage(Mage):
    """PyroMage类，继承自法师，增加了火焰法术的能力"""
    def __init__(self, name, max_health, strength, defence, magic, ranged):
        super().__init__(name, max_health, strength, defence, magic, ranged)
        self.flame_boost = 1

    def cast_spell(self, other):
        """PyroMage的施法方法，增加火焰法术的效果"""
        bonus_damage = 0
        if self.mana >= 40:
            self.mana -= 40
            self.flame_boost += 1
            print(f"{self.name} casts SuperHeat!")
        elif self.mana >= 10:
            self.mana -= 10
            bonus_damage = 10
            print(f"{self.name} casts FireBlast!")
        else:
            print(f"{self.name} has insufficient mana!")
        self.mana = min(self.magic, self.mana + self.regen_rate)
        damage = (self.strength * self.flame_boost) + bonus_damage
        other.take_damage(damage)
        return damage

class FrostMage(Mage):
    """FrostMage类，继承自法师，增加了冰霜法术的能力"""
    def __init__(self, name, max_health, strength, defence, magic, ranged):
        super().__init__(name, max_health, strength, defence, magic, ranged)
        self.ice_block = False

    def cast_spell(self, other):
        """FrostMage的施法方法，增加冰霜法术的效果"""
        bonus_damage = 0
        if self.mana >= 50:
            self.mana -= 50
            self.ice_block = True
            print(f"{self.name} casts Ice Block!")
        elif self.mana >= 10:
            self.mana -= 10
            bonus_damage = 30
            print(f"{self.name} casts Ice Barrage!")
        else:
            print(f"{self.name} has insufficient mana!")
        self.mana = min(self.magic, self.mana + self.regen_rate)
        damage = (self.magic // 4) + bonus_damage
        other.take_damage(damage)
        return damage

    def take_damage(self, damage):
        """FrostMage的受伤方法，考虑冰霜法术的防护效果"""
        if self.ice_block:
            print(f"{self.name}'s ice block absorbed all the damage!")
            self.ice_block = False
        else:
            super().take_damage(damage)
