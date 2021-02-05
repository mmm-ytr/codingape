# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:37:51 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x, y, z, 57)