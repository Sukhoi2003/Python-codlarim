class Car:
    def __init__(self, cars) -> None:
        self.cars = cars

    def brand_exist(self, brand):
        if brand in self.cars:
            return True 
        else:
            return False


cars = ["Nexiya", "Damas", "Mers"]

c = Car(cars)
print(c.brand_exist("Damas"))