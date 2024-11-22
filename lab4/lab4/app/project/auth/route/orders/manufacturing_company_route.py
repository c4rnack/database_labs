from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import manufacturing_company_controller
from lab4.app.project.auth.domain import ManufacturingCompany

manufacturing_company_bp = Blueprint('manufacturing_company', __name__, url_prefix='/manufacturing_company')

@manufacturing_company_bp.get('')
def get_all_manufacturing_company() -> Response:
    return make_response(jsonify(manufacturing_company_controller.find_all()), HTTPStatus.OK)

@manufacturing_company_bp.post('')
def create_manufacturing_company() -> Response:
    content = request.get_json()
    employee = ManufacturingCompany.create_from_dto(content)
    manufacturing_company_controller.create(employee)
    return make_response(jsonify(employee.put_into_dto()), HTTPStatus.CREATED)

@manufacturing_company_bp.get('/<int:manufacturing_company_id>')
def get_manufacturing_company(manufacturing_company_id: int) -> Response:
    return make_response(jsonify(manufacturing_company_controller.find_by_id(manufacturing_company_id)), HTTPStatus.OK)

@manufacturing_company_bp.put('/<int:manufacturing_company_id>')
def update_manufacturing_company(manufacturing_company_id: int) -> Response:
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
    manufacturing_company_controller.delete(manufacturing_company_id)
    return make_response("Manufacturing company deleted", HTTPStatus.OK)
