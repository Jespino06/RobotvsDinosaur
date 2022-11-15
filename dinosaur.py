class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = 6
        self.health = 100
        pass

    def attack(self, robot):
        self.robot = robot
        robot.health -= 10
        self.attack_power = 6
        print(f'T-rex Bo attacks Robot: {robot.health} percent health left!!!')
        pass
   
    
