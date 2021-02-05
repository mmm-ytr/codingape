# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:59:50 2021

@author: USER
"""

import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
color=random.randrange(0,16)
mc.setBlocks(x-500,y-1,z-500,x+500,y-1,z+500,166)