from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import client_product_delivery_controller
from lab4.app.project.auth.domain import ClientProductDelivery


client_product_delivery_bp = Blueprint('client_product_delivery_route'
, __name__, url_prefix='/client_product_delivery')

@client_product_delivery_bp.get('')
def get_all_client_product_delivery() -> Response:
    """
    Get all client product deliveries
    ---
    tags:
      - ClientProductDelivery
    responses:
      200:
        description: List of all client product deliveries
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(client_product_delivery_controller.find_all()), HTTPStatus.OK)

@client_product_delivery_bp.post('')
def create_client_product_delivery() -> Response:
    """
    Create a new client product delivery
    ---
    tags:
      - ClientProductDelivery
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
    responses:
      201:
        description: Client product delivery created successfully
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    client_product_delivery = ClientProductDelivery.create_from_dto(content)
    client_product_delivery_controller.create(client_product_delivery)
    return make_response(jsonify(client_product_delivery.put_into_dto()), HTTPStatus.CREATED)

@client_product_delivery_bp.get('/<int:client_product_delivery_id>')
def get_client_product_delivery(client_product_delivery_id: int) -> Response:
    """
    Get client product delivery by ID
    ---
    tags:
      - ClientProductDelivery
    parameters:
      - name: client_product_delivery_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Client product delivery object
        content:
          application/json:
            schema:
              type: object
      404:
        description: Not found
    """
    return make_response(jsonify(client_product_delivery_controller.find_by_id(client_product_delivery_id)), HTTPStatus.OK)


@client_product_delivery_bp.put('/<int:client_product_delivery_id>')
def update_client_product_delivery(client_product_delivery_id: int) -> Response:
    """
    Update client product delivery by ID
    ---
    tags:
      - ClientProductDelivery
    parameters:
      - name: client_product_delivery_id
        in: path
        required: true
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
    responses:
      200:
        description: Client product delivery updated successfully
      404:
        description: Not found
    """
    content = request.get_json()
    client_product_delivery = ClientProductDelivery.create_from_dto(content)
    client_product_delivery_controller.update(client_product_delivery_id, client_product_delivery)
    return make_response("Client product delivery updated", HTTPStatus.OK)


@client_product_delivery_bp.patch('/<int:client_product_delivery_id>')
def patch_client_product_delivery(client_product_delivery_id: int) -> Response:
    content = request.get_json()
    client_product_delivery_controller.patch(client_product_delivery_id, content)
    return make_response("Client product delivery updated", HTTPStatus.OK)


@client_product_delivery_bp.delete('/<int:client_product_delivery_id>')
def delete_client_product_delivery(client_product_delivery_id: int) -> Response:
    """
    Delete client product delivery by ID
    ---
    tags:
      - ClientProductDelivery
    parameters:
      - name: client_product_delivery_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Client product delivery deleted successfully
      404:
        description: Not found
    """
    client_product_delivery_controller.delete(client_product_delivery_id)
    return make_response("Client product delivery deleted", HTTPStatus.OK)

@client_product_delivery_bp.get('/get_client_product_delivery_after_product/<int:product_id>')
def get_client_product_delivery_after_product(product_id) -> Response:
    return make_response(
        jsonify(client_product_delivery_controller.get_client_product_delivery_after_product(product_id)),
        HTTPStatus.OK)

@client_product_delivery_bp.get('/get_client_product_delivery_after_shop/<int:shop_id>')
def get_client_product_delivery_after_shop(shop_id) -> Response:
    return make_response(jsonify(client_product_delivery_controller.get_client_product_delivery_after_shop(shop_id)),
                         HTTPStatus.OK)

@client_product_delivery_bp.get('/get_client_product_delivery_after_client/<int:client_id>')
def get_client_product_delivery_after_client(client_id) -> Response:
    return make_response(jsonify(client_product_delivery_controller.get_client_product_delivery_after_client(client_id)),
                         HTTPStatus.OK)

@client_product_delivery_bp.get('/get_client_product_delivery_after_delivery_type/<int:delivery_type_id>')
def get_client_product_delivery_after_delivery_type(delivery_type_id) -> Response:
    return make_response(jsonify(client_product_delivery_controller.get_client_product_delivery_after_delivery_type(delivery_type_id)),
                         HTTPStatus.OK)