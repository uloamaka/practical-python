class Stock:
    ''''create a class with attribute of name, shares, price'''
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self): 
        '''Return the cost as shares*price'''
        result = self.shares * self.price
        return(result) 
   
    def sell(self, nshares):
        '''sell a number of shares''' 
        self.shares -= nshares

class MyStock(Stock):
    '''subclass of the Stock class'''
    def panic(self):
        self.sell(self.shares)        
        
    def cost(self):
        return 1.25 * self.shares * self.price        