from mcpi.minecraft import Minecraft
mc = Minecraft.create()
air = 0
stone = 1
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x+5, y+0, z+5, stone)
