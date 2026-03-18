def register_product(products_dict, product_id, name, price):
    if product_id in products_dict:
        return products_dict, "Product already exists"

    products_dict[product_id] = (name, price)
    return products_dict, "Product registered successfully"


def view_products(products_dict):
    if not products_dict:
        return "No products registered"

    result = "\n--- PRODUCT LIST ---\n"

    for product_id in products_dict:
        product = products_dict[product_id]
        result += f"ID: {product_id} | Name: {product[0]} | Price: $ {product[1]}\n"

    return result