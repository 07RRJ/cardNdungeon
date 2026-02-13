from os import system
import random as rng

system("cls")

# ======================================
# BASE
# ======================================

abilities = ["ATTACK", "HEAL", "BLOCK"]

class Slime:
    MAX_HP = 10 
    HP =  10
    STR = 1
    ABILITIES = ["ATTACK"]

# ======================================
# INIT
# ======================================

player = {"MAX_HP": 10, "HP": 10, "STR": 1, "REGEN": 1, "DEFENCE": 1, "ABILITIES": ["ATTACK", "HEAL", "BLOCK"]}

enemeisPerFloor = [[1, 1, 1, 1, 2], [2, 2, 2, 3], [2, 3, 3, 3, 3, 4], [3, 4, 4, 4], [3, 4, 4, 4, 4, 5]]

def generate_enemies(floor):
    xEnemies = rng.choice(enemeisPerFloor[floor])
    enemies = []
    for i in range(xEnemies):
        slime = Slime
        enemies.append(slime)
    return enemies

enemies = generate_enemies(2)


def Attack(attack, enemyHp):
    return enemyHp - attack

def Limit(question, Min, Max):
    while True:
        value = int(input(question))
        if value > Min:
            if value < Max:
                return value

def GetEnemyStats():
    stats = []
    for idx, enemy in enumerate(enemies):
        stats.append(f"({idx + 1}), HP: ({enemy.MAX_HP}/{enemy.HP}), STR: {enemy.STR}")
    print("Enemies:")
    for enemy in stats:
        print(enemy)

while True:
    GetEnemyStats()
    print(f"Player:\nHP: ({player['MAX_HP']}/{player['HP']}), STR: ({player['STR']}), REGEN ({player['REGEN']})")
    for idx, move in enumerate(player["ABILITIES"], 1):
        print(idx, move)
    move = player["ABILITIES"][Limit("your move: ", 0, len(player["ABILITIES"]) + 1) - 1]
    system("cls")
    print(f"you chose: {move}")