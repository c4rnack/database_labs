from lab4.app.project.auth.service import employee_position_service
from lab4.app.project.auth.controller.general_controller import GeneralController


class EmployeePositionController(GeneralController):
    _service = employee_position_service