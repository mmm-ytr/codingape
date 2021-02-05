# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:54:58 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
n=1
x,y,z=mc.player.getTilePos()
for i in range(8):
    for l in range(n):
        mc.spawnEntity(x,y,z,60)
    n=n*2
    mc.postToChat("這次生成了"+str(n)+"之蠹魚")
    time.sleep(1)