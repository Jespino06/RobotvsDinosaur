from robot import Robot
from dinosaur import Dinosaur



class Battlefield:
    def __init__(self):
        self.robot = Robot('OB1')
        self.dinosaur = Dinosaur('t-rex', 6)
        pass

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        
    def display_welcome(self):
        self.welcome = "Welcome to the battlefield, the game will begin!"
        print(self.welcome)
        pass
    

    def battle_phase(self):
        self.dinosaur.attack(self.robot)
        print("T-rex Bo is on the loose!!!")
        self.robot.attack(self.dinosaur)
        print('OB1 shoots the laser gun at T-rex Bo!!!')

    
    def display_winner(self):
        while self.robot.health <= 100:
            continue
        if self.robot.health == 0:
            print(f'Game over!!! The winner is...{self.robot.name}!')
            
        while self.dinosaur.health <= 100:
            continue
        if self.dinosaur.health == 0:
            print(f'Game over!!! The winner is...{self.dinosaur.name}!')
            

       
       
       
       
        # self.level = 1
    #    self.robot = Robot('OB1')
       
        # if self.level == 1:
        #     print("Level 1!")
        # elif self.level >= '2':
        #     print("Level 2!")
        # elif self.level >= '3':
        #     print("Level 3!")
        # pass

    
        
        # if self.health == 0:
        #     print('Game over!')
        # elif self.health > 0:
        #     print(f"The winner is {self.name} !!!")
        # pass
    
    
    