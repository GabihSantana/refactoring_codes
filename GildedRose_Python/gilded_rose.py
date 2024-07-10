from update import Update
from item import Item

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_products_quality(self):
        for item in self.items:
            if "Sulfuras" in item.name:
                Update.update_sufuras()
            elif item.name == "Aged Brie":
                Update.update_aged_brie(item)
            elif "passes" in item.name:
                Update.update_quality_passes(item)
            elif "Conjured" in item.name:
                Update.update_quality_conjured(item)
            else:
                Update.update_quality_normal(item)