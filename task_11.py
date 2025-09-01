class Dessert:
    HEALTHY_CALORIES_LIMIT = 200
    def __init__(self,_name = "", _calories = 0):
        self.name = _name;
        self.calories = _calories;
    @property
    def calories(self):
        return self._calories
    @calories.setter
    def calories(self, _val):
        self._calories = _val
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, _val):
        self._name = _val
    
    def is_healthy(self):
        if(isinstance(self.calories, (int,float))):
            return self.calories < self.HEALTHY_CALORIES_LIMIT
        return False
        
    def is_delicious(self):
        return True

cupcake = Dessert("cupcake", 150)
print(f"{cupcake.name} is healty: {cupcake.is_healthy()}")
print(f"{cupcake.name} is delicious: {cupcake.is_delicious()}")

puncake = Dessert("puncake", 500)
print(f"{puncake.name} is healty: {puncake.is_healthy()}")
print(f"{puncake.name} is delicious: {puncake.is_delicious()}")


#----------------
cupcake = Dessert("cupcake", "ffff")
print(f"{cupcake.name} is healty: {cupcake.is_healthy()}")
print(f"{cupcake.name} is delicious: {cupcake.is_delicious()}")

puncake = Dessert(12, 500)
print(f"{puncake.name} is healty: {puncake.is_healthy()}")
print(f"{puncake.name} is delicious: {puncake.is_delicious()}")

print("-----------------------------------------")
dessert = Dessert()
dessert.name = "test_name"
print(dessert.name)
dessert.name = "test_name2"
print(dessert.name)
if dessert.name != "test_name2": raise Exception("Setter for name is not working")
dessert.calories = "test_calories"
if dessert.calories != "test_calories": raise Exception("Setter for calories is not working")
print(dessert.name, " ", dessert.calories)