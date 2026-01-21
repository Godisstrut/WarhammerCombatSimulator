class Model():
    def __init__(self, name: str, wounds: int, save: int, weapon):
        
        self.name = name
        self.max_wounds = wounds
        self.current_wounds = wounds
        self.save = save
        self.weapon = weapon
        
    def is_alive(self):
        return self.current_wounds > 0