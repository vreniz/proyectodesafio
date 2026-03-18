from orders import calculate_income

def generate_report(orders_dict, clients_dict, products_dict):
    total_orders = len(orders_dict)
    total_income = calculate_income(orders_dict)

    report = "\n=== FINAL REPORT ===\n"
    report += f"Total Orders: {total_orders}\n"
    report += f"Total Income: {total_income}\n"

    # Orders by client
    report += "\nOrders by Client:\n"
    for client_id in clients_dict:
        client = clients_dict[client_id]
        full_name = client["first_name"] + " " + client["last_name"]

        count = 0
        for order_id in orders_dict:
            if orders_dict[order_id]["client"] == client_id:
                count += 1

        report += f"{full_name}: {count} orders\n"

    # Products sold
    report += "\nProducts Sold:\n"
    for product_id in products_dict:
        product_name = products_dict[product_id][0]
        total_qty = 0

        for order_id in orders_dict:
            if orders_dict[order_id]["product"] == product_id:
                total_qty += orders_dict[order_id]["quantity"]

        report += f"{product_name}: {total_qty} units\n"

    return report