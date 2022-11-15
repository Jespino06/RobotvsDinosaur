from robot import Robot
from dinosaur import Dinosaur



class Battlefield:
    def __init__(self):
        self.robot = Robot('OB1')
        self.dinosaur = Dinosaur('T-rex', 6)
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
        print('OB1 is ruthless!!!')

    
    def display_winner(self):
        cannot_survive = True
        
        while cannot_survive == True:
            if self.robot.health == 0:
                cannot_survive = False
                print(f'Game over!!! The winner is...{self.dinosaur.name}!') 
            elif self.dinosaur.health == 0:
                cannot_survive = False
                print(f'Game over!!! The winner is...{self.robot.name}!')
            elif self.dinosaur.health and self.robot.health < 100:
                print('T-rex attacks Bo again!!! ')
                self.robot.health -= 10
                print(self.robot.health)
                print('OB1, shoots at T-rex Bo again!!!')
                self.dinosaur.health -= 20
                print(self.dinosaur.health)
                continue
            
       
       
       
    
    
    