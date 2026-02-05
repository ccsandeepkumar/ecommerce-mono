from services.catalog.product import get_product_price
import time

def test_product_price():
    assert get_product_price(1) == 100



