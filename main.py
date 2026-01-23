import time
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
        
    def menu(self):
        print("Menu: ")
        print("1. 20 ork boyz vs 10 space marine intercessors ")
        print("2. 20 ork boyz vs 20 tyranid hormagaunts ")
        print("3. Exit program ")
        
    def run(self):
        self.welcome_message()
        
        matchup = Matchup()
        combat = Combat()
        
        while True:
            self.menu()
            user_choice = input("Select an option: ")
            
            if user_choice == "1":
                unit_a, unit_b = matchup.orks_vs_space_marine_intercessors()
                self.run_combat(unit_a, unit_b, combat)
                
            elif user_choice == "2":
                unit_a, unit_b = matchup.orks_vs_hormagaunts()
                self.run_combat(unit_a, unit_b, combat)
                
            elif user_choice == "3":
                print("You chose to exit the program, byebye! ")
                break
                
            else:
                print("Invalid options, choose between an option (1-3) ")
                continue
            
            print("Thanks for playing! ")
            input("Press Enter to return to the main menu ")
            
    def run_combat(self, unit_a: Unit, unit_b: Unit, combat: Combat):
        print("=" * 20)
        print(f"Starting combat: {unit_a.name} vs {unit_b.name}")
        print("=" * 20)

        round_number = 1

        while not unit_a.is_destroyed() and not unit_b.is_destroyed():
            print(f"=== ROUND {round_number} ===")
            combat.combat_round(unit_a, unit_b)
            time.sleep(1)
            round_number += 1

        if unit_a.is_destroyed():
            print(f"{unit_a.name} has been wiped out!")
            print(f"{unit_b.name} wins!")
        else:
            print(f"{unit_b.name} has been wiped out!")
            print(f"{unit_a.name} wins!")
        
              
if __name__ == "__main__":
    main = Main()
    main.run()