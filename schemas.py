from enum import unique

from marshmallow import Schema
from marshmallow.fields import Float, Int, List, Nested, Str

# In this context, dump_only=True means that the field is read-only and should
# not be included in the request body. required=True means that the field is
# required in the request body.


class PlainItemSchema(Schema):
    id = Int(dump_only=True)
    name = Str(required=True)
    price = Float(required=True)


class PlainStoreSchema(Schema):
    id = Int(dump_only=True)
    name = Str(required=True)


class PlainTagSchema(Schema):
    id = Int(dump_only=True)
    name = Str(required=True)


class ItemUpdateSchema(Schema):
    name = Str()
    price = Float()
    store_id = Int()


class StoreUpdateSchema(Schema):
    name = Str()


class ItemSchema(PlainItemSchema):
    store_id = Int(required=True, load_only=True)
    store = Nested(PlainStoreSchema(), dump_only=True)
    tags = List(Nested(PlainTagSchema()), dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = List(Nested(PlainItemSchema()), dump_only=True)
    tags = List(Nested(PlainTagSchema()), dump_only=True)


class TagSchema(PlainTagSchema):
    store_id = Int(load_only=True)
    store = Nested(PlainStoreSchema(), dump_only=True)
    items = List(Nested(PlainItemSchema()), dump_only=True)


class ItemsTagsSchema(Schema):
    message = Str()
    item = Nested(ItemSchema())
    tag = Nested(TagSchema())


class UserSchema(Schema):
    id = Int(dump_only=True)
    username = Str(required=True)
    password = Str(required=True, load_only=True)
