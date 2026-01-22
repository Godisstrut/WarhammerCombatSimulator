class Unit():
    
    def __init__(self, name: str, models: int):
        
        self.name = name
        self.models = models
    
    def alive_models(self): # Checks and returns a list of alive models
        alive = []
        for model in self.models:
            if model.is_alive():
                alive.append(model)
        return alive
    
    def __str__(self):
        return f"Unit: {self.name} has {self.models} models "