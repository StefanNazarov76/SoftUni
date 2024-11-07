from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species: str) -> None:
        self.species = species

    def get_species(self) -> str:
        return self.species

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self) -> str:
        return 'woof-woof'


class Cat(Animal):
    def make_sound(self) -> str:
        return 'meow'


class Chicken(Animal):
    def make_sound(self) -> str:
        return 'cluck'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog('mammal'), Cat('mammal'), Chicken('mammal')]
animal_sound(animals)
