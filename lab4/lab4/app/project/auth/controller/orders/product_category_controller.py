from lab4.app.project.auth.service import product_category_service
from lab4.app.project.auth.controller.general_controller import GeneralController


class ProductCategoryController(GeneralController):
    _service = product_category_service