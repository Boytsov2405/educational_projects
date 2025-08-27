class Dessert:
    HEALTHY_CALORIES_LIMIT = 200
    def __init__(self,_name:str = "", _calories:int = 0):
        self.name:str = _name;
        self.calories:int = _calories;
    @property
    def calories(self):
        return self._calories
    @calories.setter
    def calories(self, _val):
        if(isinstance(_val, int)):
            self._calories = _val
        else:
            raise TypeError("Calories must be an int")
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, _val:str):
        if(isinstance(_val, str)):
            self._name = _val
        else:
            raise TypeError("name must be a srt")
    
    def is_healthy(self):
        return self.calories < self.HEALTHY_CALORIES_LIMIT
    def is_delicious(self):
        return True

cupcake = Dessert("cupcake", 150)
print(f"{cupcake.name} is healty: {cupcake.is_healthy()}")
print(f"{cupcake.name} is delicious: {cupcake.is_delicious()}")

puncake = Dessert("puncake", 500)
print(f"{puncake.name} is healty: {puncake.is_healthy()}")
print(f"{puncake.name} is delicious: {puncake.is_delicious()}")



try:
    muffin = Dessert(120, "muffin")
    print(cupcake.is_healthy())
    print(cupcake.is_delicious())
except TypeError as _error:
    print(f"Don't work. Wrong Types: {_error}. Sad, but true.")
except Exception as _error:
    print(f"Error: {_error}")