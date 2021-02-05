# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:29:11 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
from random import randrange
mc=Minecraft.create()
r=randrange(0,16)
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        if data==r:
            mc.postToChat("恭喜你找到我>//<")
            mc.setBlock(hit,pos,57)
            break
        elif data<r:
            mc.postToChat("找錯囉!再試試看更大的自ID吧")
        elif data>r:
            mc.postToChat("找錯囉!再試試看更小的自ID吧")