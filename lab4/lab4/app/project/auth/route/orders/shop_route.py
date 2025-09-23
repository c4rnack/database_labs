from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import shop_controller
from lab4.app.project.auth.domain import Shop

shop_bp = Blueprint('shop', __name__, url_prefix='/shop')

@shop_bp.get('')
def get_all_shop() -> Response:
    """
    Get all shops
    ---
    tags:
      - Shop
    responses:
      200:
        description: List of all shops
        examples:
          application/json: [
            {"id": 1, "city": "Kyiv", "street": "Khreshchatyk", "house_number": 1},
            {"id": 2, "city": "Lviv", "street": "Shevchenko", "house_number": 10},
            {"id": 3, "city": "Odessa", "street": "Deribasivska", "house_number": 20}
          ]
    """
    return make_response(jsonify(shop_controller.find_all()), HTTPStatus.OK)

@shop_bp.post('')
def create_shop() -> Response:
    """
    Create a new shop
    ---
    tags:
      - Shop
    requestBody:
      required: true
      content:
        application/json:
          example:
            city: "Dnipro"
            street: "Centralna"
            house_number: 15
    responses:
      201:
        description: Shop created successfully
        examples:
          application/json: {"id": 11, "city": "Dnipro", "street": "Centralna", "house_number": 15}
    """
    content = request.get_json()
    shop = Shop.create_from_dto(content)
    shop.create(shop)
    return make_response(jsonify(shop.put_into_dto()), HTTPStatus.CREATED)

@shop_bp.get('/<int:shop_id>')
def get_shop(shop_id: int) -> Response:
    """
    Get shop by ID
    ---
    tags:
      - Shop
    parameters:
      - in: path
        name: shop_id
        required: true
        schema:
          type: integer
        description: The ID of the shop
    responses:
      200:
        description: Shop details
        examples:
          application/json: {"id": 1, "city": "Kyiv", "street": "Khreshchatyk", "house_number": 1}
      404:
        description: Shop not found
    """
    return make_response(jsonify(shop_controller.find_by_id(shop_id)), HTTPStatus.OK)

@shop_bp.put('/<int:shop_id>')
def update_shop(shop_id: int) -> Response:
    """
    Update a shop
    ---
    tags:
      - Shop
    parameters:
      - in: path
        name: shop_id
        required: true
        schema:
          type: integer
        description: The ID of the shop to update
    requestBody:
      required: true
      content:
        application/json:
          example:
            city: "Kharkiv"
            street: "Sumska"
            house_number: 25
    responses:
      200:
        description: Shop updated successfully
    """
    content = request.get_json()
    shop = Shop.create_from_dto(content)
    shop_controller.update(shop_id, shop)
    return make_response("Shop updated", HTTPStatus.OK)

@shop_bp.patch('/<int:shop_id>')
def patch_shop(shop_id: int) -> Response:
    content = request.get_json()
    shop_controller.patch(shop_id, content)
    return make_response("Shop updated", HTTPStatus.OK)

@shop_bp.delete('/<int:shop_id>')
def delete_shop(shop_id: int) -> Response:
    """
    Delete a shop
    ---
    tags:
      - Shop
    parameters:
      - in: path
        name: shop_id
        required: true
        schema:
          type: integer
        description: The ID of the shop to delete
    responses:
      200:
        description: Shop deleted successfully
    """
    shop_controller.delete(shop_id)
    return make_response("Shop deleted", HTTPStatus.OK)