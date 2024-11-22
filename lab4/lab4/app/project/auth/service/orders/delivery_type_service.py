from lab4.app.project.auth.dao import delivery_type_dao
from lab4.app.project.auth.service.general_service import GeneralService


class DeliveryTypeService(GeneralService):

    _dao = delivery_type_dao