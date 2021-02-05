# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:37:21 2021

@author: USER
"""
c
import time
import random
mc=Minecraft.create()
a=0

while a<100:
    color=random.randrange(0,9)
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,38,color)
    time.sleep(0.2)
    a=a+1