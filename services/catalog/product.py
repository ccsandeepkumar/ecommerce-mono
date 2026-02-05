import time
def get_product_price(product_id):
    products = {
        1: 100,
        2: 200
    }
    return products.get(product_id, 0)

