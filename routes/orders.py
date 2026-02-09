from flask import Blueprint, request
from services.order_service import get_order

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/order/<oid>")
def order(oid):
    return get_order(oid, request.headers.get("X-User-ID"))
