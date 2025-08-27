class Dessert:
    HEALTHY_CALORIES_LIMIT = 200
    def __init__(self,_name:str = "", _calories:int = 0):
        self.name = _name;
        self.calories = _calories;
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
    def name(self, _val):
        if(isinstance(_val, str)):
            self._name = _val
        else:
            raise TypeError("name must be a srt")
    def is_healthy(self):
        return self.calories < self.HEALTHY_CALORIES_LIMIT
    def is_delicious(self):
        return True
        
class JellyBean(Dessert):
    def __init__(self,_name:str = "", _calories:int = 0, _flavor:str = ""):
        super().__init__(_name, _calories,)
        self.flavor = _flavor
    @property
    def flavor(self):
        return self._flavor
    @flavor.setter
    def flavor(self, _val):
        if(isinstance(_val, str)):
            self._flavor = _val
        else:
            raise TypeError("flavor must be a srt")
    def is_delicious(self):
        if (self._flavor == "black licorice"):
            return False
        return super().is_delicious()








cupcake = Dessert("cupcake", 150)
print(f"{cupcake.name} is healty: {cupcake.is_healthy()}")
print(f"{cupcake.name} is delicious: {cupcake.is_delicious()}")

puncake = Dessert("puncake", 500)
print(f"{puncake.name} is healty: {puncake.is_healthy()}")
print(f"{puncake.name} is delicious: {puncake.is_delicious()}")

jelly_bean = JellyBean("JellyBean", 150, "black licorice")

print(f"{jelly_bean.name} with {jelly_bean.flavor} flavor is healty: {jelly_bean.is_healthy()}")
print(f"{jelly_bean.name} with {jelly_bean.flavor} flavor is delicious: {jelly_bean.is_delicious()}")

jelly_bean2 = JellyBean("JellyBean", 500, "ddd")

print(f"{jelly_bean2.name} with {jelly_bean2.flavor} flavor  is healty: {jelly_bean2.is_healthy()}")
print(f"{jelly_bean2.name} with {jelly_bean2.flavor} flavor  is delicious: {jelly_bean2.is_delicious()}")

try:
    jelly_bean2.flavor = [1,2,0]
except TypeError as _error:
    print(f"Don't work. Wrong Types: {_error}. Sad, but true.")
except Exception as _error:
    print(f"Error: {_error}")