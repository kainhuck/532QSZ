#!/usr/bin/env python
# -*- coding: utf-8 -*-
from things import bright, forever

class People(object):
    def __init__(self, name):
        self.sky = bright
        self.heart = []
        self.lover = None
        self.name = name

    def meet(self, people):
        pass

    def feel(self, mood):
        pass

    def wait(self, who, time):
        print("I will wait "+who.name+" "+str(time))

    def love(self, who, time=forever):
        print("I will love "+who.name+" "+str(time))

    def take_care_of(self, who):
        pass

    def hate(self, who):
        pass

    def forgive(self, who):
        pass

    def change(self):
        pass

    def bother(self, who):
        pass

    def scold(self, who):
        pass

    def apology(self):
        pass

    def accompany(self, who):
        pass

class Girl(People):
    def __init__(self, name):
        super(Girl, self).__init__(name)

class Boy(People):
    def __init__(self, name):
        super(Boy, self).__init__(name)
