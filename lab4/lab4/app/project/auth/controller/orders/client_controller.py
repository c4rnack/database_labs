from lab4.app.project.auth.service import client_service
from lab4.app.project.auth.controller.general_controller import GeneralController


class ClientController(GeneralController):
    _service = client_service