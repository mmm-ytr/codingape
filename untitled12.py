# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:33:58 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x+2, y, z+2, 57)
mc.setBlock(x+2, y+7, z+1, 57)
mc.setBlock(x+1, y+1, z+2, 57)
mc.setBlock(x+1, y+5, z, 57)
mc.setBlock(x+2, y+6, z, 57)
mc.setBlock(x, y+2, z+2, 57)
mc.setBlock(x, y+3, z+1, 57)
mc.setBlock(x, y+4, z, 57)