# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class CommonItem(Item):

    def update_quality(self):

        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = self.quality - 2 
        else:
            self.quality = self.quality - 1 

class ConjuredItem(Item):

    def update_quality(self):

        self.sell_in = self.sell_in - 1
        self.quality = self.quality - 2    

class BrieCheeseItem(Item):

    def update_quality(self):

        self.sell_in = self.sell_in - 1
        if self.quality < 50:
            self.quality = self.quality + 1

class SulfurasItem(Item):

    def update_quality(self):
        pass

class BackstageItem(Item):

    def update_quality(self):
        self.sell_in = self.sell_in - 1
        if self.quality < 50:
            if self.sell_in >= 11:
                self.quality = self.quality + 1
            if self.sell_in < 11 and self.sell_in >= 6:
                self.quality = self.quality + 2
            if self.sell_in < 6 and self.sell_in >= 0:
                self.quality = self.quality + 3
        if self.quality > 50:
            self.quality = 50
        if self.sell_in < 0:
            self.quality = 0            
