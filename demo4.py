# It is test file
from multiprocessing.connection import wait
from re import X
from time import sleep
from tkinter import Y
from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711
mc.postToChat("demo4")

mc.postToChat("clear")
mc.setBlocks(10, 63, 10, 20, 65, 20, param.AIR)
sleep(1)

mc.postToChat("ピラミッド作成")
mc.postToChat("set goldblock at 10 63 10")
X = 10
Y = 63
Z = 10
POS = 0
for i in range(7):
    for i in range(11):
        mc.setBlocks(X+POS, Y+POS, Z+POS, X+10-POS*3, Y+POS, Z-POS, param.GOLD_BLOCK)
        X += 1
        sleep(0.5)
    POS += 1
    
    