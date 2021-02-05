# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:29:16 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
while True:
    x,y,z=mc.player.getPos()
    x=x+random.uniform(-1000,1000)
    z=z+random.uniform(-1000,1000)
    y=y+30
    mc.spawnEntity(x,y,z,93)