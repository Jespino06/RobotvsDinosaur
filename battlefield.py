from robot import Robot
from dinosaur import Dinosaur



class Battlefield:
    def __init__(self):
        self.robot = Robot('Yeti-2D')
        self.dinosaur = Dinosaur('Roxette Rex', 6)
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
        print("Roxette Rex is on the loose!!!")
        self.robot.attack(self.dinosaur)
        print('Yeti-2D is ruthless!!!')

    
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
                print('Roxette Rex attacks Yeti-2D again!!! ')
                self.robot.health -= 10
                print(self.robot.health)
                print('Yeti-2D, shoots at Roxette Rex again!!!')
                self.dinosaur.health -= 20
                print(self.dinosaur.health)
                continue
            
       
       
       
    
    
    