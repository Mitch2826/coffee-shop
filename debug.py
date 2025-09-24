from customer import Customer
from coffee import Coffee
from order import Order
import ipdb

#create sample customers
mitch = Customer("Mitchelle")
frost = Customer("Frost")
#create sample coffees
latte = Coffee("Iced latte")
espresso = Coffee("Espresso")
black = Coffee("Black coffee")
#create orders
order1 = mitch.create_order(latte, 3.5)
order2 = mitch.create_order(black, 4.0)
order3 = frost.create_order(espresso, 6.5)

ipdb.set_trace()