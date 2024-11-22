from typing import List, Dict, Any

from lab4.app.project.auth.service import product_service
from lab4.app.project.auth.controller.general_controller import GeneralController


class ProductController(GeneralController):
    _service = product_service

    def get_product_after_manufacturing_company(self, manufacturing_company_id: int) -> List[object]:
        return self._service.get_product_after_manufacturing_company(manufacturing_company_id)

    def get_product_after_category(self, category_id: int) -> List[object]:
        return self._service.get_product_after_category(category_id)