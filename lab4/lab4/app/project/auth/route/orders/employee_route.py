from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import employee_controller
from lab4.app.project.auth.domain import Employee

employee_bp = Blueprint('employee', __name__, url_prefix='/employee')

@employee_bp.get('')
def get_all_employee() -> Response:
    """
    Get all employees
    ---
    tags:
      - Employee
    responses:
      200:
        description: List of all employees
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
                  surname:
                    type: string
                  phone_number:
                    type: string
                  position_id:
                    type: integer
                  shop_id:
                    type: integer
    """
    return make_response(jsonify(employee_controller.find_all()), HTTPStatus.OK)

@employee_bp.post('')
def create_employee() -> Response:
    """
    Create a new employee
    ---
    tags:
      - Employee
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required: [name, surname, phone_number, position_id, shop_id]
            properties:
              name:
                type: string
              surname:
                type: string
              phone_number:
                type: string
              position_id:
                type: integer
              shop_id:
                type: integer
    responses:
      201:
        description: Employee created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                name:
                  type: string
                surname:
                  type: string
                phone_number:
                  type: string
                position_id:
                  type: integer
                shop_id:
                  type: integer
    """
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.create(employee)
    return make_response(jsonify(employee.put_into_dto()), HTTPStatus.CREATED)

@employee_bp.get('/<int:employee_id>')
def get_employee_position(employee_id: int) -> Response:
    """
    Get employee by ID
    ---
    tags:
      - Employee
    parameters:
      - name: employee_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Employee found
        content:
          application/json:
            schema:
              type: object
    404:
        description: Employee not found
    """
    return make_response(jsonify(employee_controller.find_by_id(employee_id)), HTTPStatus.OK)

@employee_bp.put('/<int:employee_id>')
def update_employee(employee_id: int) -> Response:
    """
    Update employee (full update)
    ---
    tags:
      - Employee
    parameters:
      - name: employee_id
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
              surname: {type: string}
              phone_number: {type: string}
              position_id: {type: integer}
              shop_id: {type: integer}
    responses:
      200:
        description: Employee updated
    """
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
    """
    Delete employee by ID
    ---
    tags:
      - Employee
    parameters:
      - name: employee_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Employee deleted
    """
    employee_controller.delete(employee_id)
    return make_response("Employee deleted", HTTPStatus.OK)

@employee_bp.get('/get_employee_after_shop/<int:shop_id>')
def get_employee_after_shop(shop_id: int) -> Response:
    return make_response(jsonify(employee_controller.get_employee_after_shop(shop_id)), HTTPStatus.OK)

@employee_bp.get('/get_employee_after_employee_position/<int:position_id>')
def get_employee_after_employee_position(position_id: int) -> Response:
    return make_response(jsonify(employee_controller.get_employee_after_employee_position(position_id)), HTTPStatus.OK)