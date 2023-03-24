from menu import products


def get_product_by_id(identifier: int) -> dict:
    result = list(filter(lambda product: product["_id"] == identifier, products))
    return result[0] if len(result) else dict()


def get_products_by_type(kind: str) -> list:
    result = list(filter(lambda product: product["type"] == kind, products))
    return result if len(result) else list()


def add_product(menu: list[dict], **kwargs) -> dict:
    curr_id = menu[len(menu)-1]["_id"] + 1 if len(menu) else 1
    kwargs["_id"] = curr_id
    menu.append(kwargs)
    return kwargs

