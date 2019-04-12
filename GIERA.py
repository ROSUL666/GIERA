import os
import time
import keyboard 
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 40
        self.weap = ["Rusty Sword"]
        xp = open("XP.txt","r")
        self.curxp = xp.read()
        
class Twoj_stary:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 7
        self.goldgain = 15
        self.xp = random.randint(1,20)
Twoj_staryE = Twoj_stary("Twój Stary")



class Goblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
        self.goldgain = 10
        self.xp = random.randint(1,20)
GoblinE = Goblin("Goblin")

def enemyrandom(): ## LOSOWANIE PRZECIWNIKA
    global enemy
    enemynum = random.randint(1, 2)
    if enemynum == 1:
        enemy = Twoj_staryE
    else:
        enemy = GoblinE

def dead(): ## ŚMIERĆ
    os.system("cls")
    print("You are dead XD") 
    time.sleep(5)
    main()  


def win(): ## WYGRANA
    os.system("cls")
    enemy.health = enemy.maxhealth
    PlayerE.gold += enemy.goldgain
    xp = open("XP.txt", "r")
    curxp = xp.read()
    xp.close()
    xp = open("XP.txt", "w")
    total = int(curxp) + enemy.xp
    xp.write(str(total))
    xp.close()
    PlayerE.curxp = total
    print("You have defeated the ",enemy.name)
    print(("You found {0:} gold!").format(enemy.goldgain))
    print(("You gain {0:} XP").format(enemy.xp))
    option = input(" ")
    start1()


def main(): ## MENU GLOWNE
    print("1) Start")
    print("2) Load")
    print("3) Exit")
    option = input("--> ")
    if option == "1":
        start()


def start(): ## TWORZENIE POSTACI
    print("Welcome in best game EU")
    print("What's your name? ")
    name = input("--> ")
    global PlayerE
    PlayerE = Player(name)
    os.system("cls")
    start1()

def start1(): ## GRA
    os.system("cls")
    print("Name: ", PlayerE.name)
    print("Health: ", PlayerE.health)
    print("Gold: ", PlayerE.gold)
    print("Current weapon: ", PlayerE.weap)
    print("XP: ", PlayerE.curxp)
    print("1) Fight ")
    print("2) Do quests for XP ")
    print("3) Store ")
    print("4) Save ")
    print("5) Exit ")
    option = input("--> ")
    if option == "1":
        fight2()
    elif option == "2":
        goexp()
    elif option == "5":
        exit(0)
    else:
        os.system("cls")
        start1()


def goexp(): ## EXPIENIE
    curxp = int(PlayerE.curxp)
    while True:
        curxp+=1
        print(curxp)
        PlayerE.curxp = curxp
        xp = open("XP.txt", "w")
        xp.write(str(curxp))
        xp.close()
        exit
        delay = 2
        while delay > 0:
            delay = delay - 0.016
            time.sleep(0.016)
            pressed = keyboard.is_pressed('q')
            if pressed:
                start1()
        os.system("cls")
        print("To end fight enter q ")

def fight2(): ## WALKA TUROWA , FAJT 1 NIE MA 
    enemyrandom()
    os.system('cls')
    print(("{0:}     vs      {1:}").format(PlayerE.name, enemy.name))
    time.sleep(4)
    while PlayerE.health > 0 or enemy.health > 0:
        pattack = random.randint(PlayerE.base_attack / 2 , PlayerE.base_attack)
        eattack = random.randint(int(enemy.attack / 2), int(enemy.attack))
        if pattack == PlayerE.base_attack / 2:
            print("You miss")
        else:
            enemy.health -= pattack
            print("You deal ",pattack,"damage , HP left ", enemy.health)
        time.sleep(1)
        if enemy.attack == enemy.attack/2:
            print("Enemy missed")
        else:
            PlayerE.health -= eattack
            print("Enemy deal ",eattack," your HP ",PlayerE.health)
        time.sleep(1)
        if PlayerE.health <= 0:
            dead()
        elif enemy.health <= 0:
            win()
        


        

main()

