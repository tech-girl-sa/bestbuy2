from promotion import PercentDiscount, Promotion


class Product:

    def __init__(self, name, price, quantity, promotion=PercentDiscount("No promotion",0)):
        if (not name) or type(name) != str:
            raise ValueError("Invalid name.")
        if  price < 0 or quantity < 0:
            raise ValueError("Invalid price or quantity. Value needs to be positive")
        self.name = name
        self.price = price
        self.promotion = promotion
        self.quantity = quantity
        self.active = True
        if self.quantity == 0:
            self.deactivate()

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        if not isinstance(promotion,Promotion):
            raise ValueError("Wrong promotion type")
        self.promotion = promotion

    def get_quantity(self)  -> float :
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    def is_active(self) -> bool:
        return self.active

    def __str__(self):
        display = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        if getattr(self.promotion, "percent", "") != 0:
            return f"{display}, Promotion: {self.promotion}"
        return display

    def buy(self, quantity) -> float:
        if  quantity < 0:
            raise ValueError("Invalid quantity. Value needs to be positive")
        if not isinstance(self, NonStockedProduct) and quantity > self.quantity:
            raise ValueError("We don't have the entered quantity in stock.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.promotion.apply_promotion(self, quantity)


class NonStockedProduct(Product):
    def __init__(self, name, price, quantity=0):
        super().__init__(name,price,quantity)
        self.activate()

    def __str__(self) -> str:
        display = f"{self.name}, Price: {self.price}"
        if getattr(self.promotion, "percent", "") != 0:
            return f"{display}, Promotion: {self.promotion}"
        return display

    def buy(self, quantity) -> float:
        purchase = super().buy(quantity)
        self.quantity = 0
        self.activate()
        return purchase

    def set_quantity(self, quantity=0):
        self.quantity = 0


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name,price,quantity)
        self.maximum = maximum

    def buy(self, quantity) -> float:
        if quantity > self.maximum:
            raise ValueError(f"This product is limited. cannot buy more than {self.maximum} times in an order")
        purchase = super().buy(quantity)
        return purchase

    def __str__(self) -> str:
        display_message = super().__str__()
        return f"{display_message}, Maximum: {self.maximum}"


