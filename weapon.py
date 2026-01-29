class Weapon(): # Represents a weapon with its respective stats
    def __init__(self, name: str, attacks: int, hit, strength: int, ap: int, damage: int, special_rules = None): # Todo Lägg till lethal/sustained hits etc som vapen kan ha
        
        self.name = name
        self.attacks = attacks
        self.hit = hit
        self.strength = strength
        self.ap = ap
        self.damage = damage
        self.special_rules = special_rules or []
        
    def __str__(self):
        return f"{self.name} Attacks:{self.attacks} Hit:{self.hit}+ Strength:{self.strength} AP:{self.ap} Damage:{self.damage}"