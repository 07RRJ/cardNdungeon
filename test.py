from os import system
import random as rng
from msvcrt import getwch

system("cls")
# ======================================
# SECTION: BASE
# ======================================

class GameData:
    def __init__(self):
        pass

class Player:
    MAX_HP = 10
    HP = 10
    STR = 1
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
            Attack(self, enemies[enemyToAttack])
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
            self.NEXT_LVL += self.LVL
            if player.LVL % 2:
                self.STR +=1
                self.MAX_HP += 1
                self.BLOCK += 1
                self.HEAL += 1

player = Player()

# ======================================
# SECTION: ENEMIES
# ======================================

class Slime:
    TYPE = "slime"
    EXP = 1
    MAX_HP = 5
    HP = 5
    STR = 1
    HEAL = 0
    DEF = 0
    BLOCK = 0
    ABILITIES = ["ATTACK", "PASS", "PASS"]
    
    def Move(self):
        enemyMove = rng.choice(self.ABILITIES)
        if enemyMove == "ATTACK":
            Attack(self, player)

class Rat:
    TYPE = "rat"
    EXP = 2
    MAX_HP = 5
    HP = 5
    STR = 2
    HEAL = 0
    DEF = 0
    BLOCK = 0
    ABILITIES = ["ATTACK"]
    
    def Move(self):
        enemyMove = rng.choice(self.ABILITIES)
        if enemyMove == "ATTACK":
            Attack(self, player)

class Boar:
    TYPE = "boar"
    EXP = 5
    MAX_HP = 5
    HP = 5
    STR = 1
    HEAL = 0
    DEF = 0
    BLOCK = 0
    ABILITIES = ["ATTACK", "ATTACK", "BLOCK", "PASS"]
    
    def Move(self):
        enemyMove = rng.choice(self.ABILITIES)
        if enemyMove == "ATTACK":
            Attack(self, player)

# ======================================
# SECTION: FUNCS
# ======================================

def Attack(self, enemy):
    if self.STR >= enemy.DEF + enemy.HP:
        enemy.DEF = 0
        enemy.HP = 0
    elif enemy.DEF:
        enemy.DEF -= self.STR
        if enemy.DEF < 0:
            enemy.HP -= enemy.DEF
            enemy.DEF = 0
    else:
        enemy.HP -= self.STR

enemeisPerFloor = [[1, 1, 2], [2, 2, 2, 3], [2, 3, 3, 3, 3, 4], [3, 4, 4, 4], [3, 4, 4, 4, 4, 5]]

def generate_enemies(floor):
    xEnemies = rng.choice(enemeisPerFloor[floor])
    enemies = []
    for i in range(xEnemies):
        enemyTypeOnFloor = [[Slime(), Slime(), Rat()], [Slime(), Rat(), Rat()], [Slime(), Rat(), Boar()], [Rat(), Boar()], [Boar()]]
        enemy = rng.choice(enemyTypeOnFloor[floor])
        enemies.append(enemy)
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

# ======================================
# SECTION: THE GAME LOOP STUFF
# ======================================

def playFloor(floor, part):
    player.DEF = 0
    while True:
        player.DEF -= player.DEF // 2 + 1
        if player.DEF < 0:
            player.DEF = 0
        if enemies:
            print(f"Floor {floor + 1}-{part + 1}")
            GetEnemyStats()
            player.Stats()
            player.Move()

            for enemy in enemies:
                enemy.Move()

            system("cls")
        else:
            break

while True:
    for floor in range(5):
        for part in range(10):
            enemies = generate_enemies(floor)
            playFloor(floor, part)