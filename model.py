from weapon import Weapon

class Model():
    def __init__(self, name: str, toughness: int, wounds: int, save: int, weapon: Weapon):
        
        self.name = name
        self.toughness = toughness
        self.max_wounds = wounds
        self.current_wounds = wounds
        self.save = save
        self.weapon = weapon
    
    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name
        
    def is_alive(self):
        return self.current_wounds > 0
    
    def __str__(self):
        return f"{self.name} Toughness:{self.toughness} Wounds:{self.max_wounds} Save:{self.save}+ Weapon:{self.weapon}"

ork_boy = Model("Ork Boyz", 5, 1, 5, weapon = Weapon("Choppa", 3, 3, 4, 1, 1))
ork_nob = Model("Ork Nob", 5, 2, 4, weapon = Weapon("Big Choppa", 3, 3, 7, 1, 2))
print(ork_boy)
print(ork_nob)