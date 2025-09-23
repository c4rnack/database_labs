from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import shop_product_receiving_controller
from lab4.app.project.auth.domain import ShopProductReceiving

shop_product_receiving_bp = Blueprint('shop_product_receiving', __name__, url_prefix='/shop_product_receiving')

@shop_product_receiving_bp.get('')
def get_all_shop_product_receiving() -> Response:
    """
    Get all shop product receiving records
    ---
    tags:
      - Shop Product Receiving
    responses:
      200:
        description: List of product receivings in shops
        examples:
          application/json: [
            {"id": 1, "product_id": 1, "shop_id": 1, "date": "2023-10-01"},
            {"id": 2, "product_id": 2, "shop_id": 1, "date": "2023-10-02"}
          ]
    """
    return make_response(jsonify(shop_product_receiving_controller.find_all()), HTTPStatus.OK)

@shop_product_receiving_bp.post('')
def create_shop_product_receiving() -> Response:
    """
    Create a new shop product receiving record
    ---
    tags:
      - Shop Product Receiving
    requestBody:
      required: true
      content:
        application/json:
          example:
            product_id: 3
            shop_id: 2
            date: "2023-10-03"
    responses:
      201:
        description: Shop product receiving created
        examples:
          application/json: {"id": 3, "product_id": 3, "shop_id": 2, "date": "2023-10-03"}
    """
    content = request.get_json()
    shop_product_receiving = ShopProductReceiving.create_from_dto(content)
    shop_product_receiving_controller.create(shop_product_receiving)
    return make_response(jsonify(shop_product_receiving.put_into_dto()), HTTPStatus.CREATED)

@shop_product_receiving_bp.get('/<int:shop_product_receiving_id>')
def get_shop_product_receiving(shop_product_receiving_id: int) -> Response:
    """
    Get a specific shop product receiving by ID
    ---
    tags:
      - Shop Product Receiving
    parameters:
      - in: path
        name: shop_product_receiving_id
        required: true
        schema:
          type: integer
        description: The ID of the receiving record
    responses:
      200:
        description: Shop product receiving details
        examples:
          application/json: {"id": 1, "product_id": 1, "shop_id": 1, "date": "2023-10-01"}
      404:
        description: Record not found
    """
    return make_response(jsonify(shop_product_receiving_controller.find_by_id(shop_product_receiving_id)), HTTPStatus.OK)

@shop_product_receiving_bp.put('/<int:shop_product_receiving_id>')
def update_shop_product_receiving(shop_product_receiving_id: int) -> Response:
    """
    Update a shop product receiving record
    ---
    tags:
      - Shop Product Receiving
    parameters:
      - in: path
        name: shop_product_receiving_id
        required: true
        schema:
          type: integer
        description: The ID of the record to update
    requestBody:
      required: true
      content:
        application/json:
          example:
            product_id: 2
            shop_id: 1
            date: "2023-10-10"
    responses:
      200:
        description: Shop product receiving updated
    """
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
    """
    Delete a shop product receiving record
    ---
    tags:
      - Shop Product Receiving
    parameters:
      - in: path
        name: shop_product_receiving_id
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Shop product receiving deleted
    """
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