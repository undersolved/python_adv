"""
Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it
"""


class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand

    def fullname(self):
        return f"The car is {self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize


my_car = ElectricCar("Tesla", "Model S", "80kWH")

# print(my_car.__brand)
print(my_car.get_brand())
