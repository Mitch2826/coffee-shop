class Coffee:
    def __init__(self, name):
        self.name = name
        
    #get the coffee's name
    @property    
    def name(self):
        return self._name
    
    #set the coffee's name
    @name.setter
    def name(self, value):
        #check if name is already set
        if hasattr(self, '_name'):
            raise AttributeError("Coffee name cannot be changed after creation!")
        #ensure name is a string
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string!")
        #ensure name is at least 3 characters long
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long!")
        
        self._name = value
    
    
    def orders(self):
        #get all orders for this coffee
        from order import Order
        #filter through all orders to find those for this coffee
        coffee_orders = []
        for order in Order.all_orders:
            if order.coffee == self:
                coffee_orders.append(order)
                
        return coffee_orders
    
    #get each customer who ordered this coffee
    def  customers(self):
        my_orders = self.orders()
        #extract customers from orders
        unique_customers = []
        for order in my_orders:
            customer = order.customer
            #only add if we haven't seen this customer before
            if customer not in unique_customers:
                unique_customers.append(customer)         
        return unique_customers
    
    #get total number of orders for this coffee
    def num_orders(self):
        return len(self.orders())
    #calculate average price paid for this coffee
    def average_price(self):
        my_orders = self.orders()
        #calculate the sum of all order prices
        total_price = 0
        for order in my_orders:
            total_price += order.price
        #calculate and return the average price
        average = total_price / len(my_orders)
        return average