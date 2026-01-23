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
        elif strength * 2 <= toughness:
            return 6
        else:
            return 5 # strength < toughness   
        
    def combat_round(self, unit_a, unit_b): # Simulates a full combat round between two units, letting both sides fight  
        print("=== FIGHT PHASE ===")
        self.fight_phase(unit_a, unit_b)
        
        if not unit_b.is_destroyed(): # Checks if the defender is alive to fight back
            print("Other side fights back! ")
            self.fight_phase(unit_b, unit_a)
            
        print("=== END OF FIGHT PHASE ===")
        
        
    def fight_phase(self, attacker, defender): # Function handling combat logic in a fight phase between two units
        
        print("="*20)
        print(f"{attacker.name} vs {defender.name}! ")
        print("="*20)
        
        for model in attacker.alive_models():
            weapon = model.weapon
            print(f"{model.name} attacks with {weapon.name} ")
            
            for attack in range(weapon.attacks):
                if defender.is_destroyed():
                    return
                hit_roll = self.dice_roll()
                if hit_roll >= weapon.hit:
                    print(f"Hit with a {hit_roll} ")
                    time.sleep(1)
                    wound_needed = self.wound_rules(weapon.strength, defender.alive_models()[0].toughness)
                    wound_roll = self.dice_roll()
                    if wound_roll >= wound_needed:
                        print(f"Wounded with a {wound_roll} ")
                        time.sleep(1)
                        target = defender.alive_models()[0]
                        save_roll = self.dice_roll()
                        modified_save = target.save + weapon.ap
                        if save_roll < modified_save:
                            print(f"Save failed with a {save_roll} ")
                            time.sleep(1)
                            target.current_wounds -= weapon.damage
                            print(f"{target.name} takes {weapon.damage} damage! ")
                            print(f"{target.name} has {target.current_wounds} wounds remaining ")
                            
                            if target.current_wounds <= 0:
                                print(f" {target.name} is slain! ")
                            