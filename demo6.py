#階段作成
from multiprocessing.connection import wait
from time import sleep
from mcje.minecraft import Minecraft
import param_MCJE as param
mc = Minecraft.create(port=param.PORT_MC)

X = 30
Y = 63
Z = 10
POS = 0

mc.setBlocks(X, Y, Z, X + 10, Y + 10, Z + 10, param.AIR)
sleep(1)
mc.postToChat("start")

for i in range(10):
    mc.setBlocks(X + POS, Y + POS, Z, X + POS, Y + POS, Z + 10, param.GOLD_BLOCK)
    sleep(0.3)
    POS += 1

sleep(5)

POS = 0
for i in range(10):
    mc.setBlocks(X + POS, Y + POS, Z, X + POS, Y + POS, Z + 10, param.AIR)
    sleep(0.3)
    POS += 1

mc.postToChat("finished")