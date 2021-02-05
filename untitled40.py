# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:36:46 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
import random
mc=Minecraft.create("104.199.150.71")
r=0
x=-555
y=86
z=275
myid=mc.getPlayerEntityId("MigUelLee")
r=random.randrange(0,5)
if r>2:
    mc.postToChat("你必須要被隔離")
    while True:
        mc.player.setTilePos(x,y,z)
elif r<2 or r==2:
    mc.postToChat("你不用被隔離")
    while True:
        x=-555
        y=86
        z=275
        
        mc.player.setTilePos(x,y,z)
        
