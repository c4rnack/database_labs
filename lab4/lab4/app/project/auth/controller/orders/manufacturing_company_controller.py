from lab4.app.project.auth.service import manufacturing_company_service
from lab4.app.project.auth.controller.general_controller import GeneralController


class ManufacturingCompanyController(GeneralController):
    _service = manufacturing_company_service