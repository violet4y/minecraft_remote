# It is test file
from multiprocessing.connection import wait
from re import X
from time import sleep
from tkinter import Y
from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711
mc.postToChat("demo4")

mc.postToChat("ピラミッド作成")
mc.postToChat("set goldblock at 10 63 10")
X = 10
Y = 63
Z = 10
mc.setBlock(X, Y, Z, param.GOLD_BLOCK)
X += 1
sleep(0.5)
mc.setBlock(X, Y, Z, param.GOLD_BLOCK)