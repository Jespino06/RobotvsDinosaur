from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('laser gun')
        pass

    def attack(self, dinosaur):
        self.dinosaur = dinosaur
        dinosaur.health -= 20
        self.active_weapon = 10
        print(f'Yeti-2D shoots the laser gun at Roxette Rex: {dinosaur.health} percent health left!!!')
        pass