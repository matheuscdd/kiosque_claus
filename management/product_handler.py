from menu import products


def get_product_by_id(identifier: int) -> dict:
    if type(identifier) != int:
        raise TypeError("product id must be an int")
    result = list(filter(lambda product: product["_id"] == identifier, products))
    return result[0] if len(result) else dict()


def get_products_by_type(kind: str) -> list:
    if type(kind) != str:
        raise TypeError("product type must be a str")
    result = list(filter(lambda product: product["type"] == kind, products))
    return result if len(result) else list()


def add_product(menu: list[dict], **kwargs) -> dict:
    curr_id = menu[len(menu)-1]["_id"] + 1 if len(menu) else 1
    kwargs["_id"] = curr_id
    menu.append(kwargs)
    return kwargs


def menu_report():
    product_count = len(products)
    average_price = round(sum(product["price"] for product in products) / product_count, 2)

    all_types = set(product["type"] for product in products)
    most_common_type: str
    many_by_type = 0
    for curr_type in all_types:
        products_filter = list(filter(lambda product: product["type"] == curr_type, products))
        if len(products_filter) > many_by_type:
            many_by_type = len(products_filter)
            most_common_type = curr_type
    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"

