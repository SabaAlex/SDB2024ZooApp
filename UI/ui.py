from domain.animal import Animal
from domain.caretaker import Caretaker
from domain.exceptions import CustomException
from service.animal_service import AnimalService
from service.caretaker_service import CaretakerService
from service.statistics_service import StatisticsService


class UI:
    def __init__(self, animal_service: AnimalService, caretaker_service: CaretakerService, statistics_service: StatisticsService):
        self.__animal_service = animal_service
        self.__caretaker_service = caretaker_service
        self.__statistics_service = statistics_service

        self.__commands = {
            "1": self.__add_animal,
            "2": self.__delete_animal,
            "3": self.__average_animal_age,
            "4": self.__show_all_animals,
            "5": self.__add_caretaker,
            "6": self.__delete_caretaker,
            "7": self.__average_caretaker_age,
            "8": self.__show_all_caretakers,
            "9": self.__show_animals_with_no_caretaker,
      }

    def __print_menu(self):
        print("1.Add animal")
        print("2.Delete animal")
        print("3.Average zoo age")
        print("4.Show all animals")
        print("5.Add caretaker")
        print("6.Delete caretaker")
        print("7.Average caretaker age")
        print("8.Show all caretaker")
        print("9.Animals with no caretaker")
        print("0.Exit")

    def __validate_age(self, age):
        try:
            int(age)
        except ValueError:
            raise CustomException('Animal age is not a number!')

    def __add_animal(self):
        name = input("Animal name: ")
        age = input("Animal age: ")
        self.__validate_age(age)
        self.__animal_service.add_animal(Animal(name, int(age)))
        print('Animal added!')

    def __delete_animal(self):
        name = input("Animal to delete name: ")
        age = input("Animal to delete age: ")
        self.__validate_age(age)
        self.__animal_service.delete_animal(Animal(name, int(age)))
        print('Animal deleted!')

    def __show_all_animals(self):
        for animal in self.__animal_service.get_all_animals():
            print(animal)

    def __average_animal_age(self):
        average_age = round(self.__animal_service.average_age(), 2)
        print(f'The average age of all the animals is {average_age}')

    def __add_caretaker(self):
        name = input("Caretaker name: ")
        age = input("Caretaker age: ")
        animal_name = input("Caretaker's animal name: ")
        self.__validate_age(age)
        self.__caretaker_service.add_caretaker(Caretaker(name, int(age), animal_name))
        print('Caretaker added!')
        
    def __delete_caretaker(self):
        name = input("Caretaker to delete name: ")
        age = input("Caretaker to delete age: ")
        animal_name = input("Caretaker's animal name: ")
        self.__validate_age(age)
        self.__caretaker_service.delete_caretaker(Caretaker(name, int(age), animal_name))
        print('Caretaker deleted!')

    def __show_all_caretakers(self):
        for caretaker in self.__caretaker_service.get_all_caretakers():
            print(caretaker)

    def __average_caretaker_age(self):
        average_age = round(self.__caretaker_service.average_age(), 2)
        print(f'The average age of all the caretakers is {average_age}')

    def __show_animals_with_no_caretaker(self):
        animals = self.__statistics_service.get_animals_without_caretaker()
        if len(animals) == 0:
            print('No animals without caretakers!')
            return
        for animal in self.__statistics_service.get_animals_without_caretaker():
            print(animal)

    def run(self):
        print("App started")
        while True:
            self.__print_menu()
            try:
                command = input("Choose the command:").strip()
                # actions[command]()
                if command == "0":
                    return
                if command in self.__commands:
                    self.__commands[command]()
                else:
                    print('Command does not exist.')
            except CustomException as error:
                print(error)
