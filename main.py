from management.product_handler import menu_report, add_product_extra
from menu import products

if __name__ == "__main__":
    required_keys = ("description", "price", "rating", "title", "type")
    # Produto com chaves extras
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "extra_key_1": "extra_value_1",
        "extra_key_2": "extra_value_2"
    }
    print(add_product_extra(products, *required_keys, **new_product))
    ...
