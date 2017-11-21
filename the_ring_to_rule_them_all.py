

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
def startcircle(number,thickness):
	#mc.setBlocks(x,y-13,z+number,x,y,z, stonebrick)
	#mc.setBlocks(x,y+13,z+number,x,y,z, stonebrick)
	#mc.setBlocks(x+13,y,z,x,y,z+number, stonebrick)
	#mc.setBlocks(x-13,y,z,x,y,z+number, stonebrick)#circle cross
	mc.setBlocks(x+3+thickness,y+12+thickness,z,x-3-thickness,y+13,z+number, stonebrick) #up
	mc.setBlocks(x+3+thickness,y-14+thickness,z,x-3-thickness,y-13,z+number, stonebrick) #down
	mc.setBlocks(x+11+thickness,y+3+thickness,z,x+13,y-3,z+number, stonebrick) #right
	mc.setBlocks(x-13-thickness,y+3+thickness,z,x-13,y-3,z+number, stonebrick) #left
def leftcircle(number,thickness):
	mc.setBlocks(x+12,y+6,z,x+12+thickness,y+3,z+number, stonebrick) #6 #upper left
	mc.setBlocks(x+11,y+8,z,x+11+thickness,y+6,z+number, stonebrick) #8
	mc.setBlocks(x+10,y+9,z,x+10+thickness,y+7,z+number, stonebrick) #9
	mc.setBlocks(x+9,y+10,z,x+9+thickness,y+8,z+number, stonebrick) #10
	mc.setBlocks(x+8,y+11,z,x+8+thickness,y+10,z+number, stonebrick) #11
	mc.setBlocks(x+7,y+12,z,x+7+thickness,y+11,z+number, stonebrick) #12
	mc.setBlocks(x+6,y+13,z,x+6+thickness,y+11,z+number, stonebrick) #13
	mc.setBlocks(x+5,y+13,z,x+4+thickness,y+12,z+number, stonebrick) #13
	
	mc.setBlocks(x+12,y-6,z,x+12+thickness,y-3,z+number, stonebrick) #6 #lower left
	mc.setBlocks(x+11,y-8,z,x+11+thickness,y-6,z+number, stonebrick) #8
	mc.setBlocks(x+10,y-9,z,x+10+thickness,y-7,z+number, stonebrick) #9 
	mc.setBlocks(x+9,y-10,z,x+9+thickness,y-8,z+number, stonebrick) #10
	mc.setBlocks(x+8,y-11,z,x+8+thickness,y-10,z+number, stonebrick) #11
	mc.setBlocks(x+7,y-12,z,x+7+thickness,y-11,z+number, stonebrick) #12
	mc.setBlocks(x+6,y-13,z,x+6+thickness,y-11,z+number, stonebrick) #13
	mc.setBlocks(x+5,y-13,z,x+4+thickness,y-12,z+number, stonebrick) #13
def rightcircle(number,thickness):	
	mc.setBlocks(x-12,y+6,z,x-12-thickness,y+3,z+number, stonebrick) #6 #uppder right
	mc.setBlocks(x-11,y+8,z,x-11-thickness,y+6,z+number, stonebrick) #8
	mc.setBlocks(x-10,y+9,z,x-10-thickness,y+7,z+number, stonebrick) #9
	mc.setBlocks(x-9,y+10,z,x-9-thickness,y+8,z+number, stonebrick) #10
	mc.setBlocks(x-8,y+11,z,x-8-thickness,y+10,z+number, stonebrick) #11
	mc.setBlocks(x-7,y+12,z,x-7-thickness,y+11,z+number, stonebrick) #12
	mc.setBlocks(x-6,y+13,z,x-6-thickness,y+11,z+number, stonebrick) #13
	mc.setBlocks(x-5,y+13,z,x-4-thickness,y+12,z+number, stonebrick) #13

	mc.setBlocks(x-12,y-6,z,x-12-thickness,y-3,z+number, stonebrick) #6 #lower right
	mc.setBlocks(x-11,y-8,z,x-11-thickness,y-6,z+number, stonebrick) #8
	mc.setBlocks(x-10,y-9,z,x-10-thickness,y-7,z+number, stonebrick) #9
	mc.setBlocks(x-9,y-10,z,x-9-thickness,y-8,z+number, stonebrick) #10
	mc.setBlocks(x-8,y-11,z,x-8-thickness,y-10,z+number, stonebrick) #11
	mc.setBlocks(x-7,y-12,z,x-7-thickness,y-11,z+number, stonebrick) #12
	mc.setBlocks(x-6,y-13,z,x-6-thickness,y-11,z+number, stonebrick) #13
	mc.setBlocks(x-5,y-13,z,x-4-thickness,y-12,z+number, stonebrick) #13
