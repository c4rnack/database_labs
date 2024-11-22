from lab4.app.project.auth.dao.general_dao import GeneralDAO
from lab4.app.project.auth.domain import ProductCategory


class ProductCategoryDAO(GeneralDAO):
    _domain_type = ProductCategory