from __future__ import annotations
from typing import Dict, Any

from lab4.app.project import db
from lab4.app.project.auth.domain.i_dto import IDto

class ProductCategory(db.Model, IDto):
    __tablename__ = "product_category"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"Product category({self.id}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ProductCategory:
        obj = ProductCategory(**dto_dict)
        return obj