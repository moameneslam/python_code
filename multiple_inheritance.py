class Actor():
    position = ()
    A_type = ''  # player NPC
    hp


class Fighter():

    def punch(hp):
        hp = hp - 1
        return hp


class Melee(Fighter):

    def melee_attack(hp):
        hp = hp - 10
        return hp


class Ranged(Fighter):

    def ranged_attack(hp):
        hp = hp - 7
        return hp


class Warrior(Melee):

    def shield_slam(self, hp):
        hp = (Melee.melee_attack(hp)) - 10
        return hp

    def bladestorm(self, hp):

        for i in range(10):
            hp = Melee.melee_attack(hp)

        return hp


class Ranger(Melee, Ranged):

    def stab_with_arrow(self, hp):
        hp = Melee.melee_attack(hp) - 50
        return hp

    def precision_shot(self, hp):
        hp = Ranged.ranged_attack(hp) - 100
        return hp

bob = Ranger()
enemyhealth = 500
print(bob.precision_shot(enemyhealth))
