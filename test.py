#!/usr/bin/python
# makes a block of stone
# Import Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block
 
mc = minecraft.Minecraft.create()
 
# Get player position
pPos = mc.player.getTilePos()
# Change block
mc.setBlocks(
    pPos.x-5, #moves it along  the X axis
    pPos.y,
    pPos.z-5, #moves it along the Z axis
    pPos.x+5, 
    pPos.y-5, #moves it along the Y axis
    pPos.z+10, 
    block.STONE)
 
 
