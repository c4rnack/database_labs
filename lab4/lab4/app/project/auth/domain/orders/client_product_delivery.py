from __future__ import annotations
from typing import Dict, Any

from lab4.app.project import db
from lab4.app.project.auth.domain.i_dto import IDto

class ClientProductDelivery(db.Model, IDto):
    __tablename__ = "client_product_delivery"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)

    client_id = db.Column(db.Integer,db.ForeignKey('client.id'), nullable=False)
    client = db.relationship("Client", backref="client_product_delivery")

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref='client_product_delivery')

    delivery_type_id = db.Column(db.Integer, db.ForeignKey('delivery_type.id'), nullable=False)
    delivery_type = db.relationship('DeliveryType', backref='client_product_delivery')

    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    shop = db.relationship('Shop', backref='client_product_delivery')

    city = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(50), nullable=False)
    house_number = db.Column(db.Integer, nullable=False)

    date = db.Column(db.Date, nullable=False)

    def __repr__(self) -> str:
        return (f"Client product delivery({self.id}, '{self.client_id}', '{self.product_id}', '{self.delivery_type_id}'"
                f", '{self.shop_id}', {self.city}, {self.street}, {self.house_number}, {self.date})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "client_surname": self.client.surname,
            "product_name": self.product.name,
            "delivery_type": self.delivery_type.name,
            "shop_id": self.shop_id,
            "city": self.city,
            "street": self.street,
            "house_number": self.house_number,
            "date": self.date,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ClientProductDelivery:
        obj = ClientProductDelivery(**dto_dict)
        return obj