from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return f'Not enough budget'

        return f'Not enough space for animal'

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'

        return f'Not enough space for worker'

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
            self.workers.remove(worker)
            return f'{worker_name} fired successfully'
        except StopIteration:
            return f'There is no {worker_name} in the zoo'

    def pay_workers(self) -> str:
        money_to_pay = sum([w.salary for w in self.workers])

        if self.__budget >= money_to_pay:
            self.__budget -= money_to_pay
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self) -> str:
        money_needed = sum([a.money_for_care for a in self.animals])

        if self.__budget >= money_needed:
            self.__budget -= money_needed
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        lions_info = '\n'.join(lion.__repr__() for lion in lions)

        tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        tigers_info = '\n'.join(tiger.__repr__() for tiger in tigers)

        cheetahs = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']
        cheetahs_info = '\n'.join(cheetah.__repr__() for cheetah in cheetahs)

        return f'You have {len(self.animals)} animals\n'\
               f'----- {len(lions)} Lions:\n'\
               f'{lions_info}\n'\
               f'----- {len(tigers)} Tigers:\n'\
               f'{tigers_info}\n'\
               f'----- {len(cheetahs)} Cheetahs:\n'\
               f'{cheetahs_info}'

    def workers_status(self) -> str:
        keepers = [w for w in self.workers if w.__class__.__name__ == 'Keeper']
        keepers_info = '\n'.join(k.__repr__() for k in keepers)

        caretakers = [w for w in self.workers if w.__class__.__name__ == 'Caretaker']
        caretakers_info = '\n'.join(c.__repr__() for c in caretakers)

        vets = [w for w in self.workers if w.__class__.__name__ == 'Vet']
        vets_info = '\n'.join(v.__repr__() for v in vets)

        return f'You have {len(self.workers)} workers\n'\
               f'----- {len(keepers)} Keepers:\n'\
               f'{keepers_info}\n'\
               f'----- {len(caretakers)} Caretakers:\n'\
               f'{caretakers_info}\n'\
               f'----- {len(vets)} Vets:\n'\
               f'{vets_info}'
