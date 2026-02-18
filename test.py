from os import system
import random as rng
from msvcrt import getwch
from time import sleep

system("cls")
# ======================================
# SECTION: BASE
# ======================================

class GameData:
    def __init__(self):
        pass

class Player:
    MAX_HP = 20
    HP = 20
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
            enemyToAttack = Limit(f"Enemy to attack (1 - {len(enemies.current)}): ", 0, len(enemies.current) + 1) - 1
            Attack(self, enemies.current[enemyToAttack])
            if enemies.current[enemyToAttack].HP <= 0:
                player.ExpUp(enemies.current[enemyToAttack].EXP)
                enemies.current.pop(enemyToAttack)
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
            # if player.LVL % 2:
            self.STR +=1
            self.MAX_HP += 1
            self.BLOCK += 1
            self.HEAL += 1

player = Player()

# ======================================
# SECTION: ENEMIES
# ======================================

class Enemies:
    current = []
    # def __init__(self):
enemies = Enemies()

class Slime:
    TYPE = "slime"
    def __init__(self, floor):
        floor += 1
        self.EXP = 1 * floor
        self.MAX_HP = 5 * floor
        self.HP = 5 * floor
        self.STR = 1 * floor
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
    def __init__(self, floor):
        floor += 1
        self.EXP = 2 * floor
        self.MAX_HP = 5 * floor
        self.HP = 5 * floor
        self.STR = 2 * floor
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
    def __init__(self, floor):
        floor += 1
        self.EXP = 5 * floor
        self.MAX_HP = 5 * floor
        self.HP = 5 * floor
        self.STR = 1 * floor
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
    generatedEnemies = []
    for i in range(xEnemies):
        enemyTypeOnFloor = [[Slime(floor), Slime(floor), Slime(floor), Slime(floor), Rat(floor)], [Slime(floor), Rat(floor)], [Slime(floor), Rat(floor), Boar(floor)], [Rat(floor), Boar(floor)], [Boar(floor)]]
        enemy = rng.choice(enemyTypeOnFloor[floor])
        generatedEnemies.append(enemy)
    enemies.current = generatedEnemies

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
    for idx, enemy in enumerate(enemies.current):
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
        if enemies.current and player.HP > 0:
            print(f"Floor {floor + 1}-{part + 1}")
            GetEnemyStats()
            player.Stats()
            player.Move()

            for enemy in enemies.current:
                # sleep(1)
                enemy.Move()

            system("cls")
        if not enemies.current:
            return "won"
        elif player.HP <= 0:
            return "dead"

runing = True

while runing:
    floor = 0
    part = 0
    result = ""
    while result != "dead":
        generate_enemies(floor)
        result = playFloor(floor, part)
        if result == "won":
            if part < 9:
                part += 1
            else:
                part = 0
                floor += 1
                if floor > 5:
                    runing = False
                    break
        elif result == "dead":
            runing = False
    print("stuck")


if floor > 5:
    system("cls")
    print("you won")
else:
    system("cls")
    print("you died")