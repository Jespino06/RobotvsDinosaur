class Weapon:
    def __init__(self):
        self.name = ''
        self.attack_power = 100
    
    def __init__(self, name, attack_power):
        self.name = ""
        self.attack_power = int
        self.damage_per_attack = int


    def laser_gun(self):
        self.attack_power = 20
        self.damage_per_attack = 10
        self.health -= self.damage_per_attack
    


