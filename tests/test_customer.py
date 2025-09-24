import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("A" * 16)
    c = Customer("Alice")
    assert c.name == "Alice"
    c.name = "Bob"
    assert c.name == "Bob"

def test_customer_orders_and_coffees():
    c = Customer("Alice")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Mocha")
    o1 = c.create_order(coffee1, 3.0)
    o2 = c.create_order(coffee2, 4.0)
    assert o1 in c.orders()
    assert o2 in c.orders()
    assert coffee1 in c.coffees()
    assert coffee2 in c.coffees()