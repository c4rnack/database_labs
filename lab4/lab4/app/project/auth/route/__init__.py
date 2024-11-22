from flask import Flask
from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)

    from .orders.shop_route import shop_bp
    from .orders.product_category_route import product_category_bp
    from .orders.employee_position_route import employee_position_bp
    from .orders.manufacturing_company_route import manufacturing_company_bp
    from .orders.delivery_type_route import delivery_type_bp
    from .orders.client_route import client_bp
    from .orders.employee_route import employee_bp
    from .orders.product_route import product_bp
    from .orders.shop_product_receiving_route import shop_product_receiving_bp
    from .orders.client_product_delivery_route import client_product_delivery_bp

    app.register_blueprint(shop_bp)
    app.register_blueprint(product_category_bp)
    app.register_blueprint(employee_position_bp)
    app.register_blueprint(manufacturing_company_bp)
    app.register_blueprint(delivery_type_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(shop_product_receiving_bp)
    app.register_blueprint(client_product_delivery_bp)