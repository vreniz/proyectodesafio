from clients import register_client, view_clients
from products import register_product, view_products
from orders import create_order, view_orders, calculate_income
from reports import generate_report
from validationfunct import input_int, input_float,input_string,input_name

clients = {}
products = {}
orders = {}

# =========================================
# VALIDATION FUNCTIONS
# =========================================
"""
def input_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Invalid input. Please enter a valid integer.")
        
def input_float(prompt):
    while True:
        value = input(prompt).strip()

        # Replace comma with dot
        value = value.replace(",", ".")

        # ❌ validar que no haya más de un punto
        if value.count(".") > 1:
            print("Invalid format. Too many decimal points.")
            continue

        # ❌ validar que no esté vacío o solo punto
        if value == "." or value == "":
            print("Invalid number.")
            continue

        # ❌ validar que solo tenga números y punto
        valid = True
        for char in value:
            if not (char.isdigit() or char == "."):
                valid = False

        if not valid:
            print("Invalid input. Only numbers allowed.")
            continue

        # convertir a float
        number = float(value)

        # ❌ validar positivo
        if number <= 0:
            print("Value must be greater than 0.")
            continue

        return number

def input_string(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("This field cannot be empty.")


def input_name(prompt):
    
    #Only allows letters and spaces
    
    while True:
        value = input(prompt).strip()

        if value.replace(" ", "").isalpha():
            return value.title()
        else:
            print("Invalid name. Only letters are allowed.")
"""

# =========================================
# CONTINUE FUNCTION
# =========================================

def ask_to_continue():
    answer = input("\nReturn to menu? (yes/no): ").strip().lower()

    if answer == "no":
        print("Goodbye!")
        return False
    return True


# =========================================
# MENU
# =========================================

def menu():
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
            client_id = input_int("Client ID: ")
            first_name = input_name("First Name: ")
            last_name = input_name("Last Name: ")
            email = input_string("Email: ")

            global clients
            clients, msg = register_client(clients, client_id, first_name, last_name, email)
            print(msg)

            running = ask_to_continue()

        # REGISTER PRODUCT
        elif option == "2":
            product_id = input_int("Product ID: ")
            name = input_string("Name: ")
            price = input_float("Price: $ ")

            global products
            products, msg = register_product(products, product_id, name, price)
            print(msg)

            running = ask_to_continue()

        # CREATE ORDER
        elif option == "3":
            order_id = input_int("Order ID: ")
            client_id = input_int("Client ID: ")
            product_id = input_int("Product ID: ")
            quantity = input_int("Quantity: ")

            global orders
            orders, msg = create_order(
                orders, order_id, client_id, product_id, quantity, clients, products
            )
            print(msg)

            running = ask_to_continue()

        # VIEW ORDERS
        elif option == "4":
            print(view_orders(orders, clients, products))
            running = ask_to_continue()

        # CALCULATE INCOME
        elif option == "5":
            print(f"Total Income: {calculate_income(orders)}")
            running = ask_to_continue()

        # REPORT
        elif option == "6":
            print(generate_report(orders, clients, products))
            running = ask_to_continue()

        # VIEW CLIENTS
        elif option == "7":
            print(view_clients(clients))
            running = ask_to_continue()

        # VIEW PRODUCTS
        elif option == "8":
            print(view_products(products))
            running = ask_to_continue()

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