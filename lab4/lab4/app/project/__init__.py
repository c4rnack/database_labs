import os
import secrets
from typing import Dict, Any

import boto3
import botocore

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from flasgger import Swagger

from .auth.route import register_routes

SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

db = SQLAlchemy()

todos = {}

def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    _process_input_config(app_config, additional_config)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}

    _init_db(app)
    register_routes(app)
    
    Swagger(app)

    return app

def get_db_uri(): 
    ssm = boto3.client("ssm")
    try:
        param = ssm.get_parameter(Name="database-link", WithDecryption=True)
        return param["Parameter"]["Value"]
    except botocore.exceptions.ClientError as e:
        print("Error fetching DB URI:", e)
        return None

def _init_db(app: Flask) -> None:
    db.init_app(app)

    db_uri = get_db_uri()

    if not database_exists(db_uri):
        create_database(db_uri)

    import lab4.app.project.auth.domain
    with app.app_context(): db.create_all()


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    root_user = os.getenv(MYSQL_ROOT_USER, additional_config[MYSQL_ROOT_USER])
    root_password = os.getenv(MYSQL_ROOT_PASSWORD, additional_config[MYSQL_ROOT_PASSWORD])
    app_config[SQLALCHEMY_DATABASE_URI] = app_config[SQLALCHEMY_DATABASE_URI].format(root_user, root_password)
    pass