from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import employee_controller
from lab4.app.project.auth.domain import Employee

employee_bp = Blueprint('employee', __name__, url_prefix='/employee')

@employee_bp.get('')
def get_all_employee() -> Response:
    return make_response(jsonify(employee_controller.find_all()), HTTPStatus.OK)

@employee_bp.post('')
def create_employee() -> Response:
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.create(employee)
    return make_response(jsonify(employee.put_into_dto()), HTTPStatus.CREATED)

@employee_bp.get('/<int:employee_id>')
def get_employee_position(employee_id: int) -> Response:
    return make_response(jsonify(employee_controller.find_by_id(employee_id)), HTTPStatus.OK)

@employee_bp.put('/<int:employee_id>')
def update_employee(employee_id: int) -> Response:
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.update(employee_id, employee)
    return make_response("Employee updated", HTTPStatus.OK)

@employee_bp.patch('/<int:employee_id>')
def patch_employee_position(employee_id: int) -> Response:
    content = request.get_json()
    employee_controller.patch(employee_id, content)
    return make_response("Employee updated", HTTPStatus.OK)

@employee_bp.delete('/<int:employee_id>')
def delete_employee(employee_id: int) -> Response:
    employee_controller.delete(employee_id)
    return make_response("Employee deleted", HTTPStatus.OK)

@employee_bp.get('/get_employee_after_shop/<int:shop_id>')
def get_employee_after_shop(shop_id: int) -> Response:
    return make_response(jsonify(employee_controller.get_employee_after_shop(shop_id)), HTTPStatus.OK)

@employee_bp.get('/get_employee_after_employee_position/<int:position_id>')
def get_employee_after_employee_position(position_id: int) -> Response:
    return make_response(jsonify(employee_controller.get_employee_after_employee_position(position_id)), HTTPStatus.OK)