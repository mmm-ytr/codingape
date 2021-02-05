# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:23:50 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
y=y-1
mc.setBlocks(x-1,y,z-1,x+1,y,z+1,57)
