from customer import Customer
from coffee import Coffee
from order import Order

def main():
    # create customers
    mitch = Customer("Mitchelle")
    frost = Customer("Frost")
    agnes = Customer("Agnes")
    # Create coffees
    latte = Coffee("Iced latte")
    espresso = Coffee("Espresso")
    black = Coffee("Black coffee")
    

    # Create orders
    order1 = mitch.create_order(latte, 3.5)
    order2 = mitch.create_order(black, 4.0)
    order3 = frost.create_order(espresso, 6.5)
    order4 = agnes.create_order(latte, 3.5)
    
    print(f"{mitch.name} ordered {[coffee.name for coffee in mitch.coffees()]}")
    print(f"{frost.name} ordered {[coffee.name for coffee in frost.coffees()]}")
    print(f"{latte.name} has {latte.num_orders()} orders, average price: {latte.average_price()}")
    print(f"{espresso.name} has {espresso.num_orders()} orders, average price: {espresso.average_price()}")
    print(f"{black.name} has {black.num_orders()} orders, average price: {black.average_price()}")
    
if __name__ == "__main__":
    main()