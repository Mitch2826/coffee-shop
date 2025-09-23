class Customer:
    #new customer
    def __init__(self, name):
        self.name = name
    #get customer's name  
    def get_name(self):
        return self.name
    def set_name(self, value):
        #name must be a string
        if not isinstance(value, str):
            raise TypeError("Name must be a string!")
        #name must range between 1 and 15 characters
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters!")
        
        self.name = value
    name = property(get_name, set_name)
    
    def orders(self):
        #get all orders placed by this customer
        
        from order import Order
        #filter through all orders to find those placed by this customer
        customer_orders = []
        for order in Order.all_orders:
            if order.customer == self:
                customer_orders.append(order)
                
        return customer_orders
    
    #get all coffees ordered by this customer
    def coffees(self):
        my_orders = self.orders()
        
        #extract coffees from orders
        unique_coffees = []
        for order in my_orders:
            coffee = order.coffee
            #only add if we haven't seen this coffee before
            if coffee not in unique_coffees:
                unique_coffees.append(coffee)
                
        return unique_coffees
    
    def create_order(self, coffee, price):
        from order import Order
        #create and return a new order for this customer
        new_order = Order(self, coffee, price)
        return new_order