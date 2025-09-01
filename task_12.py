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
        
class JellyBean(Dessert):
    def __init__(self,_name = "", _calories = 0, _flavor = ""):
        super().__init__(_name, _calories,)
        self.flavor = _flavor
    @property
    def flavor(self):
        return self._flavor
    @flavor.setter
    def flavor(self, _val):
        self._flavor = _val
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


#----------------
cupcake = Dessert("cupcake", "ffff")
print(f"{cupcake.name} is healty: {cupcake.is_healthy()}")
print(f"{cupcake.name} is delicious: {cupcake.is_delicious()}")

puncake = Dessert(12, 500)
print(f"{puncake.name} is healty: {puncake.is_healthy()}")
print(f"{puncake.name} is delicious: {puncake.is_delicious()}")

jelly_bean = JellyBean(41414141414141, 150, "black licorice")

print(f"{jelly_bean.name} with {jelly_bean.flavor} flavor is healty: {jelly_bean.is_healthy()}")
print(f"{jelly_bean.name} with {jelly_bean.flavor} flavor is delicious: {jelly_bean.is_delicious()}")

jelly_bean2 = JellyBean("JellyBean", 500, 444)

print(f"{jelly_bean2.name} with {jelly_bean2.flavor} flavor  is healty: {jelly_bean2.is_healthy()}")
print(f"{jelly_bean2.name} with {jelly_bean2.flavor} flavor  is delicious: {jelly_bean2.is_delicious()}")

print("-----------------------------------------")
dessert = JellyBean()
if not issubclass(dessert.__class__, JellyBean): raise Exception("Invalid inheritance")
dessert.name = "test_name"
print(dessert.name)
dessert.name = "test_name2"
print(dessert.name)
if dessert.name != "test_name2": raise Exception("Setter for name is not working")
dessert.calories = "test_calories"
if dessert.calories != "test_calories": raise Exception("Setter for flavor is not working")
dessert.flavor = 42
if dessert.flavor != 42: raise Exception("Setter for flavor is not working")

jelly_bean2.flavor = [1,2,0]
print(jelly_bean2.flavor)
if jelly_bean2.flavor != [1,2,0]: raise Exception("Setter for flavor is not working")