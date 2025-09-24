import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_price_validation():
    cust = Customer("Alice")
    cof = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(cust, cof, 0.5)
    with pytest.raises(ValueError):
        Order(cust, cof, 15)
    with pytest.raises(ValueError):
        Order(cust, cof, "abc")
    o = Order(cust, cof, 5.0)
    assert o.price == 5.0

def test_order_properties():
    cust = Customer("Bob")
    cof = Coffee("Mocha")
    o = Order(cust, cof, 4.5)
    assert o.customer == cust
    assert o.coffee == cof