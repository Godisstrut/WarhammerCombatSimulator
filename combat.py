import random, time
from weapon import Weapon
from model import Model

class Combat(): # Manages the combat phases between two units, indcluding attack rolls, wound rolls, and saving throws.

    def dice_roll(self): # Simulates a d6 roll
        return random.randint(1, 6)
    
    def wound_rules(self, strength, toughness): # Wounds rolls needed based on strength vs toughness, follows the standard 40k tabletop rules
        if strength >= toughness * 2:
            return 2
        elif strength > toughness:
            return 3
        elif strength == toughness:
            return 4
        elif strength < toughness:
            return 5
        elif strength <= toughness / 2:
            return 6
        
    def fight_phase(self, attacker, defender):
        for weapon in attacker.weapons:
            total_attacks = weapon.attacks * attacker.models
            print(f"{attacker.name} attacks with {weapon.name} with {total_attacks} total attacks ")
            for hit in range(total_attacks):
                hit_roll = self.dice_roll()
                if hit_roll >= weapon.hit:
                    print(f"Hit! rolled a {hit_roll} ")
                    wound_needed = self.wound_rules(weapon.strength, defender.toughness)
                    wound_roll = self.dice_roll()
                    if wound_roll >= wound_needed:
                        print(f"Wounded! rolled a {wound_roll} ")
                        save_roll = self.dice_roll()
                        modified_save = defender.save + weapon.ap
                        if save_roll >= modified_save:
                            print(f"Saved! rolled a {save_roll} against a modified save of {modified_save} ")
                        else:
                            print(f"Save failed! rolled a {save_roll} against a modified save of {modified_save} ")
                            defender.current_wounds -= weapon.damage
                            
    
                            
