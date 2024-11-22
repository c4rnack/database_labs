from lab4.app.project.auth.service import shop_service
from lab4.app.project.auth.controller.general_controller import GeneralController


class ShopController(GeneralController):
    _service = shop_service