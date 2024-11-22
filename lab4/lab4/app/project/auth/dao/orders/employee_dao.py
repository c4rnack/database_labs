from typing import List, Dict, Any

import sqlalchemy

from lab4.app.project.auth.dao.general_dao import GeneralDAO
from lab4.app.project.auth.domain import Employee


class EmployeeDAO(GeneralDAO):
    _domain_type = Employee

    def get_employee_after_shop(self, shop_id: int) -> List[object]:
        result = self._session.execute(sqlalchemy.text("CALL get_employee_after_shop(:shop_id)"),
                                       {'shop_id': shop_id}).mappings().all()
        return [dict(row) for row in result]

    def get_employee_after_employee_position(self, position_id: int) -> List[object]:
        result = self._session.execute(sqlalchemy.text("CALL get_employee_after_employee_position(:position_id)"),
                                       {'position_id': position_id}).mappings().all()
        return [dict(row) for row in result]