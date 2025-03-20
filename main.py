from product import Product, LimitedProduct, NonStockedProduct
from promotion import SecondHalfPrice, ThirdOneFree, PercentDiscount
from store import Store


product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250),
                 NonStockedProduct("Windows License", price=125),
                 LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = SecondHalfPrice("Second Half price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent = PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].promotion = second_half_price
product_list[1].promotion = third_one_free
product_list[3].promotion = thirty_percent

best_buy = Store(product_list)

def get_user_input():
    menu = """
            Store Menu
            ----------
       1. List all products in store
       2. Show total amount in store
       3. Make an order
       4. Quit
       """
    while True:
        try:
            print(menu)
            user_choice = int(input("Please choose a number: "))
            if user_choice > 4 or user_choice < 1:
                raise ValueError
            return user_choice
        except ValueError:
            print("Error with your choice! Try again!")


def list_products(store:Store):
    print("------")
    for index, product in enumerate(store.get_all_products()):
        print(f"{index+1}. {product}")
    print("------")

def show_total_amount(store):
    print(f"\nTotal of {store.get_total_quantity()} items in store\n")

def get_user_product(products):
    while True:
        try:
            print("When you want to finish order, enter empty text.")
            user_choice = input("Which product # do you want: ")
            if user_choice == "":
                return
            user_choice = int(user_choice)
            if user_choice not in range(1, len(products) + 1):
                raise ValueError
            return products[user_choice-1]
        except ValueError:
            print("Please enter a valid product index")

def get_product_quantity(product:Product):
    while True:
        try:
            user_choice = input("What amount do you want? ")
            if user_choice == "":
                return
            user_choice = int(user_choice)
            if not isinstance(product, NonStockedProduct) and user_choice not in range(0, product.quantity + 1):
                raise ValueError("We don't have the entered quantity")
            if isinstance(product, LimitedProduct) and user_choice > product.maximum:
                raise ValueError(f"his product is limited. cannot buy more than {product.maximum} times in an order")
            return user_choice
        except ValueError as e:
            print(e)


def get_user_order(products):
    shopping_dict = {}
    while True:
        product = get_user_product(products)
        if not product:
            break
        amount = get_product_quantity(product)
        if not amount:
            break
        if product not in shopping_dict:
            shopping_dict[product] = amount
        else:
            amount = shopping_dict[product] + amount
            if isinstance(product, LimitedProduct) and amount > product.maximum:
                print(f"his product is limited. cannot buy more than {product.maximum} times in an order")
                continue
            shopping_dict[product] = amount
        print("\nProduct added to the list!\n")
    shopping_list = shopping_dict.items()
    return shopping_list


def order(store):
    list_products(store)
    shopping_list = get_user_order(store.get_all_products())
    price = store.order(shopping_list)
    print("********")
    print(f"Order made! Total payment: ${price}")


def start(store:Store):
    while True:
        user_input = get_user_input()
        dispatcher = {
           1: list_products,
           2: show_total_amount,
           3: order,
        }
        if user_input == 4:
            break
        dispatcher[user_input](store)



def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose)
    print(mac)

    bose.quantity = 1000
    print(bose)
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]
    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))
    # setup initial stock of inventory
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel = LimitedProduct("Google Pixel 7", price=500, quantity=250, maximum=1)

    best_buy = Store([mac, bose])
    try:
        mac.price = -100
    except Exception:
        print("error")# Should give error
    print(mac)  # Should print `MacBook Air M2, Price: $1450 Quantity:100`
    print(mac > bose)  # Should print True
    print(mac in best_buy)  # Should print True
    print(pixel in best_buy)  # Should print False


if __name__ == '__main__':
    start(best_buy)



