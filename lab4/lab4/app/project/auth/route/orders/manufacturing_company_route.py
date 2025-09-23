from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import manufacturing_company_controller
from lab4.app.project.auth.domain import ManufacturingCompany

manufacturing_company_bp = Blueprint('manufacturing_company', __name__, url_prefix='/manufacturing_company')

@manufacturing_company_bp.get('')
def get_all_manufacturing_company() -> Response:
    """
    Get all manufacturing companies
    ---
    tags:
      - Manufacturing Company
    responses:
      200:
        description: List of all manufacturing companies
        examples:
          application/json: [
            {"id": 1, "name": "Roshen", "city": "Kyiv", "street": "Leiptsyzka", "house_number": 1},
            {"id": 2, "name": "Coca-Cola Beverages Ukraine", "city": "Kyiv", "street": "Vyzvolyteliv", "house_number": 2},
            {"id": 3, "name": "Danone", "city": "Lviv", "street": "Hrushevskoho", "house_number": 15}
          ]
    """
    return make_response(jsonify(manufacturing_company_controller.find_all()), HTTPStatus.OK)

@manufacturing_company_bp.post('')
def create_manufacturing_company() -> Response:
    """
    Create a new manufacturing company
    ---
    tags:
      - Manufacturing Company
    requestBody:
      required: true
      content:
        application/json:
          example:
            name: "Carlsberg Ukraine"
            city: "Lviv"
            street: "Stryyska"
            house_number: 39
    responses:
      201:
        description: Company created successfully
        examples:
          application/json: {"id": 6, "name": "Carlsberg Ukraine", "city": "Lviv", "street": "Stryyska", "house_number": 39}
    """
    content = request.get_json()
    employee = ManufacturingCompany.create_from_dto(content)
    manufacturing_company_controller.create(employee)
    return make_response(jsonify(employee.put_into_dto()), HTTPStatus.CREATED)

@manufacturing_company_bp.get('/<int:manufacturing_company_id>')
def get_manufacturing_company(manufacturing_company_id: int) -> Response:
    """
    Get manufacturing company by ID
    ---
    tags:
      - Manufacturing Company
    parameters:
      - in: path
        name: manufacturing_company_id
        required: true
        schema:
          type: integer
        description: The ID of the manufacturing company
    responses:
      200:
        description: Manufacturing company details
        examples:
          application/json: {"id": 1, "name": "Roshen", "city": "Kyiv", "street": "Leiptsyzka", "house_number": 1}
      404:
        description: Company not found
    """
    return make_response(jsonify(manufacturing_company_controller.find_by_id(manufacturing_company_id)), HTTPStatus.OK)

@manufacturing_company_bp.put('/<int:manufacturing_company_id>')
def update_manufacturing_company(manufacturing_company_id: int) -> Response:
    """
    Update a manufacturing company
    ---
    tags:
      - Manufacturing Company
    parameters:
      - in: path
        name: manufacturing_company_id
        required: true
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          example:
            name: "Nestle"
            city: "Kharkiv"
            street: "Poltavskyi Shlyakh"
            house_number: 40
    responses:
      200:
        description: Manufacturing company updated successfully
    """
    content = request.get_json()
    manufacturing_company = ManufacturingCompany.create_from_dto(content)
    manufacturing_company_controller.update(manufacturing_company_id, manufacturing_company)
    return make_response("Manufacturing company updated", HTTPStatus.OK)

@manufacturing_company_bp.patch('/<int:manufacturing_company_id>')
def patch_manufacturing_company(manufacturing_company_id: int) -> Response:
    content = request.get_json()
    manufacturing_company_controller.patch(manufacturing_company_id, content)
    return make_response("Manufacturing company updated", HTTPStatus.OK)

@manufacturing_company_bp.delete('/<int:manufacturing_company_id>')
def delete_manufacturing_company(manufacturing_company_id: int) -> Response:
    """
    Delete a manufacturing company
    ---
    tags:
      - Manufacturing Company
    parameters:
      - in: path
        name: manufacturing_company_id
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Manufacturing company deleted successfully
    """
    manufacturing_company_controller.delete(manufacturing_company_id)
    return make_response("Manufacturing company deleted", HTTPStatus.OK)
