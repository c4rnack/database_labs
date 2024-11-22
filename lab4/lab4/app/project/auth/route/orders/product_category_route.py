from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import product_category_controller
from lab4.app.project.auth.domain import ProductCategory

product_category_bp = Blueprint('product_category', __name__, url_prefix='/product_category')

@product_category_bp.get('')
def get_all_product_category() -> Response:
    return make_response(jsonify(product_category_controller.find_all()), HTTPStatus.OK)

@product_category_bp.post('')
def create_product_category() -> Response:
    content = request.get_json()
    product_category = ProductCategory.create_from_dto(content)
    product_category_controller.create(product_category)
    return make_response(jsonify(product_category.put_into_dto()), HTTPStatus.CREATED)

@product_category_bp.get('/<int:product_category_id>')
def get_product_category(product_category_id: int) -> Response:
    return make_response(jsonify(product_category_controller.find_by_id(product_category_id)), HTTPStatus.OK)

@product_category_bp.put('/<int:product_category_id>')
def update_product_category(product_category_id: int) -> Response:
    content = request.get_json()
    product_category = ProductCategory.create_from_dto(content)
    product_category_controller.update(product_category_id, product_category)
    return make_response("Product category updated", HTTPStatus.OK)

@product_category_bp.patch('/<int:product_category_id>')
def patch_product_category(product_category_id: int) -> Response:
    content = request.get_json()
    product_category_controller.patch(product_category_id, content)
    return make_response("Product category updated", HTTPStatus.OK)

@product_category_bp.delete('/<int:product_category_id>')
def delete_product_category(product_category_id: int) -> Response:
    product_category_controller.delete(product_category_id)
    return make_response("Product category deleted", HTTPStatus.OK)