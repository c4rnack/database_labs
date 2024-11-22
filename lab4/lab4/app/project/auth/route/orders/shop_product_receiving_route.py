from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import shop_product_receiving_controller
from lab4.app.project.auth.domain import ShopProductReceiving

shop_product_receiving_bp = Blueprint('shop_product_receiving', __name__, url_prefix='/shop_product_receiving')

@shop_product_receiving_bp.get('')
def get_all_shop_product_receiving() -> Response:
    return make_response(jsonify(shop_product_receiving_controller.find_all()), HTTPStatus.OK)

@shop_product_receiving_bp.post('')
def create_shop_product_receiving() -> Response:
    content = request.get_json()
    shop_product_receiving = ShopProductReceiving.create_from_dto(content)
    shop_product_receiving_controller.create(shop_product_receiving)
    return make_response(jsonify(shop_product_receiving.put_into_dto()), HTTPStatus.CREATED)

@shop_product_receiving_bp.get('/<int:shop_product_receiving_id>')
def get_shop_product_receiving(shop_product_receiving_id: int) -> Response:
    return make_response(jsonify(shop_product_receiving_controller.find_by_id(shop_product_receiving_id)), HTTPStatus.OK)

@shop_product_receiving_bp.put('/<int:shop_product_receiving_id>')
def update_shop_product_receiving(shop_product_receiving_id: int) -> Response:
    content = request.get_json()
    shop_product_receiving = ShopProductReceiving.create_from_dto(content)
    shop_product_receiving_controller.update(shop_product_receiving_id, shop_product_receiving)
    return make_response("Shop product receiving updated", HTTPStatus.OK)

@shop_product_receiving_bp.patch('/<int:shop_product_receiving_id>')
def patch_shop_product_receiving(shop_product_receiving_id: int) -> Response:
    content = request.get_json()
    shop_product_receiving_controller.patch(shop_product_receiving_id, content)
    return make_response("Shop product receiving updated", HTTPStatus.OK)

@shop_product_receiving_bp.delete('/<int:shop_product_receiving_id>')
def delete_shop_product_receiving(shop_product_receiving_id: int) -> Response:
    shop_product_receiving_controller.delete(shop_product_receiving_id)
    return make_response("Shop product receiving deleted", HTTPStatus.OK)

@shop_product_receiving_bp.get('/get_shop_product_receiving_after_shop/<int:shop_id>')
def get_shop_product_receiving_after_shop(shop_id) -> Response:
    return make_response(jsonify(shop_product_receiving_controller.get_shop_product_receiving_after_shop(shop_id)),
                         HTTPStatus.OK)

@shop_product_receiving_bp.get('/get_shop_product_receiving_after_product/<int:product_id>')
def get_shop_product_receiving_after_product(product_id) -> Response:
    return make_response(jsonify(shop_product_receiving_controller.get_shop_product_receiving_after_product(product_id)),
                         HTTPStatus.OK)