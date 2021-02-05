# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:16:34 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,38)
    time.sleep(0.2)