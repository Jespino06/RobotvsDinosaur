class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = 6
        self.health = 100
        pass

    def attack(self, robot):
        self.robot = robot
        self.health -= 20
        print(f'T-rex Bo attacks Robot: {self.health}')
        pass
   
    
