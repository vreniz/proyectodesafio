# =========================================
# CUSTOMER ORDER MANAGEMENT SYSTEM
# =========================================

# In-memory databases (no lists allowed)
clients = {}
products = {}
orders = {}

# =========================================
# CLIENT FUNCTIONS
# =========================================
def register_client(clients_dict, client_id, first_name, last_name, email):
    """
    Register a new client
    """
    if client_id in clients_dict:
        return clients_dict, "Client already exists"

    clients_dict[client_id] = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }

    return clients_dict, "Client registered successfully"

# =========================================
# PRODUCT FUNCTIONS
# =========================================
def register_product(products_dict, product_id, name, price):
    """
    Register a new product (stored as tuple)
    """
    if product_id in products_dict:
        return products_dict, "Product already exists"

    products_dict[product_id] = (name, price)
    return products_dict, "Product registered successfully"


# =========================================
# ORDER FUNCTIONS
# =========================================
def create_order(orders_dict, order_id, client_id, product_id, quantity, clients_dict, products_dict):
    """
    Create a new order
    """
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

def view_clients(clients_dict):
    if not clients_dict:
        return "No clients registered"

    result = "\n--- CLIENT LIST ---\n"

    for client_id in clients_dict:
        client = clients_dict[client_id]
        full_name = client["first_name"] + " " + client["last_name"]

        result += f"ID: {client_id} | Name: {full_name} | Email: {client['email']}\n"

    return result


def view_products(products_dict):
    """
    Return formatted string of all products
    """
    if not products_dict:
        return "No products registered"

    result = "\n--- PRODUCT LIST ---\n"

    for product_id in products_dict:
        product = products_dict[product_id]
        result += f"ID: {product_id} | Name: {product[0]} | Price: {product[1]}\n"

    return result


def view_orders(orders_dict, clients_dict, products_dict):
    """
    Return formatted string of all orders
    """
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
    """
    Calculate total income of the day
    """
    total_income = 0

    for order_id in orders_dict:
        total_income += orders_dict[order_id]["total"]

    return total_income


def generate_report(orders_dict, clients_dict, products_dict):
    """
    Generate final report
    """
    total_orders = len(orders_dict)
    total_income = calculate_income(orders_dict)

    report = "\n=== FINAL REPORT ===\n"
    report += f"Total Orders: {total_orders}\n"
    report += f"Total Income: {total_income}\n"

    # Orders grouped by client
    report += "\nOrders by Client:\n"
    for client_id in clients_dict:
        client_name = clients_dict[client_id]["name"]
        report += f"{client_name}: "

        count = 0
        for order_id in orders_dict:
            if orders_dict[order_id]["client"] == client_id:
                count += 1

        report += f"{count} orders\n"

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


# =========================================
# MENU SYSTEM
# =========================================
def menu():
    """
    Display menu and handle user interaction
    """
    running = True

    while running:
        print("\n===== MENU =====")
        print("1. Register Client")
        print("2. Register Product")
        print("3. Create Order")
        print("4. View Orders")
        print("5. Calculate Income")
        print("6. Generate Report")
        print("7. View Clients")
        print("8. View Products")
        print("9. Exit")

        option = input("Select an option: ").strip()

        # REGISTER CLIENT
        if option == "1":
            try:
                client_id = int(input("Client ID: "))
                name = input("First Name: ")
                last_name = input("Last Name: ")
                email = input("Email: ")

                global clients
                clients, msg = register_client(clients, client_id, first_name, last_name, email)
                print(msg)

            except:
                print("Invalid input")

        # REGISTER PRODUCT
        elif option == "2":
            try:
                product_id = int(input("Product ID: "))
                name = input("Name: ")
                price = float(input("Price: "))

                global products
                products, msg = register_product(products, product_id, name, price)
                print(msg)

            except:
                print("Invalid input")

        # CREATE ORDER
        elif option == "3":
            try:
                order_id = int(input("Order ID: "))
                client_id = int(input("Client ID: "))
                product_id = int(input("Product ID: "))
                quantity = int(input("Quantity: "))

                global orders
                orders, msg = create_order(
                    orders,
                    order_id,
                    client_id,
                    product_id,
                    quantity,
                    clients,
                    products
                )
                print(msg)

            except:
                print("Invalid input")

        # VIEW ORDERS
        elif option == "4":
            print(view_orders(orders, clients, products))
        # VIEW CLIENTS
        elif option == "7":
             print(view_clients(clients))

        # VIEW PRODUCTS
        elif option == "8":
            print(view_products(products))

        # CALCULATE INCOME
        elif option == "5":
            print(f"Total Income: {calculate_income(orders)}")

        # REPORT
        elif option == "6":
            print(generate_report(orders, clients, products))

        # EXIT
        elif option == "9":
            print("Goodbye!")
            running = False

        else:
            print("Invalid option")


# =========================================
# MAIN
# =========================================
if __name__ == "__main__":
    menu()
    
    
  