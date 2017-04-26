
#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block

def init():
    mc = Minecraft.create()
    x, y, z = mc.player.getTilePos() #/gm gets your current posistion
    if z > 70:
        # We need room along the z axis for the steet
        z = 70
    mc.setBlocks(x-15, -1, z-2, x+15, 50, z+58, block.AIR.id)
    mc.setBlocks(x-15, -1, z-2, x+15, -1, z+58, block.AIR.id)
    mc.setBlocks(x-2, -1, z-2, x+2, -1, z+58, block.AIR.id)
    mc.player.setPos(x, 0, z)
    return mc


mc = init()
x, y, z = mc.player.getTilePos()
