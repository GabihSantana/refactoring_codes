# Teste
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo_normal_prod(self):
        items = [Item("foo", 4, 5)] 
        gilded_rose = GildedRose(items)
        gilded_rose.update_products_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_products_quality()
        self.assertEqual(1, items[0].quality)

    def test_backstage_pass(self):
        items = [Item("Backstage passes to a concert", 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_products_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_products_quality()
        self.assertEqual(80, items[0].quality)

    def test_conjured(self):
        items = [Item("Conjured cake", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_products_quality()
        self.assertEqual(8, items[0].quality)
        self.assertEqual(4, items[0].sell_in)
    
    def test_quality_pass_after_sellin(self):
        items = [Item("Backstage passes to a concert", -1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_products_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)
        
if __name__ == '__main__':
    unittest.main()
