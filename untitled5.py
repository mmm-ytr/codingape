# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:52:10 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
t=0
while True:
    t=t+1
    mc.postToChat("第"+str(t)+"次")