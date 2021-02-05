# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 09:53:15 2021

@author: USER
"""

while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.setBlock(x,y,z,41)