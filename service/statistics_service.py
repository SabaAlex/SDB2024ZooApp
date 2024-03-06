from domain.animal import Animal
from repository.repository import Repository


class StatisticsService:
    def __init__(self, animal_repository: Repository, caretaker_repository: Repository):
        self.__animal_repository = animal_repository
        self.__caretaker_repository = caretaker_repository

    def __has_caretaker(self, animal: Animal):
        caretaker_list = self.__caretaker_repository.get_all()
        for caretaker in caretaker_list:
            if caretaker.get_animal_name() == animal.get_name():
                return True
        return False

    def get_animals_without_caretaker(self):
        animal_list = self.__animal_repository.get_all()
        no_caretaker_list = []
        for animal in animal_list:
            if not self.__has_caretaker(animal):
                no_caretaker_list.append(animal)
        return no_caretaker_list
