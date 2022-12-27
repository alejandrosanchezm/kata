# -*- coding: utf-8 -*-
import unittest

from gilded_rose import *


class GildedRoseTest(unittest.TestCase):

    def test_foo(self):
        items = [CommonItem("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_Brie(self):
        items = [BrieCheeseItem("BrieCheese", sell_in=2, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(1, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(2, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(3, items[0].quality)

    def test_Sulfuras(self):

        # Comprobamos que nunca varía sell_in ni quality
        items = [SulfurasItem("Sulfuras", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(80, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(80, items[0].quality)

    def test_Backstage(self):
        items = [BackstageItem("Backstage", sell_in=15, quality=20)]
        gilded_rose = GildedRose(items)

        # Primeras dos iteraciones: Aumenta 1 la calidad por cada paso
        gilded_rose.update_quality()
        self.assertEquals(14, items[0].sell_in)
        self.assertEquals(21, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(13, items[0].sell_in)
        self.assertEquals(22, items[0].quality)

        # segundo caso: Para 11, aumenta el valor 1, para 10, aumenta el valor 2
        items = [BackstageItem("Backstage", sell_in=12, quality=13)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(11, items[0].sell_in)
        self.assertEquals(14, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(10, items[0].sell_in)
        self.assertEquals(16, items[0].quality)

        # tercer caso: Para 6, aumenta el valor 2, para 5, aumenta el valor 3
        items = [BackstageItem("Backstage", sell_in=7, quality=32)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(6, items[0].sell_in)
        self.assertEquals(34, items[0].quality) 

        gilded_rose.update_quality()
        self.assertEquals(5, items[0].sell_in)
        self.assertEquals(37, items[0].quality) 

        # cuarto caso: Para 11, aumenta el valor 1, para 10, aumenta el valor 2
        items = [BackstageItem("Backstage", sell_in=2, quality=46)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(49, items[0].quality)

        # Con este caso, comprobamos que el valor no aumenta de 50
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(50, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)
     
    def test_Conjured(self):

        # Comprobamos que nunca varía sell_in ni quality
        items = [ConjuredItem("Conjured", sell_in=3, quality=6)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEquals(2, items[0].sell_in)
        self.assertEquals(4, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(2, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(0, items[0].quality) 

        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(-2, items[0].quality)         

if __name__ == '__main__':
    unittest.main()
