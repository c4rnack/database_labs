from typing import List, Dict, Any

import sqlalchemy

from lab4.app.project.auth.dao.general_dao import GeneralDAO
from lab4.app.project.auth.domain import Product


class ProductDAO(GeneralDAO):
    _domain_type = Product

    def get_product_after_manufacturing_company(self, manufacturing_company_id: int) -> List[object]:
        result = self._session.execute(sqlalchemy.text("CALL get_product_after_manufacturing_company(:manufacturing_company_id)"),
                                       {'manufacturing_company_id': manufacturing_company_id}).mappings().all()
        return [dict(row) for row in result]

    def get_product_after_category(self, category_id: int) -> List[object]:
        result = self._session.execute(sqlalchemy.text("CALL get_product_after_category(:category_id)"),
                                       {'category_id': category_id}).mappings().all()
        return [dict(row) for row in result]