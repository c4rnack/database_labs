from typing import List, Dict, Any

from lab4.app.project.auth.service import employee_service
from lab4.app.project.auth.controller.general_controller import GeneralController


class EmployeeController(GeneralController):
    _service = employee_service

    def get_employee_after_shop(self, shop_id: int) -> List[object]:
        return self._service.get_employee_after_shop(shop_id)

    def get_employee_after_employee_position(self, position_id: int) -> List[object]:
        return self._service.get_employee_after_employee_position(position_id)