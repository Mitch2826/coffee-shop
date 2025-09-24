import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("A")
    c = Coffee("Latte")
    assert c.name == "Latte"
    with pytest.raises(AttributeError):
        c.name = "Mocha"

def test_coffee_orders_and_customers():
    coffee = Coffee("Espresso")
    cust1 = Customer("Alice")
    cust2 = Customer("Bob")
    o1 = cust1.create_order(coffee, 3.0)
    o2 = cust2.create_order(coffee, 4.0)
    assert o1 in coffee.orders()
    assert o2 in coffee.orders()
    assert cust1 in coffee.customers()
    assert cust2 in coffee.customers()

def test_coffee_aggregate_methods():
    coffee = Coffee("Mocha")
    cust1 = Customer("Alice")
    cust2 = Customer("Bob")
    cust1.create_order(coffee, 5.0)
    cust2.create_order(coffee, 7.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 6.0