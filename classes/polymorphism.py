"""
Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviours
"""


class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand

    def fullname(self):
        return f"The car is {self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Deisel"


class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def fuel_type(self):
        return "Electric Charge"


my_car = ElectricCar("Tesla", "Model S", "80kWH")
print(my_car.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())
