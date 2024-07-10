class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
    
    @staticmethod
    def update_sell_in(item):
        item.sell_in -= 1
    
    @staticmethod
    def increment_quality(item, value):
        if item.quality + value <= 50:
            item.quality += value
        else:
            item.quality = 50
    
    @staticmethod
    def decrement_quality(item, value):
        if item.quality - value > 0:
            item.quality -= value
        else:
            item.quality = 0
