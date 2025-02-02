


class Product:

    def __init__(self, name, price, quantity):
        if not name and type(name) != str:
            raise ValueError("Invalid name.")
        if  price < 0 or quantity < 0:
            raise ValueError("Invalid price or quantity. Value needs to be positive")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

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

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if  quantity < 0:
            raise ValueError("Invalid quantity. Value needs to be positive")
        if quantity > self.quantity:
            raise ValueError("We don't have the entered quantity in stock.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return quantity * self.price
