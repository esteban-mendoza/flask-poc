import uuid

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items

blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found.")

    def put(self, item_id):
        item_data = request.get_json()

        # Schema validation
        if "name" not in item_data or "price" not in item_data:
            abort(400, message="Missing required fields.")
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
    def get(self):
        return {"items": list(items.values())}

    def post(self):
        item_data = request.get_json()
        # Schema validation
        if (
            "store_id" not in item_data
            or "name" not in item_data
            or "price" not in item_data
        ):
            abort(400, message="Missing required fields.")

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
