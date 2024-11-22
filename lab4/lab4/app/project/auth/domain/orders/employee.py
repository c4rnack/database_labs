from __future__ import annotations
from typing import Dict, Any

from lab4.app.project import db
from lab4.app.project.auth.domain.i_dto import IDto


class Employee(db.Model, IDto):
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    phone_number = db.Column(db.String(13), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('employee_position.id'), nullable=False)
    position = db.relationship("EmployeePosition", backref="employees")
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    shop = db.relationship("Shop", backref="employees")
    def __repr__(self) -> str:
        return f"Employee({self.id}, {self.name} {self.surname},{self.phone_number} ,'{self.position_id}', '{self.shop_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "phone_number": self.phone_number,
            "position_name": self.position.name,
            "shop_id": self.shop.id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Employee:
        obj = Employee(**dto_dict)
        return obj