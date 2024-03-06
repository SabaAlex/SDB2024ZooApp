from domain.caretaker import Caretaker
from repository.repository import Repository


class CaretakerService:
    def __init__(self, repository: Repository):
        self.__repository = repository

    def add_caretaker(self, new_caretaker: Caretaker):
        """
        This adds a caretaker to the caretaker list
        :param new_caretaker: the caretaker to be added (Caretaker)
        """
        self.__repository.add(new_caretaker)

    def delete_caretaker(self, caretaker_to_delete):
        """
        Deletes an caretaker from the caretaker list
        :param caretaker_to_delete: Caretaker to delete from in the list (Caretaker)
        """
        self.__repository.delete(caretaker_to_delete)


    def get_all_caretakers(self):
        """
        Returns the list containing all the caretakers
        :return: The list of all the caretakers (list)
        """
        return self.__repository.get_all()

    def average_age(self):
        """
        Returns the average of all the caretakers in the list
        :return: The average age of all the caretakers (float)
        """
        sum = 0
        for caretaker in self.__repository.get_all():
            sum += caretaker.get_age()
        average_age = sum / len(self.__repository.get_all())
        return average_age

