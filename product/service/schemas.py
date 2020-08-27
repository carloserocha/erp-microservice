from marshmallow import Schema, fields

class ProductSchema(Schema):
    sku = fields.Int(required=True)
    description = fields.Str(required=True)        
    short_description = fields.Str(required=True)
    reference = fields.Str(required=True)
    warehouse_id = fields.Int(required=True)

class WarehouseSchema(Schema):
    id = fields.Int(required=True)
    products = fields.Nested(ProductSchema, many=True)