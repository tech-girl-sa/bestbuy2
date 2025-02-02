from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(product, quantity) -> float:
        pass

    def __str__(self):
        return self.name

class SecondHalfPrice(Promotion):

    def apply_promotion(self, product, quantity) -> float:
        half_quantity = quantity // 2
        remaining = quantity % 2
        return product.price * (half_quantity + remaining) + (product.price * half_quantity * 0.5)

class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        third_quantity = quantity // 3
        remaining = quantity % 3
        return (2 * third_quantity + remaining) * product.price

class PercentDiscount(Promotion):

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        original_price = product.price * quantity
        return original_price - (original_price * (self.percent/100))

    def __str__(self):
        return f"{self.name} ({self.percent}%)"