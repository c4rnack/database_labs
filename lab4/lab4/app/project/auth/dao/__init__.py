from .orders.shop_dao import ShopDAO
from .orders.product_category_dao import ProductCategoryDAO
from .orders.employee_position_dao import EmployeePositionDAO
from .orders.manufacturing_company_dao import ManufacturingCompanyDAO
from .orders.delivery_type_dao import DeliveryTypeDAO
from .orders.client_dao import ClientDAO
from .orders.employee_dao import EmployeeDAO
from .orders.product_dao import ProductDAO
from .orders.shop_product_receiving_dao import ShopProductReceivingDAO
from .orders.client_product_delivery_dao import ClientProductDeliveryDAO

shop_dao = ShopDAO()
product_category_dao = ProductCategoryDAO()
employee_position_dao = EmployeePositionDAO()
manufacturing_company_dao = ManufacturingCompanyDAO()
delivery_type_dao = DeliveryTypeDAO()
client_dao = ClientDAO()
employee_dao = EmployeeDAO()
product_dao = ProductDAO()
shop_product_receiving_dao = ShopProductReceivingDAO()
client_product_delivery_dao = ClientProductDeliveryDAO()
