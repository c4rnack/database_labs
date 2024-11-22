from lab4.app.project.auth.dao import shop_dao
from lab4.app.project.auth.service.general_service import GeneralService


class ShopService(GeneralService):

    _dao = shop_dao