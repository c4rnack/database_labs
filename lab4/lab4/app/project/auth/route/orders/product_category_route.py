from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import product_category_controller
from lab4.app.project.auth.domain import ProductCategory

product_category_bp = Blueprint('product_category', __name__, url_prefix='/product_category')

@product_category_bp.get('')
def get_all_product_category() -> Response:
    """
    Get all product categories
    ---
    tags:
      - Product Category
    responses:
      200:
        description: List of all product categories
        examples:
          application/json: [
            {"id": 1, "name": "Beverages"},
            {"id": 2, "name": "Dairy"},
            {"id": 3, "name": "Snacks"},
            {"id": 4, "name": "Bakery"},
            {"id": 5, "name": "Household"}
          ]
    """
    return make_response(jsonify(product_category_controller.find_all()), HTTPStatus.OK)

@product_category_bp.post('')
def create_product_category() -> Response:
    """
    Create a new product category
    ---
    tags:
      - Product Category
    requestBody:
      required: true
      content:
        application/json:
          example:
            name: "Frozen Foods"
    responses:
      201:
        description: Category created successfully
        examples:
          application/json: {"id": 6, "name": "Frozen Foods"}
    """
    content = request.get_json()
    product_category = ProductCategory.create_from_dto(content)
    product_category_controller.create(product_category)
    return make_response(jsonify(product_category.put_into_dto()), HTTPStatus.CREATED)

@product_category_bp.get('/<int:product_category_id>')
def get_product_category(product_category_id: int) -> Response:
    """
    Get product category by ID
    ---
    tags:
      - Product Category
    parameters:
      - in: path
        name: product_category_id
        required: true
        schema:
          type: integer
        description: The ID of the product category
    responses:
      200:
        description: Product category details
        examples:
          application/json: {"id": 2, "name": "Dairy"}
      404:
        description: Category not found
    """
    return make_response(jsonify(product_category_controller.find_by_id(product_category_id)), HTTPStatus.OK)

@product_category_bp.put('/<int:product_category_id>')
def update_product_category(product_category_id: int) -> Response:
    """
    Update a product category
    ---
    tags:
      - Product Category
    parameters:
      - in: path
        name: product_category_id
        required: true
        schema:
          type: integer
        description: The ID of the category to update
    requestBody:
      required: true
      content:
        application/json:
          example:
            name: "Confectionery"
    responses:
      200:
        description: Category updated successfully
    """
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
    """
    Delete a product category
    ---
    tags:
      - Product Category
    parameters:
      - in: path
        name: product_category_id
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Category deleted successfully
    """
    product_category_controller.delete(product_category_id)
    return make_response("Product category deleted", HTTPStatus.OK)