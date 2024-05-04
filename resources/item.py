import uuid

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found.")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(ItemSchema)
    def put(self, item_data, item_id):
        try:
            item = items[item_id]
            item.update(item_data)
            return item
        except KeyError:
            abort(404, message="Item not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"Message": f"Item {item_id} deleted."}
        except KeyError:
            abort(404, message="Item not found.")


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(ItemSchema(many=True))
    def get(self):
        return items.values()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        # Uniqueness validation
        for item in items.values():
            if (
                item["name"] == item_data["name"]
                and item["store_id"] == item_data["store_id"]
            ):
                abort(400, message="Item already exists.")

        item_id = uuid.uuid4().hex
        item = {**item_data, "item_id": item_id}
        items[item_id] = item
        return item
