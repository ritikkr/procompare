"""Class to represent product details."""

class Product:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating
        
    def __str__(self):
        return "Name: %s, Price: %s, Rating: %s" % (self.name, self.price, self.rating)
