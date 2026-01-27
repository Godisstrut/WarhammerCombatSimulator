import time
from weapon import Weapon
from model import Model
from unit import Unit
from matchup import Matchup
from combat import Combat

class Main():
    
    def welcome_message(self): # Welcome message for the user
        print("="*20)
        print("Warhammer 40k combat simulator! ")
        print("="*20)
        
    def menu(self): # Presents the user with a menu of preset matchups
        print("Menu: ")
        print("1. 15 Ork Boyz vs 10 Space marine Assualt Intercessors ")
        print("2. 10 Ork Boyz vs 20 Tyranid Hormagaunts ")
        print("3. 5 Ork Nobz vs 3 Bladeguard Veterans")
        print("4. Exit program ")
         
    def run(self): # Main method for running the program
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
                unit_a, unit_b = matchup.orks_vs_hormaguants()
                self.run_combat(unit_a, unit_b, combat)
            
            elif user_choice == "3":
                unit_a, unit_b = matchup.nobz_vs_bladeguard_veterans()
                self.run_combat(unit_a, unit_b, combat)
                
            elif user_choice == "4":
                print("You chose to exit the program, byebye! ")
                break
                
            else:
                print("Invalid options, choose between an option (1-4) ")
                continue
            
            print("Feel like playing again? ")
            input("Press Enter to return to the main menu ")
            
    def run_combat(self, unit_a: Unit, unit_b: Unit, combat: Combat): # Runs the combat loop between two units
        
        mode = ""
        while mode not in ("slow", "fast"):
            mode = input("Fast or slow paced combat? ").lower()
            
        print("=" * 20)
        print("Initializing combat... ")
        print("=" * 20)
        
        time.sleep(2)
        print()

        round_number = 1

        while not unit_a.is_destroyed() and not unit_b.is_destroyed():
            print(f"=== ROUND: {round_number} ===")
            combat.combat_round(unit_a, unit_b, mode)
            time.sleep(1)
            round_number += 1

        if unit_a.is_destroyed():
            print(f"{unit_b.name} wins with {len(unit_b.alive_models())} models remaining! ")
        else:
            print(f"{unit_a.name} wins with {len(unit_a.alive_models())} models remaining! ")
        
              
if __name__ == "__main__":
    main = Main()
    main.run()