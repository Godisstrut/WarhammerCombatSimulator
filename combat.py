import random, time
from weapon import Weapon
from model import Model

class Combat(): # Manages the combat phases between two units, indcluding attack rolls, wound rolls, and saving throws.

    def dice_roll(self): # Simulates a d6 roll
        return random.randint(1, 6)
    
    def unit_status(self, unit):
        print(f"{unit.name}: {len(unit.alive_models())}") # Prints number of alive models in a unit
    
    def wound_rules(self, strength, toughness): # Wounds rolls needed based on strength vs toughness, follows the standard 40k tabletop rules
        if strength >= toughness * 2:
            return 2
        elif strength > toughness:
            return 3
        elif strength == toughness:
            return 4
        elif strength * 2 <= toughness:
            return 6
        else:
            return 5 # strength < toughness   
        
    def combat_round(self, unit_a, unit_b): # Simulates a full combat round between two units, letting both sides fight  
        self.unit_status(unit_a)
        print("===== VS =====")
        self.unit_status(unit_b)
        input("Press Enter to begin the combat ")
        
        kills = self.fight_phase(unit_a, unit_b) # Begins fightphase with unit_a starting 
        print()
        print(f"{unit_a.name} killed {kills} models this round  ")
        print(f"{unit_b.name} remaining: {len(unit_b.alive_models())} models ")
        
        if not unit_b.is_destroyed(): # Checks if the defender is alive to fight back
            print("Switching sides... ")
            print()
            time.sleep(3)
            
            kills = self.fight_phase(unit_b, unit_a) # Switches the side with unit_b hitting back
            print(f"The {unit_b.name} killed {kills} {unit_a.name} models this round ")
            print(f"{unit_a.name} remaining models: {len(unit_a.alive_models())} ")
        
        
    def fight_phase(self, attacker, defender): # Function handling combat logic in a fight phase between two units
        
        print("="*20)
        print(f" {attacker.name} hitting {defender.name}! ")
        print("="*20)
        
        kills_this_phase = 0 # Counts number of kills made per phase
        
        for model in attacker.alive_models(): # Checks number of alive models that are eligble to attack
            weapon = model.weapon
            print(f"{model.name} attacks with {weapon.name} ")
            
            for attack in range(weapon.attacks):
                if defender.is_destroyed(): 
                    return kills_this_phase # Stops attack sequencing if all defender models are destroyed
                hit_roll = self.dice_roll()
                if hit_roll >= weapon.hit:
                    print(f"Hit with a {hit_roll} ")
                    time.sleep(0.75)
                    wound_needed = self.wound_rules(weapon.strength, defender.alive_models()[0].toughness)
                    wound_roll = self.dice_roll()
                    if wound_roll >= wound_needed:
                        print(f"Wounded with a {wound_roll} ")
                        time.sleep(0.75)
                        target = defender.alive_models()[0]
                        save_roll = self.dice_roll()
                        modified_save = target.save + weapon.ap
                        if save_roll < modified_save:
                            print(f"Save failed with a {save_roll}, needed a {modified_save}+ ")
                            time.sleep(0.75)
                            target.current_wounds -= weapon.damage
                            print(f"{target.name} takes {weapon.damage} damage! ")
                            print(f"{target.name} has {target.current_wounds} wounds remaining ")
                            
                            if target.current_wounds <= 0:
                                print(f" {target.name} is slain! ")
                                kills_this_phase += 1
        
        return kills_this_phase
                            