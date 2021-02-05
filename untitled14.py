# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:23:12 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
while True:
    color=random.randrange(0,16)
    mc.setBlocks(x+20,y-1,z+20,x-20,y-1,z-20,color)
    time.sleep(0.5)