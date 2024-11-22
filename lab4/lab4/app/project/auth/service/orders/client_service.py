from lab4.app.project.auth.dao import client_dao
from lab4.app.project.auth.service.general_service import GeneralService


class ClientService(GeneralService):

    _dao = client_dao