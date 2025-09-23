from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import product_controller
from lab4.app.project.auth.domain import Product

product_bp = Blueprint('product', __name__, url_prefix='/product')

@product_bp.get('')
def get_all_product() -> Response:
    """
    Get all products
    ---
    tags:
      - Product
    responses:
      200:
        description: List of all products
        examples:
          application/json: [
            {"id": 1, "name": "Roshen Chocolate Bar", "price_UAH": 45, "description": "Dark chocolate bar 100g", "shelf_time_WEEKS": 52, "product_category_id": 5, "manufacturing_company_id": 1},
            {"id": 2, "name": "Coca-Cola 1L", "price_UAH": 20, "description": "Carbonated soft drink 1L", "shelf_time_WEEKS": 12, "product_category_id": 4, "manufacturing_company_id": 2}
          ]
    """
    return make_response(jsonify(product_controller.find_all()), HTTPStatus.OK)

@product_bp.post('')
def create_product() -> Response:
    """
    Create a new product
    ---
    tags:
      - Product
    requestBody:
      required: true
      content:
        application/json:
          example:
            name: "Oreo Cookies"
            price_UAH: 40
            description: "Chocolate sandwich cookies 150g"
            shelf_time_WEEKS: 52
            product_category_id: 5
            manufacturing_company_id: 1
    responses:
      201:
        description: Product created successfully
        examples:
          application/json: {"id": 11, "name": "Oreo Cookies", "price_UAH": 40, "description": "Chocolate sandwich cookies 150g", "shelf_time_WEEKS": 52, "product_category_id": 5, "manufacturing_company_id": 1}
    """
    content = request.get_json()
    product = Product.create_from_dto(content)
    product_controller.create(product)
    return make_response(jsonify(product.put_into_dto()), HTTPStatus.CREATED)

@product_bp.get('/<int:product_id>')
def get_product(product_id: int) -> Response:
    """
    Get a product by ID
    ---
    tags:
      - Product
    parameters:
      - in: path
        name: product_id
        required: true
        schema:
          type: integer
        description: The ID of the product
    responses:
      200:
        description: Product details
        examples:
          application/json: {"id": 1, "name": "Roshen Chocolate Bar", "price_UAH": 45, "description": "Dark chocolate bar 100g", "shelf_time_WEEKS": 52, "product_category_id": 5, "manufacturing_company_id": 1}
      404:
        description: Product not found
    """
    return make_response(jsonify(product_controller.find_by_id(product_id)), HTTPStatus.OK)

@product_bp.put('/<int:product_id>')
def update_product(product_id: int) -> Response:
    """
    Update a product
    ---
    tags:
      - Product
    parameters:
      - in: path
        name: product_id
        required: true
        schema:
          type: integer
        description: The ID of the product to update
    requestBody:
      required: true
      content:
        application/json:
          example:
            name: "Carlsberg Beer 0.5L"
            price_UAH: 30
            description: "Alcoholic beverage"
            shelf_time_WEEKS: 24
            product_category_id: 4
            manufacturing_company_id: 6
    responses:
      200:
        description: Product updated successfully
    """
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
    """
    Delete a product
    ---
    tags:
      - Product
    parameters:
      - in: path
        name: product_id
        required: true
        schema:
          type: integer
        description: The ID of the product to delete
    responses:
      200:
        description: Product deleted successfully
    """
    product_controller.delete(product_id)
    return make_response("Product deleted", HTTPStatus.OK)

@product_bp.get('/get_product_after_category/<int:category_id>')
def get_product_after_category(category_id: int) -> Response:
    return make_response(jsonify(product_controller.get_product_after_category(category_id)), HTTPStatus.OK)

@product_bp.get('/get_product_after_manufacturing_company/<int:manufacturing_company_id>')
def get_product_after_manufacturing_company(manufacturing_company_id: int) -> Response:
    return make_response(jsonify(product_controller.get_product_after_manufacturing_company(manufacturing_company_id)), HTTPStatus.OK)