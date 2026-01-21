from weapon import Weapon

class Model(Weapon):
    def __init__(self, name: str, toughness: int, wounds: int, save: int, weapon):
        
        self.name = name
        self.toughness = toughness
        self.max_wounds = wounds
        self.current_wounds = wounds
        self.save = save
        self.weapon = weapon
        
    def is_alive(self):
        return self.current_wounds > 0
    
    def __str__(self):
        return f"{self.name} Toughness:{self.toughness} Wounds:{self.max_wounds} Save:{self.save}+ Weapon:{self.weapon.name}"

ork_boy = Model("Ork Boyz", 5, 1, 5, Weapon("Choppa", 3, 3, 4, 0, 1))
ork_nob = Model("Ork Nob", 5, 2, 4, Weapon("Big Choppa", 3, 3, 7, -1, 2))
print(ork_boy)
print(ork_nob)