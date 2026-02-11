from os import system
import random as rng

# ======================================
# BASE
# ======================================

abilities = ["ATTACK", "HEAL", "BLOCK"]

class Slime:
    MAX_HP = 10 
    HP =  10
    ATTACK = 1
    ABILITIES = ["ATTACK"]

# ======================================
# INIT
# ======================================

player = {"MAX_HP": 10, "HP": 10, "ATTACK": 1, "REGEN": 1, "DEFENCE": 1, "ABILITIES": ["ATTACK", "HEAL", "BLOCK"]}

enemeisPerFloor = [[1, 1, 1, 2], [2, 2, 2, 3], [2, 3, 3, 3, 3, 4], [3, 4, 4, 4], [3, 4, 4, 4, 4, 5]]

def generate_enemies(floor):
    xEnemies = rng.choice(enemeisPerFloor[floor])
    enemies = []
    for i in range(xEnemies):
        slime = Slime
        enemies.append(slime)
    return enemies

enemies = generate_enemies(1)

print(enemies)

enemies = generate_enemies(floor)

def attack(attack, enemyHp):
    return enemyHp - attack

def limit(question, Min, Max):
    while True:
        value = int(input(question))
        if value > Min:
            if value < Max:
                return value

# while True:
#     print(f"Player HP: {player["HP"]}, Enemy HP: {enemy["HP"]}")
#     for idx, move in enumerate(player["ABILITIES"], 1):
#         print(idx, move)
#     move = player["ABILITIES"][limit("your move: ", 0, len(player["ABILITIES"]) + 1) - 1]
#     system("cls")
#     print(move)