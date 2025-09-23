from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import employee_position_controller
from lab4.app.project.auth.domain import EmployeePosition

employee_position_bp = Blueprint('employee_position', __name__, url_prefix='/employee_position')

@employee_position_bp.get('')
def get_all_employee_position() -> Response:
    """
    Get all employee positions
    ---
    tags:
      - EmployeePosition
    responses:
      200:
        description: List of all employee positions
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
    return make_response(jsonify(employee_position_controller.find_all()), HTTPStatus.OK)

@employee_position_bp.post('')
def create_employee_position() -> Response:
    """
    Create a new employee position
    ---
    tags:
      - EmployeePosition
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
        description: Employee position created successfully
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
    employee_position = EmployeePosition.create_from_dto(content)
    employee_position_controller.create(employee_position)
    return make_response(jsonify(employee_position.put_into_dto()), HTTPStatus.CREATED)

@employee_position_bp.get('/<int:employee_position_id>')
def get_employee_position(employee_position_id: int) -> Response:
    """
    Get employee position by ID
    ---
    tags:
      - EmployeePosition
    parameters:
      - name: employee_position_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Employee position found
        content:
          application/json:
            schema:
              type: object
              properties:
                id: {type: integer}
                name: {type: string}
      404:
        description: Employee position not found
    """
    return make_response(jsonify(employee_position_controller.find_by_id(employee_position_id)), HTTPStatus.OK)


@employee_position_bp.put('/<int:employee_position_id>')
def update_employee_position(employee_position_id: int) -> Response:
    """
    Update employee position (full update)
    ---
    tags:
      - EmployeePosition
    parameters:
      - name: employee_position_id
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
        description: Employee position updated
    """
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
    """
    Delete employee position by ID
    ---
    tags:
      - EmployeePosition
    parameters:
      - name: employee_position_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Employee position deleted
    """
    employee_position_controller.delete(employee_position_id)
    return make_response("Employee position deleted", HTTPStatus.OK)
