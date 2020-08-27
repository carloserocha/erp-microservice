from nameko.rpc import RpcProxy
from nameko.web.handlers import http
from werkzeug import Response
import json

from service.exceptions import ProductNotFound


class GatewayService:
    name = 'service_gateway'

    product_rpc = RpcProxy('service_product')

    @http('GET', '/product/<int:productId>', expected_exceptions=ProductNotFound)
    def get_product(self, request, productId):
        try:
            product = self.product_rpc.get_product(productId)
            return json.dumps({'product': product})
        except ProductNotFound:
            return Response(
                status=404,
                response=json.dumps({'error': 'not found'}),
                mimetype='application/json'
            )

    @http('POST', '/product')
    def create_product(self, request):
        product = self.product_rpc.create_product(request)
        return json.dumps({'product': product})

    @http('GET', '/warehouse/<int:warehouseId>')
    def get_warehouse(self, request, warehouseId):
        warehouse = self.product_rpc.get_warehouse(warehouseId)
        return json.dumps({'warehouse': warehouse})
    
    @http('POST', '/warehouse')
    def create_warehouse(self, request):
        warehouse = self.product_rpc.create_warehouse(request)
        return json.dumps({'warehouse': warehouse})
