def create_order(orders_dict, order_id, client_id, product_id, quantity, clients_dict, products_dict):
    if order_id in orders_dict:
        return orders_dict, "Order already exists"

    if client_id not in clients_dict:
        return orders_dict, "Client does not exist"

    if product_id not in products_dict:
        return orders_dict, "Product does not exist"

    unit_price = products_dict[product_id][1]
    total = unit_price * quantity

    orders_dict[order_id] = {
        "client": client_id,
        "product": product_id,
        "quantity": quantity,
        "total": total
    }

    return orders_dict, "Order created successfully"


def view_orders(orders_dict, clients_dict, products_dict):
    if not orders_dict:
        return "No orders registered"

    result = "\n--- ORDER LIST ---\n"

    for order_id in orders_dict:
        order = orders_dict[order_id]

        client = clients_dict[order["client"]]
        client_name = client["first_name"] + " " + client["last_name"]
        product_name = products_dict[order["product"]][0]

        result += (
            f"Order ID: {order_id} | "
            f"Client: {client_name} | "
            f"Product: {product_name} | "
            f"Qty: {order['quantity']} | "
            f"Total: {order['total']}\n"
        )

    return result


def calculate_income(orders_dict):
    total_income = 0

    for order_id in orders_dict:
        total_income += orders_dict[order_id]["total"]

    return total_income