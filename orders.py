class Order:
    def __init__(self) ->None:
        self.items={}

    def add_item(self, item):
        if item in self.items:
            # If The item is already in cart
            self.items[item] += item.quantity
        else:
            self.items[item]=item.quantity  #If item is not in cart

    def remove(self, item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def clear(self):
        self.items={}
