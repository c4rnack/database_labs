from lab4.app.project.auth.service import delivery_type_service
from lab4.app.project.auth.controller.general_controller import GeneralController


class DeliveryTypeController(GeneralController):
    _service = delivery_type_service