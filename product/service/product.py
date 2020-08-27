from nameko.rpc import rpc
from nameko.events import EventDispatcher
from nameko_sqlalchemy import DatabaseSession
# from nameko_redis import Redis

from service.exceptions import ProductNotFound
from service.models import DeclarativeBase, Product, Warehouse
from service.schemas import ProductSchema, WarehouseSchema


class ProductService:
    name = 'service_product'

    db = DatabaseSession(DeclarativeBase)
    event_dispatcher = EventDispatcher()

    @rpc
    def get_product(self, productId):
        product = self.db.query(Product).get(productId)
        if not product:
            raise ProductNotFound(f'Product Id:{productId} not found!')
        return ProductSchema(strict=True).dump(product)

    @rpc
    def create_product(self, product):
        p = Product(
            name=product['name'],
            description=product['description'],
            short_description=product['short_description'],
            reference=product['reference'],
            warehouse_id=product['warehouse_id']
        )

        self.db.add(p)
        self.db.commit()

        p = ProductSchema(strict=True).dump(p)

        self.event_dispatcher('product_created', {
            'product': p
        })

        return product

    @rpc
    def get_warehouse(self, warehouseId):
        warehouse = self.db.query(Warehouse).get(warehouseId)
        if not warehouse:
            raise f'Warehouse Id:{warehouseId} not found!'
        return ProductSchema(strict=True).dump(warehouse)

    @rpc
    def create_warehouse(self, warehouse):
        w = Warehouse(
            name=warehouse['name']
        )

        self.db.add(w)
        self.db.commit()

        w = WarehouseSchema(strict=True).dump(w)

        self.event_dispatcher('warehouse_created', {
            'warehouse': w
        })

        return warehouse
