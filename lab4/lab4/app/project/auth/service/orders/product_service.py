from typing import List, Dict, Any

from lab4.app.project.auth.dao import product_dao
from lab4.app.project.auth.domain.orders.product import Product
from lab4.app.project.auth.service.general_service import GeneralService


class ProductService(GeneralService):

    _dao = product_dao

    def get_product_after_manufacturing_company(self, manufacturing_company_id: int) -> List[object]:
        return self._dao.get_product_after_manufacturing_company(manufacturing_company_id)

    def get_product_after_category(self, category_id: int) -> List[object]:
        return self._dao.get_product_after_category(category_id)