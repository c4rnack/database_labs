from typing import List, Dict, Any

import sqlalchemy

from lab4.app.project.auth.dao.general_dao import GeneralDAO
from lab4.app.project.auth.domain import ShopProductReceiving


class ShopProductReceivingDAO(GeneralDAO):
    _domain_type = ShopProductReceiving

    def get_shop_product_receiving_after_shop(self, shop_id: int) -> List[object]:
        result = self._session.execute(sqlalchemy.text("CALL get_shop_product_receiving_after_shop(:shop_id)"),
                                                       {'shop_id': shop_id}).mappings().all()
        return [dict(row) for row in result]

    def get_shop_product_receiving_after_product(self, product_id: int) -> List[object]:
        result = self._session.execute(sqlalchemy.text("CALL get_shop_product_receiving_after_product(:product_id)"),
                                       {'product_id': product_id}).mappings().all()
        return [dict(row) for row in result]