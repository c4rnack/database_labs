from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import delivery_type_controller
from lab4.app.project.auth.domain import DeliveryType

delivery_type_bp = Blueprint('delivery_type', __name__, url_prefix='/delivery_type')

@delivery_type_bp.get('')
def get_all_delivery_type() -> Response:
    return make_response(jsonify(delivery_type_controller.find_all()), HTTPStatus.OK)

@delivery_type_bp.post('')
def create_delivery_type() -> Response:
    content = request.get_json()
    delivery_type = DeliveryType.create_from_dto(content)
    delivery_type_controller.create(delivery_type)
    return make_response(jsonify(delivery_type.put_into_dto()), HTTPStatus.CREATED)

@delivery_type_bp.get('/<int:delivery_type_id>')
def get_delivery_type(delivery_type_id: int) -> Response:
    return make_response(jsonify(delivery_type_controller.find_by_id(delivery_type_id)), HTTPStatus.OK)


@delivery_type_bp.put('/<int:delivery_type_id>')
def update_delivery_type(delivery_type_id: int) -> Response:
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
    delivery_type_controller.delete(delivery_type_id)
    return make_response("Delivery type deleted", HTTPStatus.OK)
