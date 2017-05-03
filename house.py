
from mcpi.minecraft import Minecraft
from mcpi import block	  

mc = Minecraft.create()
air = 0
stone = 1
iron = 42
dirt = 3
gold = 41
wood = 5
leaf = 18
door = 64
stonebrick = 98

x, y, z = mc.player.getTilePos()                                                  
x, y, z = mc.player.getPos()  


mc.setBlocks(x-9,y-9,z,x,y,z, stonebrick) #back wall
mc.setBlocks(x-9,y-9,z-9,x-9,y,z, stonebrick) #left wall
mc.setBlocks(x,y-9,z-9,x,y,z, stonebrick) #right wall
mc.setBlocks(x-9,y-9,z-9,x,y,z-9, stonebrick) #top wall
mc.setBlocks(x-9,y-9,z-9,x,y-9,z, stone) #floor
mc.setBlocks(x-9,y,z-9,x,y,z, stonebrick) #roof

mc.setBlocks(x-8,y+1,z-1,x-1,y,z-1, wood) #tier 1
mc.setBlocks(x-8,y+1,z-1,x-1,y,z-8, wood)

mc.setBlocks(x-7,y+2,z-2,x-2,y,z-2, wood) #tier 2
mc.setBlocks(x-7,y+2,z-2,x-2,y,z-7, wood)

mc.setBlocks(x-6,y+3,z-3,x-3,y,z-3, wood) #tier 3
mc.setBlocks(x-6,y+3,z-3,x-3,y,z-6, wood)

mc.setBlocks(x-5,y+4,z-4,x-4,y,z-4, wood) #tier 4
mc.setBlocks(x-5,y+4,z-4,x-4,y,z-5, wood)

mc.setBlocks(x-5,y-8,z,x-4,y-7,z, air) #door

