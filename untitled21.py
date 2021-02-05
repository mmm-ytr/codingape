# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:07:13 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setSign(x+1,y,z,63,0,"我愛","minecraft","","也愛","python")