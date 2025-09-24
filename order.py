class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        #validate value is a float
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number!")
        #ensure price range is between 1.0 and 10.0
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0!")
        
        self._price = float(price)
        self._customer = customer
        self._coffee = coffee
        #add this order to the list of all orders
        Order.all_orders.append(self)
        

    @property    
    def price(self):
        return self._price
    
    @property
    #get customer who placed this order
    def customer(self):
        return self._customer
    
    @property
    #get coffee that was ordered
    def coffee(self):
       return self._coffee
       
        
    