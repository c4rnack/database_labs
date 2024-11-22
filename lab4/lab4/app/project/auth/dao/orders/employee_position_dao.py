from lab4.app.project.auth.dao.general_dao import GeneralDAO
from lab4.app.project.auth.domain import EmployeePosition


class EmployeePositionDAO(GeneralDAO):
    _domain_type = EmployeePosition