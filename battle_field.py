from robot import Robot
from dinosaur import Dinosaur

class Battle_field:
    def __init__(self):
        self.attack_active = True

    def run_game(self):
        if self.run_game == self.welcome:
            print("Start!")

        def display_welcome(self):
            self.welcome = "Welcome to the battlefield, the game will begin!"
            print(self.welcome)

        display_welcome()

        def battle_phase(self):
            if self.phase == self.name:
                print("Level 1!")
            elif self.phase >= 2:
                print("Level 2!")
            elif self.phase >= 3:
                print("Level 3!")
        
        battle_phase()

        def display_winner(self):
            if self.health == 0:
                print('Game over!')
            elif self.health > 0:
                print(f"The winner is {self.name} !!!")

        display_winner()
        
    