from UI.ui import UI
from service.service import Service

service = Service()
ui = UI(service)

ui.run()