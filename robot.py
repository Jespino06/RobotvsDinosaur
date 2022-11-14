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
        print(f'OB1 attacks T-rex Bo: {dinosaur.health}')
        pass