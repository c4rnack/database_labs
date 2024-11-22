from __future__ import annotations
from typing import Dict, Any

from lab4.app.project import db
from lab4.app.project.auth.domain.i_dto import IDto

class ManufacturingCompany(db.Model, IDto):
    __tablename__ = "manufacturing_company"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(50), nullable=False)
    house_number = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Manufacturing company({self.id}, '{self.name}', {self.city}, {self.street}, {self.house_number})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "city": self.city,
            "street": self.street,
            "house_number": self.house_number,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ManufacturingCompany:
        obj = ManufacturingCompany(**dto_dict)
        return obj