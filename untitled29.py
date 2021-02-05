# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:53:58 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
def planttree(x,y,z):
    mc.setBlocks(x,y,z,x,y+3,z,17)
    mc.setBlocks(x-1,y+4,z-1,x+1,y+6,z+1,161)
x,y,z=mc.player.getPos()
for i in range(10):
    for j in range(10):
        planttree(x+i*5,y+i*j,z)