"""
File: main.py
Description: Main execution script for the arena combat game.
Author: 林师弘
StudentID: 2218040122
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from combatant import *
from field import Field
from arena import Arena

def main():
    # 创建不同的战斗者对象
    tim = Ranger("Tim", 99, 10, 10, 1, 50)
    jay = Warrior("Jay", 99, 1, 99, 1, 1, 1)
    kevin = Dharok("Kevin", 99, 45, 25, 25, 25, 10)
    zac = Guthans("Zac", 99, 45, 30, 1, 1, 10)
    jeff = Karil("Jeff", 99, 50, 40, 1, 10, 5)

    try:
        durial = Mage("Durial", 99, 99, 99, 99, 99)
    except TypeError:
        print("Mages must be specialized!")

    jaina = FrostMage("Jaina", 99, 10, 20, 94, 10)
    zezima = PyroMage("Zezima", 99, 15, 20, 70, 1)

    # 设置第一个竞技场
    falador = Arena("Falador")
    falador.add_combatant(tim)
    falador.add_combatant(jeff)
    falador.list_combatants()

    # 游侠与Karil的决斗
    falador.duel(tim, jeff)

    # 展示不正确的决斗
    falador.duel(tim, jeff)
    falador.duel(jeff, zezima)

    # 恢复战斗者
    falador.list_combatants()
    falador.restore_combatants()
    falador.list_combatants()

    # 移除竞技场中的战斗者
    falador.remove_combatant(jeff)
    falador.remove_combatant(jeff)

    # 设置第二个竞技场
    varrock = Arena("Varrock")
    varrock.add_combatant(kevin)
    varrock.add_combatant(zac)
    varrock.duel(kevin, zac)

    # 设置第三个竞技场
    wilderness = Arena("Wilderness")
    wilderness.add_combatant(jaina)
    wilderness.add_combatant(zezima)
    wilderness.duel(jaina, zezima)

    # 设置最终竞技场
    lumbridge = Arena("Lumbridge")
    lumbridge.add_combatant(jaina)
    lumbridge.add_combatant(jay)
    lumbridge.add_combatant(tim)
    lumbridge.duel(jaina, jay)
    lumbridge.duel(jay, tim)

if __name__ == "__main__":
    main()
