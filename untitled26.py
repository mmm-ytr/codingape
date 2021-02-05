# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:43:15 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getPos()
for i in range(1000):
    mc.setBlock(x-i,y-1,z,1)