import os, sys
import random as rng
from msvcrt import getwch
from time import sleep

# ======================================
# SECTION: BASE
# ======================================

def cls():
    os.system("cls")

def get_game_folder():
    return getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

class GameData:
    floor = 0
    part = 0
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
        print(f"Player:\nHP: ({self.HP}/{self.MAX_HP}), STR: ({self.STR}), HEAL ({self.HEAL}), DEF ({self.BLOCK}), BLOCK ({self.DEF}), LVL ({self.LVL}), EXP ({self.EXP}/{self.NEXT_LVL})")
    
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
            self.STR += 2
            self.MAX_HP += 1
            self.BLOCK += 1
            self.HEAL += 1

# ======================================
# SECTION: ENEMIES
# ======================================

enemeisPerFloor = [[1, 1, 2], [2, 2, 2, 3], [2, 3, 3, 3, 3, 4], [3, 4, 4, 4], [3, 4, 4, 4, 4, 5]]
enemyTypes = ["Slime", "Rat", "Boar"]

class Enemies:
    current = []
    possible = ["Slime"]
    def generate(self):
        if not self.current:
            xEnemies = rng.choice(enemeisPerFloor[gameData.floor])
            generatedEnemies = []
            for i in range(xEnemies):
                enemy = rng.choice(self.possible)
                if enemy == "Slime":
                    enemy = Slime()
                elif enemy == "Rat":
                    enemy = Rat()
                elif enemy == "Boar":
                    enemy = Boar()
                generatedEnemies.append(enemy)
            self.current = generatedEnemies

class Slime:
    TYPE = "slime"
    def __init__(self, summoned = False):
        floor = gameData.floor + 1
        if summoned:
            self.EXP = 0
        else:
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
    def __init__(self):
        floor = gameData.floor + 1
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
    def __init__(self):
        floor = gameData.floor + 1
        self.EXP = 5 * floor
        self.MAX_HP = 10 * floor
        self.HP = 10 * floor
        self.STR = 3 * floor
    HEAL = 0
    DEF = 0
    BLOCK = 0
    ABILITIES = ["PASS", "BLOCK", "ATTACK"]
    
    def Move(self):
        enemyMove = rng.choice(self.ABILITIES)
        if enemyMove == "ATTACK":
            Attack(self, player)

# ======================================
# SECTION: BOSSES
# ======================================

class KingSlime:
    TYPE = "kingslime"
    def __init__(self):
        floor = gameData.floor + 1
        self.EXP = 20 * floor
        self.MAX_HP = 50 * floor
        self.HP = 50 * floor
        self.STR = 4 * floor
        self.BLOCK = 10 * floor
    MOVE = 0
    HEAL = 0
    DEF = 0
    ABILITIES = ["PASS", "BLOCK", "SUMMON"]
    
    def Move(self):
        self.DEF -= self.DEF // 2 + 1
        if self.DEF < 0:
            self.DEF = 0
        enemyMove = self.ABILITIES[self.MOVE]
        if enemyMove == "BLOCK":
            self.DEF += self.BLOCK
        if enemyMove == "SUMMON":
            slime = Slime(True)
            enemies.current.append(slime)
        self.MOVE += 1
        if self.MOVE > len(self.ABILITIES) - 1:
            self.MOVE = 0

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

def playFloor():
    player.DEF = 0
    while True:
        player.DEF -= player.DEF // 2 + 1
        if player.DEF < 0:
            player.DEF = 0
        if enemies.current and player.HP > 0:
            print(f"Floor {gameData.floor + 1}-{gameData.part + 1}")
            GetEnemyStats()
            player.Stats()
            player.Move()

            for enemy in enemies.current:
                # sleep(1)
                enemy.Move()

            cls()
        if not enemies.current:
            return "won"
        elif player.HP <= 0:
            return "dead"

runing = True

def play():
    result = ""
    while result != "dead":
        if gameData.floor < 5:
            enemies.generate()
            result = playFloor()
            if result == "won":
                if gameData.part < 9:
                    gameData.part += 1
                else:
                    if gameData.floor % 5 == 0:
                        kingSlime = KingSlime()
                        enemies.current = [kingSlime]
                        gameData.part = 0
                        gameData.floor += 1
                        result = playFloor()
                        if result == "won":
                            pass
                        else:
                            return "dead"
                    else:
                        gameData.part = 0
                        gameData.floor += 1
                    # elif gameData.floor % 5 == 1:
                        # pass
            elif result == "dead":
                return "dead"
        else:
            return "won"

while True:
    cls()
    player = Player()
    enemies = Enemies()
    gameData = GameData()
    result = play()
    if result == "won":
        print("you won")
    else:
        print(f"you died, floor: ({gameData.floor + 1}-{gameData.part + 1})")
    print("play again (y/n):")
    while getwch().lower() != "y":
        pass