#!/usr/bin/env python
# -*- coding: utf-8 -*-
# _author_: KainHuck

from world import Girl, Boy
from feelings import *
from things import *

LUCKY = True

you = Girl(YourName)
your = you
I = Boy(MyName)
my = me = I

if LUCKY:
    I.meet(you)
    I.feel(happyness)
    I.love(you, time=forever)
else:
    I.wait(you, time=forever)

if you.feel(sadness) or you.feel(depressed):
    print("my Sweetheart")
    I.feel(sadness)
    I.accompany(you)


while always:
    I.take_care_of(you)
    if you.lover is not me:
        my.sky = dark
        break

for emotion in my.heart:
    try:
        your.lover = me
    except:
        your.best_friend = me

if you.hate(me):
    you.forgive(me)
    I.change()
    love(me)
elif I.bother(you):
    you.scold(me)
    I.apology()
    love(me)
else:
    love(me, how=deeply, when=now)





