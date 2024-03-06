from UI.ui import UI
from domain.animal import Animal
from repository.repository import Repository
from service.animal_service import AnimalService

animal_repository = Repository([Animal('Rex', 2), Animal('Luna', 5)])
animal_service = AnimalService(animal_repository)
ui = UI(animal_service)

ui.run()