from marshmallow import Schema, fields

# In this context, dump_only=True means that the field is read-only and should not be included in the request body.
# required=True means that the field is required in the request body.


class ItemSchema(Schema):
    item_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Str()


class StoreSchema(Schema):
    store_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class StoreUpdateSchema(Schema):
    name = fields.Str()
