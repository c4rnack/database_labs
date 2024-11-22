from typing import List, Dict, Any

from lab4.app.project.auth.dao import client_product_delivery_dao
from lab4.app.project.auth.service.general_service import GeneralService


class ClientProductDeliveryService(GeneralService):

    _dao = client_product_delivery_dao

    def get_client_product_delivery_after_product(self, product_id) -> List[object]:
        return self._dao.get_client_product_delivery_after_product(product_id)

    def get_client_product_delivery_after_shop(self, shop_id) -> List[object]:
        return self._dao.get_client_product_delivery_after_shop(shop_id)

    def get_client_product_delivery_after_client(self, client_id) -> List[object]:
        return self._dao.get_client_product_delivery_after_client(client_id)

    def get_client_product_delivery_after_delivery_type(self, delivery_type_id) -> List[object]:
        return self._dao.get_client_product_delivery_after_delivery_type(delivery_type_id)