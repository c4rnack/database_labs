from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import delivery_type_controller
from lab4.app.project.auth.domain import DeliveryType

delivery_type_bp = Blueprint('delivery_type', __name__, url_prefix='/delivery_type')

@delivery_type_bp.get('')
def get_all_delivery_type() -> Response:
    """
    Get all delivery types
    ---
    tags:
      - DeliveryType
    responses:
      200:
        description: List of all delivery types
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  name:
                    type: string
    """
    return make_response(jsonify(delivery_type_controller.find_all()), HTTPStatus.OK)

@delivery_type_bp.post('')
def create_delivery_type() -> Response:
    """
    Create a new delivery type
    ---
    tags:
      - DeliveryType
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required: [name]
            properties:
              name:
                type: string
    responses:
      201:
        description: Delivery type created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                name:
                  type: string
    """
    content = request.get_json()
    delivery_type = DeliveryType.create_from_dto(content)
    delivery_type_controller.create(delivery_type)
    return make_response(jsonify(delivery_type.put_into_dto()), HTTPStatus.CREATED)

@delivery_type_bp.get('/<int:delivery_type_id>')
def get_delivery_type(delivery_type_id: int) -> Response:
    """
    Get delivery type by ID
    ---
    tags:
      - DeliveryType
    parameters:
      - name: delivery_type_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Delivery type found
        content:
          application/json:
            schema:
              type: object
              properties:
                id: {type: integer}
                name: {type: string}
      404:
        description: Delivery type not found
    """
    return make_response(jsonify(delivery_type_controller.find_by_id(delivery_type_id)), HTTPStatus.OK)


@delivery_type_bp.put('/<int:delivery_type_id>')
def update_delivery_type(delivery_type_id: int) -> Response:
    """
    Update delivery type (full update)
    ---
    tags:
      - DeliveryType
    parameters:
      - name: delivery_type_id
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
            properties:
              name: {type: string}
    responses:
      200:
        description: Delivery type updated
    """
    content = request.get_json()
    delivery_type = DeliveryType.create_from_dto(content)
    delivery_type_controller.update(delivery_type_id, delivery_type)
    return make_response("Delivery type updated", HTTPStatus.OK)


@delivery_type_bp.patch('/<int:delivery_type_id>')
def patch_delivery_type(delivery_type_id: int) -> Response:
    content = request.get_json()
    delivery_type_controller.patch(delivery_type_id, content)
    return make_response("Delivery type updated", HTTPStatus.OK)


@delivery_type_bp.delete('/<int:delivery_type_id>')
def delete_delivery_type(delivery_type_id: int) -> Response:
    """
    Delete delivery type by ID
    ---
    tags:
      - DeliveryType
    parameters:
      - name: delivery_type_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Delivery type deleted
    """
    delivery_type_controller.delete(delivery_type_id)
    return make_response("Delivery type deleted", HTTPStatus.OK)
