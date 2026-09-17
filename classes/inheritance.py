class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"The car is {self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize


bittu_car = ElectricCar("Tesla", "Model S", "90KwH")

print(bittu_car.brand, bittu_car.model, bittu_car.batterySize, bittu_car.fullname())
