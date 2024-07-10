from item import Item

class Update:  
    @staticmethod
    def update_sufuras():
        pass

    @staticmethod  
    def update_aged_brie(item):
        Item.update_sell_in(item)
        Item.increment_quality(item, 1)
    
    @staticmethod
    def update_quality_passes(item):
        Item.update_sell_in(item)
        if item.sell_in < 0:
            item.quality = 0    
        elif item.sell_in <= 5:
            Item.increment_quality(item, 3)
        elif item.sell_in <= 10:
            Item.increment_quality(item, 2)
        else:
            Item.decrement_quality(item, 1)

    @staticmethod
    def update_quality_conjured(item):
        Item.update_sell_in(item)
        Item.decrement_quality(item, 2)
    
    @staticmethod
    def update_quality_normal(item):
        Item.update_sell_in(item)
        if item.sell_in < 0:
            Item.decrement_quality(item, 2)
        else:
            Item.decrement_quality(item, 1)