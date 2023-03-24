from menu import products


def calculate_tab(table: list[dict]) -> dict:
    total = 0
    for items in table:
        find_product = list(filter(lambda product: product["_id"] == items["_id"], products))
        total += find_product[0]["price"] * items["amount"]
    return dict(subtotal=f'${round(total, 2)}')

