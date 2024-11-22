from __future__ import annotations
from typing import Dict, Any

from lab4.app.project import db
from lab4.app.project.auth.domain.i_dto import IDto

class Product(db.Model, IDto):
    __tablename__ = "product"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price_UAH = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    shelf_time_WEEKS = db.Column(db.Float, nullable=False)
    product_category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'), nullable=False)
    product_category = db.relationship("ProductCategory", backref="product")
    manufacturing_company_id = db.Column(db.Integer, db.ForeignKey('manufacturing_company.id'), nullable=False)
    manufacturing_company = db.relationship("ManufacturingCompany", backref="product")

    def __repr__(self) -> str:
        return f"Delivery type({self.id}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "price_UAH": self.price_UAH,
            "description": self.description,
            "shelf_time_WEEKS": self.shelf_time_WEEKS,
            "product_category_name": self.product_category.name,
            "manufacturing_company_name": self.manufacturing_company.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Product:
        obj = Product(**dto_dict)
        return obj