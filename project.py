

from mcpi.minecraft import Minecraft
from mcpi import*

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

#circlesize 27
def makecircle():
	mc.setBlocks(x,y-13,z,x,y,z, stonebrick)
	mc.setBlocks(x,y+13,z,x,y,z, stonebrick)
	mc.setBlocks(x+13,y,z,x,y,z, stonebrick)
	mc.setBlocks(x-13,y,z,x,y,z, stonebrick)#circle cross
	mc.setBlocks(x+3,y+13,z,x-3,y+13,z, stonebrick) #up
	mc.setBlocks(x+3,y-13,z,x-3,y-13,z, stonebrick) #down
	mc.setBlocks(x+13,y+3,z,x+13,y-3,z, stonebrick) #right
	mc.setBlocks(x-13,y+3,z,x-13,y-3,z, stonebrick) #left

	mc.setBlocks(x+12,y+6,z,x+12,y+3,z, stonebrick) #6 #upper left
	mc.setBlocks(x+11,y+8,z,x+11,y+6,z, stonebrick) #8
	mc.setBlocks(x+10,y+9,z,x+10,y+7,z, stonebrick) #9
	mc.setBlocks(x+9,y+10,z,x+9,y+8,z, stonebrick) #10
	mc.setBlocks(x+8,y+11,z,x+8,y+10,z, stonebrick) #11
	mc.setBlocks(x+7,y+12,z,x+7,y+11,z, stonebrick) #12
	mc.setBlocks(x+6,y+13,z,x+6,y+11,z, stonebrick) #13
	mc.setBlocks(x+5,y+13,z,x+4,y+12,z, stonebrick) #13
	
	mc.setBlocks(x-12,y+6,z,x-12,y+3,z, stonebrick) #6 #uppder right
	mc.setBlocks(x-11,y+8,z,x-11,y+6,z, stonebrick) #8
	mc.setBlocks(x-10,y+9,z,x-10,y+7,z, stonebrick) #9
	mc.setBlocks(x-9,y+10,z,x-9,y+8,z, stonebrick) #10
	mc.setBlocks(x-8,y+11,z,x-8,y+10,z, stonebrick) #11
	mc.setBlocks(x-7,y+12,z,x-7,y+11,z, stonebrick) #12
	mc.setBlocks(x-6,y+13,z,x-6,y+11,z, stonebrick) #13
	mc.setBlocks(x-5,y+13,z,x-4,y+12,z, stonebrick) #13

	mc.setBlocks(x+12,y-6,z,x+12,y-3,z, stonebrick) #6 #lower left
	mc.setBlocks(x+11,y-8,z,x+11,y-6,z, stonebrick) #8
	mc.setBlocks(x+10,y-9,z,x+10,y-7,z, stonebrick) #9 
	mc.setBlocks(x+9,y-10,z,x+9,y-8,z, stonebrick) #10
	mc.setBlocks(x+8,y-11,z,x+8,y-10,z, stonebrick) #11
	mc.setBlocks(x+7,y-12,z,x+7,y-11,z, stonebrick) #12
	mc.setBlocks(x+6,y-13,z,x+6,y-11,z, stonebrick) #13
	mc.setBlocks(x+5,y-13,z,x+4,y-12,z, stonebrick) #13


	mc.setBlocks(x-12,y-6,z,x-12,y-3,z, stonebrick) #6 #lower right
	mc.setBlocks(x-11,y-8,z,x-11,y-6,z, stonebrick) #8
	mc.setBlocks(x-10,y-9,z,x-10,y-7,z, stonebrick) #9
	mc.setBlocks(x-9,y-10,z,x-9,y-8,z, stonebrick) #10
	mc.setBlocks(x-8,y-11,z,x-8,y-10,z, stonebrick) #11
	mc.setBlocks(x-7,y-12,z,x-7,y-11,z, stonebrick) #12
	mc.setBlocks(x-6,y-13,z,x-6,y-11,z, stonebrick) #13
	mc.setBlocks(x-5,y-13,z,x-4,y-12,z, stonebrick) #13
makecircle()
def move():
    place = mc.player.getPos()
    place = str(place)
    print ((place)[5:])
    mc.player.setPos(place)
makecircle()
move()
print('place')









