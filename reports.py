from orders import calculate_income

def generate_report(orders_dict, clients_dict, products_dict):
    total_orders = len(orders_dict)
    total_income = calculate_income(orders_dict)

    total_income_str = f"${total_income:,.2f}"

    report = "\n=== FINAL REPORT ===\n"
    report += f"Total Orders: {total_orders}\n"
    report += f"Total Income: {total_income_str}\n"

    # =========================================
    # Orders by client (grouped with detail)
    # =========================================
    report += "\n--- Orders by Client ---\n"

    for client_id in clients_dict:
        client = clients_dict[client_id]
        full_name = client["first_name"] + " " + client["last_name"]

        # count orders
        count = 0
        for order_id in orders_dict:
            if orders_dict[order_id]["client"] == client_id:
                count += 1

        order_text = "order" if count == 1 else "orders"

        report += f"\n[Client ID: {client_id}] {full_name}: {count} {order_text}\n"

        # show each order
        has_orders = False

        for order_id in orders_dict:
            order = orders_dict[order_id]

            if order["client"] == client_id:
                has_orders = True

                product_name = products_dict[order["product"]][0]

                report += (
                    f"   - Order ID: {order_id} | "
                    f"Product: {product_name} | "
                    f"Qty: {order['quantity']} | "
                    f"Total: ${order['total']}\n"
                )

        if not has_orders:
            report += "   (No orders)\n"

    # =========================================
    # Products sold
    # =========================================
    report += "\n--- Products Sold ---\n"

    for product_id in products_dict:
        product_name = products_dict[product_id][0].title()
        total_qty = 0

        for order_id in orders_dict:
            if orders_dict[order_id]["product"] == product_id:
                total_qty += orders_dict[order_id]["quantity"]

        unit_text = "unit" if total_qty == 1 else "units"

        report += f"[Product ID: {product_id}] {product_name}: {total_qty} {unit_text}\n"

    return report