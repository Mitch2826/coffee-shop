class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        
        self.price = price
        self.customer = customer
        self.coffee = coffee
        #add this order to the list of all orders
        Order.all_orders.append(self)
        
    def get_price(self):
        return self.price
    
    def set_price(self, value):
        #ensure price is settable once
        if hasattr(self, 'price'):
            raise AttributeError("Price cannot be changed after order creation!")
        #validate value is a float
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be a number!")
        #ensure price range is between 1.0 and 10.0
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0!")
        #convert value to float and store it
        self.price = float(value)
        
    price = property(get_price, set_price)
    
    def get_customer(self):
        #get customer who's placed this order
        return self.customer
    #read only
    customer = property(get_customer)
    
    def get_coffee(self):
        #get coffee that was ordered
        return self.coffee
    #read only
    coffee = property(get_coffee)