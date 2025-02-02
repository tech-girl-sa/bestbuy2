from typing import List

from product import Product



class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        quantities = [product.quantity for product in self.products]
        return sum(quantities)

    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            price = product.buy(quantity)
            total_price += price
        return total_price