class InventoryItem:

    def __init__(self, name, quantity, minimum_stock):
        self.name = name
        self.quantity = quantity
        self.minimum_stock = minimum_stock

    def is_low_stock(self):
        return self.quantity <= self.minimum_stock