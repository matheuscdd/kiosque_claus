from menu import products


def get_product_by_id(identifier: int):
    result = list(filter(lambda product: product["_id"] == identifier, products))
    return result[0] if len(result) else dict()


def get_products_by_type(kind: str):
    result = list(filter(lambda product: product["type"] == kind, products))
    return result if len(result) else list()

