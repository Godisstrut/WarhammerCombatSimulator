from weapon import Weapon
from model import Model
from unit import Unit
from matchup import Matchup

class Main():
    
    def welcome_message(self):
        print("="*20)
        print("Warhammer 40k combat simulator! ")
        print("="*20)
        

    def run(self):
        self.welcome_message()
        self.Menu()
        
    def Menu(self):
        print("Menu: ")
        print("1. Start a preset matchup ")
        
main = Main()
main.run()