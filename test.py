from os import system
import random as rng
from msvcrt import getwch

system("cls")

# ======================================
# BASE
# ======================================

class Player:
    MAX_HP = 10
    HP = 10
    STR = 5 
    HEAL = 1
    DEF = 0
    BLOCK = 3
    STAMINA = 0
    EXP = 0
    NEXT_LVL = 5
    LVL = 0
    ABILITIES = ["ATTACK", "HEAL", "BLOCK"]

    def Stats(self):
        print(f"Player:\nHP: ({self.HP}/{self.MAX_HP}), STR: ({self.STR}), HEAL ({self.HEAL}), BLOCK ({self.DEF}), LVL ({self.LVL}), EXP ({self.EXP}/{self.NEXT_LVL})")
    
    def Alive(self):
        if self.HP <= 0:
            print("you died")

    def Move(self):
        for idx, move in enumerate(self.ABILITIES, 1):
            print(idx, move)
        move = self.ABILITIES[Limit("your move: ", 0, len(self.ABILITIES) + 1) - 1]
        print(f"you chose: {move}")
        if move == "ATTACK":
            enemyToAttack = Limit(f"Enemy to attack (1 - {len(enemies)}): ", 0, len(enemies) + 1) - 1
            self.Attack(enemies[enemyToAttack])
            if enemies[enemyToAttack].HP <= 0:
                player.ExpUp(enemies[enemyToAttack].EXP)
                enemies.pop(enemyToAttack)
        elif move == "HEAL":
            if self.HP != self.MAX_HP and self.HP + self.HEAL < self.MAX_HP:
                self.HP += self.HEAL
            else:
                self.HP = self.MAX_HP
        elif move == "BLOCK":
            self.DEF += self.BLOCK

    def ExpUp(self, exp):
        self.EXP += exp
        while self.EXP >= self.NEXT_LVL:
            self.EXP -= self.NEXT_LVL
            self.LVL += 1
            self.NEXT_LVL = int(self.NEXT_LVL ** 1.1)

    def Attack(self, enemy):
        if enemy.DEF:
            enemy.DEF -= self.STR
            if enemy.DEF < 0:
                enemy.HP -= enemy.DEF
                enemy.DEF = 0
        else:
            enemy.HP -= self.STR
player = Player()

class Slime:
    TYPE = "slime"
    EXP = 2
    MAX_HP = 5
    HP = 5
    STR = 1
    HEAL = 0
    DEF = 0
    BLOCK = 0
    ABILITIES = ["ATTACK", "PASS", "PASS"]

    def alive(self):
        if self.HP <= 0:
            print("slime died")
    
    def Attack(self, enemy):
        if enemy.DEF:
            enemy.DEF -= self.STR
            if enemy.DEF < 0:
                enemy.HP -= enemy.DEF
                enemy.DEF = 0
        else:
            enemy.HP -= self.STR

# ======================================
# INIT
# ======================================


enemeisPerFloor = [[1, 2], [2, 2, 2, 3], [2, 3, 3, 3, 3, 4], [3, 4, 4, 4], [3, 4, 4, 4, 4, 5]]

def generate_enemies(floor):
    xEnemies = rng.choice(enemeisPerFloor[floor])
    enemies = []
    for i in range(xEnemies):
        slime = Slime()
        enemies.append(slime)
    return enemies


def Limit(question, Min, Max):
    while True:
        try:
            print(question)
            value = int(getwch())
            if value > Min:
                if value < Max:
                    return value
        except:
            pass

def GetEnemyStats():
    stats = []
    for idx, enemy in enumerate(enemies):
        stats.append(f"({idx + 1}){enemy.TYPE}, HP: ({enemy.HP}/{enemy.MAX_HP}), STR: {enemy.STR}")
    print("Enemies:")
    for enemy in stats:
        print(enemy)

def playFloor(floor, part):
    player.DEF = 0
    while True:
        player.DEF -= player.DEF // 2 + 1
        if player.DEF < 0:
            player.DEF = 0
        if enemies:
            print(f"Floor {floor + 1}-{part}")
            GetEnemyStats()
            player.Stats()
            player.Move()

            for enemy in enemies:
                enemyMove = rng.choice(enemy.ABILITIES)
                if enemyMove == "ATTACK":
                    enemy.Attack(player)

            system("cls")
        else:
            break

while True:
    for floor in range(5):
        for part in range(10):
            enemies = generate_enemies(floor)
            playFloor(floor, part)