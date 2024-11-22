from .orders.shop_service import ShopService
from .orders.product_category_service import ProductCategoryService
from .orders.employee_position_service import EmployeePositionService
from .orders.manufacturing_company_service import ManufacturingCompanyService
from .orders.delivery_type_service import DeliveryTypeService
from .orders.client_service import ClientService
from .orders.employee_service import EmployeeService
from .orders.product_service import ProductService
from .orders.shop_product_receiving_service import ShopProductReceivingService
from .orders.client_product_delivery_service import ClientProductDeliveryService

shop_service = ShopService()
product_category_service = ProductCategoryService()
employee_position_service = EmployeePositionService()
manufacturing_company_service= ManufacturingCompanyService()
delivery_type_service = DeliveryTypeService()
client_service = ClientService()
employee_service = EmployeeService()
product_service = ProductService()
shop_product_receiving_service = ShopProductReceivingService()
client_product_delivery_service = ClientProductDeliveryService()