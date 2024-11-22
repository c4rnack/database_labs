from typing import List, Dict, Any

from lab4.app.project.auth.dao import employee_dao
from lab4.app.project.auth.service.general_service import GeneralService


class EmployeeService(GeneralService):

    _dao = employee_dao

    def get_employee_after_shop(self, shop_id: int) -> List[object]:
        return self._dao.get_employee_after_shop(shop_id)

    def get_employee_after_employee_position(self, position_id: int) -> List[object]:
        return self._dao.get_employee_after_employee_position(position_id)