# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:38:35 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
myid=mc.getPlayerEntityId("MigUelLee")
mc.postToTitle(myid,"Hello")