from lab4.app.project.auth.dao.general_dao import GeneralDAO
from lab4.app.project.auth.domain import DeliveryType


class DeliveryTypeDAO(GeneralDAO):
    _domain_type = DeliveryType