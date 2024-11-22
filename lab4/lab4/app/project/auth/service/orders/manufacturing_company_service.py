from lab4.app.project.auth.dao import manufacturing_company_dao
from lab4.app.project.auth.service.general_service import GeneralService


class ManufacturingCompanyService(GeneralService):

    _dao = manufacturing_company_dao