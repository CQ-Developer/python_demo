class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This cat has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, mileage):
        self.odometer_reading += mileage

    def fill_gas_tank(self):
        print("This car need 70L gas")


my_cat = Car("audi", "a4", 2003)
print(my_cat.get_descriptive_name())
print(my_cat.odometer_reading)
my_cat.increment_odometer(3000)
print(my_cat.odometer_reading)
