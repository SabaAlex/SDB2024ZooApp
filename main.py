from UI.ui import UI
from domain.animal import Animal
from domain.caretaker import Caretaker
from repository.repository import Repository
from service.animal_service import AnimalService
from service.caretaker_service import CaretakerService
from service.statistics_service import StatisticsService

animal_repository = Repository([Animal('Rex', 2), Animal('Luna', 5)])
caretaker_repository = Repository([Caretaker('Raul', 55, 'Rex')])

animal_service = AnimalService(animal_repository)
caretaker_service = CaretakerService(caretaker_repository)
statistics_service = StatisticsService(animal_repository, caretaker_repository)

ui = UI(animal_service, caretaker_service, statistics_service)

ui.run()