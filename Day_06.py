class Car:
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.model = usermodel

    def name(self):
        print(f"Brand: {self.__brand} \nModel: {self.model}")

# encapsulation
    def get_brand(self):
        return self.__brand

# polymorphism
    def fuel_type(self):
        print("diesal")

# inheritence
class ElectricCar(Car):
    def __init__(self, userbrand, usermodel, batterysize):
        super().__init__(userbrand, usermodel)
        self.Batter_size = batterysize

# polymorphism
    def fuel_type(self):
        print("electric charge")



# making object
tesla = Car("carolla", "2018")
tesla.fuel_type()
# print(tesla.get_brand())

electricCar = ElectricCar("tesla", "s model", "85khw")
electricCar.fuel_type()
# print(electricCar.Batter_size)
# print(electricCar.brand)
# print(electricCar.model)




