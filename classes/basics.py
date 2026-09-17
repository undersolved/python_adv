class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


bittu_car = Car("Honda", "Br-V", 2017)


print(bittu_car.brand, bittu_car.model, bittu_car.year)
