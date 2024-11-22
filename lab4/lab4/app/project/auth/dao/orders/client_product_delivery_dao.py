from typing import List, Dict, Any

import sqlalchemy

from lab4.app.project.auth.dao.general_dao import GeneralDAO
from lab4.app.project.auth.domain import ClientProductDelivery


class ClientProductDeliveryDAO(GeneralDAO):
    _domain_type = ClientProductDelivery

    def get_client_product_delivery_after_product(self, product_id: int) -> List[object]:
        result = self._session.execute(sqlalchemy.text("CALL get_client_product_delivery_after_product(:product_id)"),
                                       {'product_id': product_id}).mappings().all()
        return [dict(row) for row in result]

    def get_client_product_delivery_after_shop(self, shop_id: int) -> List[object]:
        result = self._session.execute(sqlalchemy.text("CALL get_client_product_delivery_after_shop(:shop_id)"),
                                       {'shop_id': shop_id}).mappings().all()
        return [dict(row) for row in result]

    def get_client_product_delivery_after_client(self, client_id: int) -> List[object]:
        result = self._session.execute(sqlalchemy.text("CALL get_client_product_delivery_after_client(:client_id)"),
                                       {'client_id': client_id}).mappings().all()
        return [dict(row) for row in result]

    def get_client_product_delivery_after_delivery_type(self, delivery_type_id: int) -> List[object]:
        result = self._session.execute(sqlalchemy.text("CALL get_client_product_delivery_after_delivery_type(:delivery_type_id)"),
                                       {'delivery_type_id': delivery_type_id}).mappings().all()
        return [dict(row) for row in result]