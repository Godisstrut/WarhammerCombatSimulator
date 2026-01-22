import matchup
from weapon import Weapon
from model import Model
from unit import Unit
from matchup import Matchup
from combat import Combat

class Main():
    
    def welcome_message(self):
        print("="*20)
        print("Warhammer 40k combat simulator! ")
        print("="*20)
        

    def run(self):
        self.welcome_message()
        self.user_options()
        
    def menu(self):
        print("Menu: ")
        print("1. 20 ork boyz vs 10 space marine intercessors ")
        print("2. 20 ork boyz vs 20 tyranid hormagaunts ")
        print("3. Exit program ")
        
    def user_options(self):
        matchup = Matchup()
        while True:
            self.menu()
            user_choice = input("Select an option: ")
            
            if user_choice == "1":
                orks, space_marines = matchup.orks_vs_space_marine_intercessors()
                self.run_combat(orks, space_marines)
                
            elif user_choice == "2":
                orks, hormagaunts = matchup.orks_vs_hormaguants()
                self.run_combat(orks, hormagaunts)
                
            elif user_choice == "3":
                print("You chose to exit the program, byebye! ")
                break
                
            else:
                print("Invalid options, choose between an option (1-3) ")
                
    def run_combat(self, attacker: Unit, defender: Unit):
        print("="*20)
        print(f"Starting combat between {attacker.name} and {defender.name} ")
        print("="*20)
        
        
main = Main()
main.run()