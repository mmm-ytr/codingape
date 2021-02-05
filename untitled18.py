# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:17:25 2021

@author: USER
"""
c
while True:
    x,y,z=mc.player.getTilePos()
    a=mc.getBlock(x,y-1,z+1)
    b=mc.getBlock(x+1,y-1,z)
    c=mc.getBlock(x,y-1,z-1)
    d=mc.getBlock(x-1,y-1,z)
    if a==8 or b==8 or c==8 or d==8 or a==9 or b==9 or c==9 or d==9:
        mc.setBlocks(x-5,y-1,z-5,x+5,y-1,z+5,4)