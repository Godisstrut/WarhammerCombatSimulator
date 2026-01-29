from weapon import Weapon

class Model(): # Represents a single model with its stats and weapon
    def __init__(self, name: str, toughness: int, wounds: int, save: int, invul_save: int | None, weapon: Weapon,  abilities = None): #Todo lägg till Special regler modeller kan ha
        
        self.name = name
        self.toughness = toughness
        self.max_wounds = wounds
        self.current_wounds = wounds
        self.save = save
        self.invul_save = invul_save
        self.abilities = abilities or []
        self.weapon = weapon
    
    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name
        
    def is_alive(self): # Checks if a model is still alive
        return self.current_wounds > 0
    
    def __str__(self):
        invulerable_save = f"{self.invul_save}+" if self.invul_save is not None else "-"
        return f"{self.name} Toughness:{self.toughness} Wounds:{self.max_wounds} Save:{self.save}+ Invulnerable Save:{invulerable_save} Weapon: {self.weapon}"

ork_boy = Model("Ork Boy:", 5, 1, 5, None, weapon = Weapon("Choppa", 3, 3, 4, 1, 1))
ork_nob = Model("Ork Nob:", 5, 2, 4, None, weapon = Weapon("Big Choppa", 3, 3, 7, 1, 2))
bladeguard = Model("Bladeguard Veteran:", 4, 3, 3, 4, weapon = Weapon("Master-Crafted power weapon", 4, 3, 5, 1, 2))
print(ork_boy)
print(ork_nob)
print(bladeguard)