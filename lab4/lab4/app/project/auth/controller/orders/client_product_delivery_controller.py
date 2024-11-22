from typing import List, Dict, Any

from lab4.app.project.auth.service import client_product_delivery_service
from lab4.app.project.auth.controller.general_controller import GeneralController


class ClientProductDeliveryController(GeneralController):
    _service = client_product_delivery_service

    def get_client_product_delivery_after_product(self, product_id) -> List[object]:
        return self._service.get_client_product_delivery_after_product(product_id)

    def get_client_product_delivery_after_shop(self, shop_id) -> List[object]:
        return self._service.get_client_product_delivery_after_shop(shop_id)

    def get_client_product_delivery_after_client(self, client_id) -> List[object]:
        return self._service.get_client_product_delivery_after_client(client_id)

    def get_client_product_delivery_after_delivery_type(self, delivery_type_id) -> List[object]:
        return self._service.get_client_product_delivery_after_delivery_type(delivery_type_id)