def hollow():
        mc.setBlocks(x-14,y+6,z,x-14,y-6,z, air)
        mc.setBlocks(x-14,y+6,z,x-13,y-6,z, air)
        mc.setBlocks(x-17,y+6,z,x-16,y-2,z+3,air)#6
        mc.setBlocks(x-17,y+7,z,x-16,y-3,z+3, air)#6
        mc.setBlocks(x-17,y+7,z,x-16,y-3,z+3, air)#6
        mc.setBlocks(x-13,y+8,z,x-11,y+6,z, air)
        mc.setBlocks(x-12,y+9,z,x-10,y+8,z, air)
        mc.setBlocks(x-11,y+10,z,x-10,y+8,z, air)
        mc.setBlocks(x-10,y+11,z,x-9,y+10,z, air)
        mc.setBlocks(x-9,y+12,z,x-8,y+11,z, air)
        mc.setBlocks(x-7,y+12,z,x-6,y+12,z, air)
        mc.setBlocks(x+6,y+14,z,x-6,y+14,z, air)#top flat part
        mc.setBlocks(x+6,y+14,z,x-6,y+14,z, air)
        mc.setBlocks(x+7,y+16,z,x-7,y+16,z+3, air)
        mc.setBlocks(x+6,y+14,z,x+5,y+13,z, air)
        mc.setBlocks(x+7,y+13,z,x+6,y+12,z, air)
        mc.setBlocks(x+13,y+6,z,x+13,y,z, air)
        mc.setBlocks(x+14,y+5,z,x+14,y-3,z, air)
        mc.setBlocks(x+13,y-6,z,x+13,y-3,z, air) #lower left
        
        
        mc.setBlocks(x+8,y-12,z,x-9,y-11,z, air)#bottom
        mc.setBlocks(x+9,y-11,z,x-10,y-11,z, air)
        
        
def downleft(first,second,third,fourth,fith,sixth,iterations):
    X = 0
    while X != iterations:
        first = first+1
        second = second-1
        fourth = fourth+1
        fith = fith-1
        mc.setBlocks(x+first,y+second,z,x+fourth,y+fith,z, air)
        X = X+1
def downright(first,second,third,fourth,fith,sixth,iterations,material):
    X = 0
    while X != iterations:
        first = first-1
        second = second-1
        fourth = fourth-1
        fith = fith-1
        mc.setBlocks(x+first,y+second,z+third,x+fourth,y+fith,z,material)
        X = X+1
def upright(first,second,third,fourth,fith,sixth,iterations,material):
    X = 0
    while X != iterations:
        first = first-1
        second = second+1
        fourth = fourth-1
        fith = fith+1
        mc.setBlocks(x+first,y+second,z,x+fourth,y+fith,z,material)
        X = X+1

        #mc.setBlocks(x+6,y+14,z,x+5,y+13,z, air)
        
        #mc.setBlocks(x+7,y+13,z,x+6,y+12,z, air)
        #downleft(7,13,0,6,12,0,6)
def sword():
        def cube(X,Y,Z,first,second,material):
            mc.setBlocks(x+X,y+Y,z+Z,x+X+first,y+Y+second,z,material)
        cube(15,-10,2,-3,3,stone)#big
        cube(13,-8,2,-2,2,stone)
        cube(12,-7,2,-2,2,stone)
        cube(11,-6,2,-2,2,stone)
        cube(10,-5,2,-2,2,stone)
        cube(9,-4,2,-2,2,stone)
        cube(8,-3,2,-2,2,stone)
        cube(7,-2,2,-2,2,stone)
        downright(9,5,2,9,4,0,8,iron)
        mc.setBlocks(x+4,y+1,z+2,x+4,y+1,z+0,iron)
        cube(4,-1,2,2,1,iron)
        cube(3,0,2,3,1,iron)
        cube(2,1,2,3,1,iron)
        cube(5,1,2,2,1,iron)
        cube(1,2,2,3,1,iron)
        cube(0,3,2,3,1,iron)
        cube(-1,4,2,3,1,iron)
        cube(-2,5,2,3,1,iron)
        cube(-3,6,2,3,1,iron)
        cube(-4,7,2,3,1,iron)
        cube(-5,8,2,3,1,iron)
        cube(-6,9,2,3,1,iron)
        cube(-7,10,2,3,1,iron)
        cube(-7,11,2,2,1,iron)
        upright(4,1,2,4,1,2,10,air)
        
def fixit():
    mc.setBlocks(x-15,y+6,z,x-15,y-3,z+2, stonebrick)#6
    mc.setBlocks(x-12,y+5,z,x-12,y-3,z+2, stonebrick)#6
    mc.setBlocks(x-11,y+6,z,x-11,y+5,z+2, stonebrick)
    mc.setBlocks(x+12,y+2,z,x+12,y,z+2, stonebrick)
    mc.setBlocks(x+9,y-10,z,x+9,y-10,z,air)
    mc.setBlocks(x-6,y+13,z,x-6,y+12,z,air)
    mc.setBlocks(x-8,y+12,z,x-8,y+12,z,air)
    mc.setBlocks(x-8,y+13,z,x-8,y+12,z,air)
    mc.setBlocks(x-8,y+13,z,x-8,y+12,z,stonebrick)
    mc.setBlocks(x-7,y+15,z,x-8,y+12,z,stonebrick)
    
    
        
startcircle(2,4)
leftcircle(2,2)
rightcircle(2,3)
hollow()
downleft(6,13,0,7,12,0,6)
downright(13,-6,0,13,-5,0,3,air)
downright(13,-7,0,13,-7,0,4,air)
downleft(-14,-6,0,-13,-6,0,4)
downleft(-14,-7,0,-14,-7,0,4)
downleft(-13,-5,0,-13,-5,0,2)
fixit()
sword()

#def move():
   # place = mc.player.getPos()
  #  place = str(place)
    #int(round(x))
 #   place = ((place)[5:-2])
    #print (place)
    #a = (place[0:2])
    #if a <10 and a >-10:
   #     a =((place)[0:])
  #  else:
 #       a = (place[0:2])
        
    #b =(place[8])
    #c =(place[])
    #place = int(place)
    #place=int(round(place))
#    print (place)
#    print (a)
 #   mc.player.setPos(place)

#move()









 