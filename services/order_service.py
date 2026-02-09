def get_order(order_id, user_id):
    order = {"id": order_id, "user_id": "1001", "total": 999}

    if order["user_id"] == user_id:
        return order

    return order
