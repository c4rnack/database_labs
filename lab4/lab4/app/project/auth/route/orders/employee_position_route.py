from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import employee_position_controller
from lab4.app.project.auth.domain import EmployeePosition

employee_position_bp = Blueprint('employee_position', __name__, url_prefix='/employee_position')

@employee_position_bp.get('')
def get_all_employee_position() -> Response:
    return make_response(jsonify(employee_position_controller.find_all()), HTTPStatus.OK)

@employee_position_bp.post('')
def create_employee_position() -> Response:
    content = request.get_json()
    employee_position = EmployeePosition.create_from_dto(content)
    employee_position_controller.create(employee_position)
    return make_response(jsonify(employee_position.put_into_dto()), HTTPStatus.CREATED)

@employee_position_bp.get('/<int:employee_position_id>')
def get_employee_position(employee_position_id: int) -> Response:
    return make_response(jsonify(employee_position_controller.find_by_id(employee_position_id)), HTTPStatus.OK)


@employee_position_bp.put('/<int:employee_position_id>')
def update_employee_position(employee_position_id: int) -> Response:
    content = request.get_json()
    employee_position = EmployeePosition.create_from_dto(content)
    employee_position_controller.update(employee_position_id, employee_position)
    return make_response("Employee position updated", HTTPStatus.OK)


@employee_position_bp.patch('/<int:employee_position_id>')
def patch_employee_position(employee_position_id: int) -> Response:
    content = request.get_json()
    employee_position_controller.patch(employee_position_id, content)
    return make_response("Employee position updated", HTTPStatus.OK)


@employee_position_bp.delete('/<int:employee_position_id>')
def delete_employee_position(employee_position_id: int) -> Response:
    employee_position_controller.delete(employee_position_id)
    return make_response("Employee position deleted", HTTPStatus.OK)
