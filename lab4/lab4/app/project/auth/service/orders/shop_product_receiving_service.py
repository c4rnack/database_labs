from typing import List, Dict, Any

from lab4.app.project.auth.dao import shop_product_receiving_dao
from lab4.app.project.auth.service.general_service import GeneralService


class ShopProductReceivingService(GeneralService):

    _dao = shop_product_receiving_dao

    def get_shop_product_receiving_after_shop(self, shop_id: int) -> List[object]:
        return self._dao.get_shop_product_receiving_after_shop(shop_id)

    def get_shop_product_receiving_after_product(self, product_id: int) -> List[object]:
        return self._dao.get_shop_product_receiving_after_product(product_id)