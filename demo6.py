from multiprocessing.connection import wait
from time import sleep
from mcje.minecraft import Minecraft
import param_MCJE as param
mc = Minecraft.create(port=param.PORT_MC)

X = 20
Y = 63
Z = 10
POS = 0

mc.postToChat("階段")

for i in range(10):
    mc.setBlocks(X + POS, Y, Z, param.GOLD_BLOCK)
mc.postToChat("finished")