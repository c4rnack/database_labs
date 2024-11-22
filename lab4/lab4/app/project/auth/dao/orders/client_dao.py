from lab4.app.project.auth.dao.general_dao import GeneralDAO
from lab4.app.project.auth.domain import Client


class ClientDAO(GeneralDAO):
    _domain_type = Client