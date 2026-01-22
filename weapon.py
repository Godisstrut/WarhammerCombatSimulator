class Weapon(): # Represents a weapon with its respective stats
    def __init__(self, name: str, attacks: int, hit, strength, ap, damage: int):
        
        self.name = name
        self.attacks = attacks
        self.hit = hit
        self.strength = strength
        self.ap = ap
        self.damage = damage
        
    def __str__(self):
        return f"{self.name} Attacks:{self.attacks} Hit:{self.hit}+ Strength:{self.strength} AP:{self.ap} Damage:{self.damage}"