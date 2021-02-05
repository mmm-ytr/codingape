# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:51:02 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create("104.199.150.71")
x,y,z=mc.player.getTilePos()
mc.setBlocks(x,y,z,x-40,y,z-40,2)