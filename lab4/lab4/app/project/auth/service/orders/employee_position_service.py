from lab4.app.project.auth.dao import employee_position_dao
from lab4.app.project.auth.service.general_service import GeneralService


class EmployeePositionService(GeneralService):

    _dao = employee_position_dao