from lab4.app.project.auth.dao.general_dao import GeneralDAO
from lab4.app.project.auth.domain import ManufacturingCompany


class ManufacturingCompanyDAO(GeneralDAO):
    _domain_type = ManufacturingCompany