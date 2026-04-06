from abc import ABC

class Creature:
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health

class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    def combat(self, c1_index, c2_index):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]
        
        self.hit(c1, c2)
        self.hit(c2, c1)

        c1_alive = c1.health > 0
        c2_alive = c2.health > 0

        if c1_alive == c2_alive:
            return -1
        elif c1_alive:
            return c1_index
        else:
            return c2_index
        
    def hit(self, attacker, defender):
        pass

class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        temporary_health = defender.health
        defender.health = defender.health - attacker.attack
        if defender.health > 0:
            defender.health = temporary_health
            return True
        else:
            return False
 
class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health = defender.health - attacker.attack
        return defender.health > 0

# Näide 1

creatures = [Creature(1, 2), Creature(1, 3)]
game = TemporaryDamageCardGame(creatures)
print(game.combat(0, 1))
print("-----------------")

game = PermanentDamageCardGame(creatures)
print(game.combat(0, 1))
print(game.combat(0, 1))
print("-----------------")

# Näide 2

creatures = [Creature(2, 2), Creature(2, 2)]
game = PermanentDamageCardGame(creatures)
print(game.combat(0, 1))