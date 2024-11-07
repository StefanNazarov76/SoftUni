from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: int) -> None:
        pass


class Car(Vehicle):
    air_conditioner_consumption = 0.9

    def drive(self, distance: int) -> None:
        consumption = (self.fuel_consumption + self.air_conditioner_consumption) * distance

        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    air_conditioner_consumption = 1.6

    def drive(self, distance: int) -> None:
        consumption = (self.fuel_consumption + self.air_conditioner_consumption) * distance

        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
