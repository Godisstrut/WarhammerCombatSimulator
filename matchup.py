from weapon import Weapon
from model import Model
from unit import Unit

class Matchup(): # Factory class to create preset matchups between different units
    
    def create_ork_boy(self):
        choppa = Weapon("Choppa", 3, 3, 4, 1, 1)
        return Model("Ork Boy", 5, 1, 5, choppa)
    
    def create_ork_nob(self):
        power_claw = Weapon("Power Claw", 3, 4, 8, 2, 2)
        return Model("Ork Nob", 5, 2, 4, power_claw)
    
    def create_assault_intercessor(self):
        chain_sword = Weapon("Astartes Chainsword", 4, 3, 4, 1, 1)
        return Model("Assault Intercessor", 4, 2, 3, chain_sword)
    
    def create_intercessor_sergeant(self):
        power_fist = Weapon("Power Fist", 3, 3, 8, 2, 2)
        return Model("Intercessor Sergeant", 4, 2, 3, power_fist)
    
    def create_bladeguard_veteran(self):
        power_sword = Weapon("Master Crafted Power Sword", 4, 3, 5, 2, 2)
        return Model("Bladeguard Veteran", 4, 3, 3, power_sword)
    
    def create_hormaguant(self):
        scything_talon = Weapon("Scything Talons", 3, 4, 3, 1, 1)
        return Model("Hormagaunt", 3, 1, 5, scything_talon)
    
    # PRESET MATCHUPS
    
    def orks_vs_space_marine_intercessors(self): # Creates a preset matchup between ork boyz and space marine intercessors
        orks = Unit("Ork Boyz", self.create_ork_boy, 9)
        orks.add_model(self.create_ork_nob()) # Adds a ork nob leader to the unit
        space_marine_intercessors = Unit("Assault Intercessors", self.create_assault_intercessor, 9)
        space_marine_intercessors.add_model(self.create_intercessor_sergeant()) # Adds a sergeant to the unit
        return orks, space_marine_intercessors
    
    def orks_vs_hormaguants(self): # Creates a preset matchup between ork boyz and tyranid hormagaunts
        orks = Unit("Ork Boyz", self.create_ork_boy, 9)
        orks.add_model(self.create_ork_nob()) 
        hormagaunts = Unit("Hormagaunts", self.create_hormaguant, 20)
        return orks, hormagaunts
    
    def nobz_vs_bladeguard_veterans(self):
        ork_nobz = Unit("Ork Nobz", self.create_ork_nob, 5)
        space_marine_bladeguard = Unit("Bladeguard Veterans", self.create_bladeguard_veteran, 3)
        return ork_nobz, space_marine_bladeguard