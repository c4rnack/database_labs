from __future__ import annotations
from typing import Dict, Any

from lab4.app.project import db
from lab4.app.project.auth.domain.i_dto import IDto

class ShopProductReceiving(db.Model, IDto):
    __tablename__ = "shop_product_receiving"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref='receiving')
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    shop = db.relationship('Shop', backref='receiving')
    date = db.Column(db.Date, nullable=False)

    def __repr__(self) -> str:
        return f"Shop product receiving ({self.id}, '{self.product}', {self.shop_id}, '{self.date}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "product_name": self.product.name,
            "shop_id": self.shop_id,
            "date": self.date,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ShopProductReceiving:
        obj = ShopProductReceiving(**dto_dict)
        return obj