from lab4.app.project.auth.dao import product_category_dao
from lab4.app.project.auth.service.general_service import GeneralService


class ProductCategoryService(GeneralService):

    _dao = product_category_dao