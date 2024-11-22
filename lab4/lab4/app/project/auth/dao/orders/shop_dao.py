from lab4.app.project.auth.dao.general_dao import GeneralDAO
from lab4.app.project.auth.domain import Shop


class ShopDAO(GeneralDAO):
    _domain_type = Shop