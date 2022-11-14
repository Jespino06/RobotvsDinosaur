from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('laser gun')
        pass

    # def __init__(self, name):
    #     self.name = name
    #     self.health = 100
    #     self.active_weapon = Weapon('')
    #     pass
    
    # def attack(self, dinosaur):
    #     self.name = ""
    #     self.dinosaur = dinosaur
    #     pass


    def attack(self, dinosaur):
        self.dinosaur = dinosaur
        dinosaur.health -= 40
        self.active_weapon = 25
        print(f'OB1 shoots the laser gun at T-rex Bo: {dinosaur.health} percent health left!!!')
        pass