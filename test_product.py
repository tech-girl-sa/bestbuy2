from product import Product
import pytest


def test_create_product():
    product = Product("MacBook Air M2", price=10, quantity=100)
    assert isinstance(product, Product)

def test_product_name():
    product = Product("MacBook Air M2", price=10, quantity=100)
    assert product.name == "MacBook Air M2"

def test_product_price():
    product = Product("MacBook Air M2", price=10, quantity=100)
    assert product.price == 10


def test_product_quantity():
    product = Product("MacBook Air M2", price=10, quantity=100)
    assert product.quantity == 100


def test_product_is_active():
    product = Product("MacBook Air M2", price=10, quantity=100)
    assert product.is_active()


def test_product_empty_name():
    try:
        product = Product("", price=10, quantity=100)
        assert False
    except ValueError:
        assert True

def test_product_negative_quantity():
    try:
        product = Product("MacBook Air M2", price=10, quantity=-100)
        assert False
    except ValueError:
        assert True

def test_product_negative_price():
    try:
        product = Product("MacBook Air M2", price=-10, quantity=100)
        assert False
    except ValueError:
        assert True

def test_product_0_quantity():
    product = Product("MacBook Air M2", price=10, quantity=0)
    assert not product.is_active()

def test_buy():
    product = Product("MacBook Air M2", price=10, quantity=100)
    product.buy(50)
    assert product.quantity == 50
    product.buy(50)
    assert product.quantity == 0
    assert not product.is_active()

def test_buy_too_much():
    try:
        product = Product("MacBook Air M2", price=10, quantity=100)
        product.buy(101)
        assert False
    except ValueError:
        assert True


pytest.main()