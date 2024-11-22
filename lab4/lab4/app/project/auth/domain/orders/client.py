from __future__ import annotations
from typing import Dict, Any

from lab4.app.project import db
from lab4.app.project.auth.domain.i_dto import IDto

class Client(db.Model, IDto):
    __tablename__ = "client"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(13), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"Client({self.id}, {self.name} {self.surname}, {self.phone_number}, {self.email})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "phone_number": self.phone_number,
            "email": self.email,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Client:
        obj = Client(**dto_dict)
        return obj