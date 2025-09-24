import pytest
from customer import Customer
from coffee import Coffee
from order import Order


def test_order_price_boundary_values():
    cust = Customer("Alice")
    cof = Coffee("Latte")
    o1 = Order(cust, cof, 1.0)
    o2 = Order(cust, cof, 10.0)
    assert o1.price == 1.0
    assert o2.price == 10.0


def test_order_all_orders_tracks_instances():
    cust1 = Customer("Alice")
    cust2 = Customer("Bob")
    cof1 = Coffee("Espresso")
    cof2 = Coffee("Mocha")

    o1 = Order(cust1, cof1, 3.0)
    o2 = Order(cust2, cof2, 4.5)

    assert len(Order.all_orders) == 2
    assert o1 in Order.all_orders and o2 in Order.all_orders


def test_customer_set_invalid_name_raises():
    c = Customer("Alice")
    with pytest.raises(TypeError):
        c.name = 123
    with pytest.raises(ValueError):
        c.name = ""  # too short
    with pytest.raises(ValueError):
        c.name = "A" * 16  # too long


def test_coffee_customers_unique():
    coffee = Coffee("Cappuccino")
    cust = Customer("Eve")
    # Same customer orders the same coffee twice
    Order(cust, coffee, 3.0)
    Order(cust, coffee, 4.0)
    customers = coffee.customers()
    assert customers == [cust]


def test_coffee_orders_specificity():
    coffee_a = Coffee("Flat White")
    coffee_b = Coffee("Americano")
    cust = Customer("Zoe")
    o1 = Order(cust, coffee_a, 3.5)
    Order(cust, coffee_b, 4.0)

    orders_a = coffee_a.orders()
    assert orders_a == [o1]


def test_average_price_zero_orders_raises_zerodivisionerror():
    # Current implementation divides by len(orders) without guard
    coffee = Coffee("Macchiato")
    with pytest.raises(ZeroDivisionError):
        coffee.average_price()


def test_customer_coffees_unique():
    c = Customer("Mia")
    coffee = Coffee("Cortado")
    # Multiple orders for the same coffee
    c.create_order(coffee, 3.0)
    c.create_order(coffee, 3.5)
    coffees = c.coffees()
    assert coffees == [coffee]


def test_create_order_returns_order_and_links():
    c = Customer("Noah")
    coffee = Coffee("Affogato")
    o = c.create_order(coffee, 5.0)
    assert isinstance(o, Order)
    assert o.customer == c
    assert o.coffee == coffee
    assert o in Order.all_orders
