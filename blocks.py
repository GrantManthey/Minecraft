
from mcpi.minecraft import Minecraft
from mcpi import block	  

mc = Minecraft.create()
air = 0
stone = 1
iron = 42
dirt = 3
gold = 41

x, y, z = mc.player.getTilePos()                                                  
x, y, z = mc.player.getPos()  


mc.setBlocks(x-4,y-4,z,x,y,z, dirt) #back wall
mc.setBlocks(x-4,y-4,z-4,x-4,y,z, dirt) #left wall
mc.setBlocks(x,y-4,z-4,x,y,z, dirt) #right wall
mc.setBlocks(x-4,y-4,z-4,x,y,z-4, dirt) #top wall
mc.setBlocks(x-4,y-4,z-4,x,y-4,z, dirt) #floor
mc.setBlocks(x-4,y,z-4,x,y,z, dirt) #roof

