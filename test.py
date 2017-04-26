#!/usr/bin/python
# Import Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block
 
mc = minecraft.Minecraft.create()
 
# Get player position
pPos = mc.player.getTilePos()
# Change block
mc.setBlocks(
    pPos.x-5, #down
    pPos.y,
    pPos.z-5, #left
    pPos.x+5, #up
    pPos.y-5, #down
    pPos.z+10, #right
    block.STONE)
 
 
