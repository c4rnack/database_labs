from typing import List, Dict, Any

from lab4.app.project.auth.service import shop_product_receiving_service
from lab4.app.project.auth.controller.general_controller import GeneralController


class ShopProductReceivingController(GeneralController):
    _service = shop_product_receiving_service

    def get_shop_product_receiving_after_shop(self, shop_id: int) -> List[object]:
        return self._service.get_shop_product_receiving_after_shop(shop_id)

    def get_shop_product_receiving_after_product(self, product_id: int) -> List[object]:
        return self._service.get_shop_product_receiving_after_product(product_id)