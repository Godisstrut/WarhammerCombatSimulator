class Unit(): # Represents a unit composed of multiple models
    
    def __init__(self, name: str, model_factory, models: int):
        
        self.name = name
        self.model_factory = model_factory
        self.models = []
        
        for model in range(models):
            self.models.append(model_factory())
    
    def alive_models(self): # Checks and returns a list of alive models
        alive = []
        for model in self.models:
            if model.is_alive():
                alive.append(model)
        return alive
    
    def is_destroyed(self): # Checks if the unit is destroyed
        return len(self.alive_models()) == 0
    
    def add_model(self, model): # Adds a model to the unit, used for sergeants
        self.models.append(model)

    def __str__(self):
        return f"Unit: {self.name} has {len(self.models)} models "
    
