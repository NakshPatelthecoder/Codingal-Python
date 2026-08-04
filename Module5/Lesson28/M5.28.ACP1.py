class Vehicle:
    # Class variable
    vehicle_count = 0

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        Vehicle.vehicle_count += 1

    def start(self):
        print(f"The {self.brand} vehicle is starting.")

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, year, model, colour):
        super().__init__(brand, year)
        self.model = model
        self.colour = colour

    # Override the parent method
    def start(self):
        print(f"The {self.brand} {self.model} starts with a push-button ignition.")

    def display_info(self):
        super().display_info()
        print(f"Model: {self.model}")
        print(f"Colour: {self.colour}")

    def drive(self):
        print(f"The {self.colour} {self.model} is now driving.")


# Create an object
my_car = Car("Toyota", 2024, "Corolla", "Blue")

print("Vehicle Information")
print("-" * 25)
my_car.display_info()

print("\nStarting the vehicle:")
my_car.start()

print("\nDriving:")
my_car.drive()

print("\nInheritance Check")
print("Is Car a subclass of Vehicle?", issubclass(Car, Vehicle))

print("\nTotal Vehicles Created:", Vehicle.vehicle_count)