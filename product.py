
class Product:
    """Represent the product scraped from websites."""
    def __init__(self, name, price, rating, link=""):
        self.name = name
        self.price = price
        self.rating = rating
        self.link = link

    def __str__(self):
        return "Name: %s, Price: %s, Rating: %s" % (self.name, self.price, self.rating)