# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:46:16 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
import time
cy,z=mc.player.getTilePos()
q=20
w=10
e=15
mc.setBlocks(x,y,z,x+q,y+w,z+e,4)
mc.setBlocks(x+1,y+1,z+1,x+q-1,y+w-1,z+e-1,0)