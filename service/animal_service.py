from domain.animal import Animal
from repository.repository import Repository


class AnimalService:
    def __init__(self, repository: Repository):
        self.__repository = repository

    def add_animal(self, new_animal: Animal):
        """
        This adds an animal to the animal list
        :param new_animal: the animal to be added (Animal)
        """
        self.__repository.add(new_animal)

    def delete_animal(self, animal_to_delete):
        """
        Deletes an animal from the animal list
        :param animal_to_delete: Animal to delete from in the list (Animal)
        """
        self.__repository.delete(animal_to_delete)


    def get_all_animals(self):
        """
        Returns the list containing all the animals
        :return: The list of all the animals (list)
        """
        return self.__repository.get_all()

    def average_age(self):
        """
        Returns the average of all the animals in the list
        :return: The average age of all the animals (float)
        """
        sum = 0
        for animal in self.__repository.get_all():
            sum += animal.get_age()
        average_age = sum / len(self.__repository.get_all())
        return average_age
