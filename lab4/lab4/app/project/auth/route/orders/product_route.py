from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import product_controller
from lab4.app.project.auth.domain import Product

product_bp = Blueprint('product', __name__, url_prefix='/product')

@product_bp.get('')
def get_all_product() -> Response:
    return make_response(jsonify(product_controller.find_all()), HTTPStatus.OK)

@product_bp.post('')
def create_product() -> Response:
    content = request.get_json()
    product = Product.create_from_dto(content)
    product_controller.create(product)
    return make_response(jsonify(product.put_into_dto()), HTTPStatus.CREATED)

@product_bp.get('/<int:product_id>')
def get_product(product_id: int) -> Response:
    return make_response(jsonify(product_controller.find_by_id(product_id)), HTTPStatus.OK)

@product_bp.put('/<int:product_id>')
def update_product(product_id: int) -> Response:
    content = request.get_json()
    product = Product.create_from_dto(content)
    product_controller.update(product_id, product)
    return make_response("Product updated", HTTPStatus.OK)

@product_bp.patch('/<int:product_id>')
def patch_product(product_id: int) -> Response:
    content = request.get_json()
    product_controller.patch(product_id, content)
    return make_response("Product updated", HTTPStatus.OK)

@product_bp.delete('/<int:product_id>')
def delete_product(product_id: int) -> Response:
    product_controller.delete(product_id)
    return make_response("Product deleted", HTTPStatus.OK)

@product_bp.get('/get_product_after_category/<int:category_id>')
def get_product_after_category(category_id: int) -> Response:
    return make_response(jsonify(product_controller.get_product_after_category(category_id)), HTTPStatus.OK)

@product_bp.get('/get_product_after_manufacturing_company/<int:manufacturing_company_id>')
def get_product_after_manufacturing_company(manufacturing_company_id: int) -> Response:
    return make_response(jsonify(product_controller.get_product_after_manufacturing_company(manufacturing_company_id)), HTTPStatus.OK)