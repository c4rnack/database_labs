from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.project.auth.controller import client_controller
from lab4.app.project.auth.domain import Client


client_bp = Blueprint('client', __name__, url_prefix='/client')

@client_bp.get('')
def get_all_client() -> Response:
    """
    Get all clients
    ---
    tags:
      - Client
    responses:
      200:
        description: List of all clients
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(client_controller.find_all()), HTTPStatus.OK)

@client_bp.post('')
def create_client() -> Response:
    """
    Create a new client
    ---
    tags:
      - Client
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              name:
                type: string
              email:
                type: string
    responses:
      201:
        description: Client created successfully
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    client = Client.create_from_dto(content)
    client_controller.create(client)
    return make_response(jsonify(client.put_into_dto()), HTTPStatus.CREATED)

@client_bp.get('/<int:client_id>')
def get_client(client_id: int) -> Response:
    """
    Get client by ID
    ---
    tags:
      - Client
    parameters:
      - name: client_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Client object
        content:
          application/json:
            schema:
              type: object
      404:
        description: Client not found
    """
    return make_response(jsonify(client_controller.find_by_id(client_id)), HTTPStatus.OK)


@client_bp.put('/<int:client_id>')
def update_client(client_id: int) -> Response:
    """
    Update client by ID
    ---
    tags:
      - Client
    parameters:
      - name: client_id
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
    responses:
      200:
        description: Client updated successfully
      404:
        description: Client not found
    """
    content = request.get_json()
    client = Client.create_from_dto(content)
    client_controller.update(client_id, client)
    return make_response("Client updated", HTTPStatus.OK)


@client_bp.patch('/<int:client_id>')
def patch_client(client_id: int) -> Response:
    content = request.get_json()
    client_controller.patch(client_id, content)
    return make_response("Client updated", HTTPStatus.OK)


@client_bp.delete('/<int:client_id>')
def delete_client(client_id: int) -> Response:
    """
    Delete client by ID
    ---
    tags:
      - Client
    parameters:
      - name: client_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Client deleted successfully
      404:
        description: Client not found
    """
    client_controller.delete(client_id)
    return make_response("Client deleted", HTTPStatus.OK)
