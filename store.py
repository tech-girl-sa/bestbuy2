import copy
from typing import List

from product import Product



class Store:
    """
    Represents a Stores and manage all actions that can be performed on it.
    adding and removing products from it, showing all available products and making orders.
    A Store is composed of a list of Product instances.
    """

    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        if product in self.products:
            similar_product = list(filter(lambda x: x.name == product.name and x.price == product.price,
                                          self.products))[0]
            similar_product.quantity = similar_product.quantity+product.quantity
        else:
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

    def __contains__(self, product:Product):
        similar_products = list(filter( lambda x: x.name == product.name and x.price == product.price , self.products))
        return len(similar_products) > 0

    def __add__(self, other_store):
        new_store = copy.deepcopy(self)
        for product in other_store.products:
            new_store.add_product(product)
        return new_store


