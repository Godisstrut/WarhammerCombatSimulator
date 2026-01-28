import random, time
from weapon import Weapon
from model import Model
from collections import defaultdict

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
        
    def combat_round(self, unit_a, unit_b, mode = "slow"): # Simulates a full combat round between two units, letting both sides fight  
        self.unit_status(unit_a)
        print("===== VS =====")
        self.unit_status(unit_b)
        input("Press Enter to begin the combat ")
        
        fight_mode = self.fight_phase_fast if mode == "fast" else self.fight_phase
        
        if not unit_a.is_destroyed():
            kills = fight_mode(unit_a, unit_b) # Begins fightphase with unit_a starting 
            print()
            print(f"{unit_a.name} killed {kills} models this round  ")
            print(f"{unit_b.name} remaining: {len(unit_b.alive_models())} models ")
        
        if not unit_b.is_destroyed(): # Checks if the defender is alive to fight back
            print("Switching sides... ")
            print()
            time.sleep(2)
            
            kills = fight_mode(unit_b, unit_a) # Switches the side with unit_b hitting back
            print(f"The {unit_b.name} killed {kills} {unit_a.name} models this round ")
            print(f"{unit_a.name} remaining models: {len(unit_a.alive_models())} ")
        
        
    def fight_phase(self, attacker, defender): # Function handling combat logic in a fight phase between two units
        print("="*20)
        print(f" {attacker.name} hitting {defender.name}! ")    
        print("="*20)
        
        kills_this_phase = 0  # Counts number of kills made per phase
        
        for model in attacker.alive_models(): # Checks number of alive models that are eligble to attack
            if defender.is_destroyed(): 
                    return kills_this_phase # Stops attack sequencing if all defender models are destroyed
            weapon = model.weapon
            print()
            print(f"{model.name} attacks with his {weapon.name}! {weapon.attacks}A") # Prints name and number of a attacks for a model
            time.sleep(1)
            
            hits = 0
            for attack in range(weapon.attacks): # attack sequence checking how many hits go through
                if self.dice_roll() >= weapon.hit:
                    hits += 1
            print(f"Hits: {hits}")
            if hits == 0:
                continue
            time.sleep(1)
            
            target = defender.alive_models()[0] # Target is an alive model first in the list
            wound_needed = self.wound_rules(weapon.strength, target.toughness)
            wounds = 0
            for hit in range(hits): # Takes the successful hits and checks how many wounds go through
                if self.dice_roll() >= wound_needed:
                    wounds += 1
            print(f"Wounds: {wounds}")
            if wounds == 0:
                continue
            time.sleep(1)
            
            failed_saves = 0
            for wound in range(wounds): # Takes the successful wounds and checks how many saves are failed
                save_roll = self.dice_roll()
                modified_save = target.save + weapon.ap # The required save of a model, save - the armor piercing value. eg 3+ save with 1 ap becomes 4+
                if target.invul_save is not None:
                    save_needed = min(modified_save, target.invul_save)
                else:
                    save_needed = modified_save
                if save_roll < save_needed:
                    failed_saves += 1
                    print(f"Save failed with a roll of {save_roll}, needed a {save_needed}+ ") # Prints save roll needed for the user, for clarity
            print(f"Unsaved wounds: {failed_saves}")
            time.sleep(1)
            
            for save in range(failed_saves): # Takes the failed saves and applies the correct damage
                if defender.is_destroyed():
                    return kills_this_phase
                target = defender.alive_models()[0]
                target.current_wounds -= weapon.damage 
                print(f"{target.name} takes {weapon.damage} damage! {target.name} has {target.current_wounds} wounds remaining ")
                if target.current_wounds <= 0:
                    print(f"{target.name} is slain!")
                    kills_this_phase += 1
            time.sleep(1)
        
        return kills_this_phase

        
    def fight_phase_slow(self, attacker, defender): # Function handling combat logic in a fight phase between two units
        
        print("="*20)
        print(f" {attacker.name} hitting {defender.name}! ")    
        print("="*20)
        
        kills_this_phase = 0 # Counts number of kills made per phase
        
        for model in attacker.alive_models(): # Checks number of alive models that are eligble to attack
            weapon = model.weapon
            print()
            print(f"{model.name} attacks with his {weapon.name}! ")
            
            for attack in range(weapon.attacks):
                if defender.is_destroyed(): 
                    return kills_this_phase # Stops attack sequencing if all defender models are destroyed
                hit_roll = self.dice_roll()
                if hit_roll >= weapon.hit:
                    print(f"Hit with a roll of {hit_roll} ")
                    time.sleep(1)
                    wound_needed = self.wound_rules(weapon.strength, defender.alive_models()[0].toughness)
                    wound_roll = self.dice_roll()
                    if wound_roll >= wound_needed:
                        print(f"Wounded with a roll of {wound_roll} ")
                        time.sleep(1)
                        target = defender.alive_models()[0]
                        save_roll = self.dice_roll()
                        modified_save = target.save + weapon.ap
                        if save_roll < modified_save:
                            print(f"Save failed with a roll of {save_roll}, needed a {modified_save}+ ")
                            time.sleep(1)
                            target.current_wounds -= weapon.damage
                            print(f"{target.name} takes {weapon.damage} damage! ")
                            print(f"{target.name} has {target.current_wounds} wounds remaining ")
                            
                            if target.current_wounds <= 0:
                                print(f"A {target.name} is slain! ")
                                kills_this_phase += 1
        
        return kills_this_phase 
                            
    def fight_phase_fast(self, attacker, defender): #todo: Fix printing same name for entire unit
        print("="*20)
        print(f" {attacker.name} hitting {defender.name}! ")
        print("="*20)
        
        attack_pools = defaultdict(int)
        kills_this_phase = 0
        total_hits = 0
        total_wounds = 0
        total_failed_saves = 0

        for model in attacker.alive_models(): 
            attack_pools[model.weapon] += model.weapon.attacks

        print("Attacks: ")
        for weapon, attacks in attack_pools.items():
            print(f"{weapon.name}: {attacks} attacks")
        
        for weapon, attacks in attack_pools.items():
            if defender.is_destroyed():
                break
            
            hits = 0
            for attack in range(attacks):
                if self.dice_roll() >= weapon.hit:
                    hits += 1

            total_hits += hits
            if hits == 0:
                continue

            target = defender.alive_models()[0]
            wound_needed = self.wound_rules(weapon.strength, target.toughness)

            wounds = 0
            for hit in range(hits):
                if self.dice_roll() >= wound_needed:
                    wounds += 1

            total_wounds += wounds
            if wounds == 0:
                continue

            failed_saves = 0
            for wound in range(wounds):
                save_roll = self.dice_roll()
                modified_save = target.save + weapon.ap # The actual save of a model, save - the armor piercing value. eg 3+ save with 1 ap becomes 4+
                if target.invul_save is not None: # Checks if the target has an invulnerable save
                    save_needed = min(modified_save, target.invul_save) # Uses the lowest, e.g best save option. Either armor or invulnerable save
                else:
                    save_needed = modified_save
                if save_roll < save_needed:
                    failed_saves += 1

            total_failed_saves += failed_saves

            for save in range(failed_saves):
                if defender.is_destroyed():
                    break

                target = defender.alive_models()[0]
                target.current_wounds -= weapon.damage

                if target.current_wounds <= 0:
                    kills_this_phase += 1
                    
        print()
        print(f"Total hits: {total_hits}")
        time.sleep(1)
        print(f"Total wounds: {total_wounds}")
        time.sleep(1)
        print(f"Unsaved wounds: {total_failed_saves}")
        time.sleep(1)
        print(f"Models slain: {kills_this_phase}")

        return kills_this_phase      