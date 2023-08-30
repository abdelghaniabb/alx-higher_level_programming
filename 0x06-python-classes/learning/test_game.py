import random
import math
"""
https://www.youtube.com/watch?v=1AGyBuVCTeE&t=8s
sam attacks paul and deals 9 damage
paul is down to 10 health
paul attacks sam and deals 7 damage
sam is down to 7 health
sam attacks paul and deals 19 damage
paul is down to -9 health
paull has died and sam is victorious
game over
"""
# Waarrior & Battle class
class Warrior:

    def __init__(self, name="Warrior", health=0, attackMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attackMax = attackMax
        self.blockMax = blockMax

    def attack(self):
        attackAmt = self.attackMax * (random.random()+ .5)

        return attackAmt

    def block(self):
        blockAmt = self.blockMax * (random.random()+ .5)

        return blockAmt

class Battle:

    def startFight(self, Warrior1, Warrior2):

        while True:
            if self.getAttackResult(Warrior1, Warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(Warrior2, Warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(WaarriorA, WaarriorB):

        WaarriorAAttackAmt = WaarriorA.attack()

        WaarriorBBlockAmt = WaarriorB.block()

        damage2WarriorB = math.ceil(WaarriorAAttackAmt - WaarriorBBlockAmt)

        WaarriorB.health = WaarriorB.health - damage2WarriorB

        print("{} attacks {} and deals {} damage".format(WaarriorA.name, WaarriorB.name, damage2WarriorB))

        print("{} is down to {} health".format(WaarriorB.name, WaarriorB.health))

        if WaarriorB.health <= 0:
            print("{} has died and {} is victorious".format(WaarriorB.name, WaarriorA.name))
            return "Game Over"
        else:
            return "fight Again"

def main():
    maximus = Warrior("Maximus", 50, 20, 10)

    galaaxon = Warrior("Galaxon", 50, 20, 10)

    battle = Battle()

    battle.startFight(maximus, galaaxon)

main()
# Worriors will have name, health, and attack maximums
# They will have the capabilites to attack and block random amounts

#" Attack random() 0.0 to 1.0 * maxAttack + .5

# Black will use random()

# Battle class capability of lopping until 1 worrior dies
#woriors will each get a turn to attack each other

 