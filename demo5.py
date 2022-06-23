# ピラミッド作成プログラム{改良版}
from multiprocessing.connection import wait
from re import X
from time import sleep
from tkinter import Y
from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711
mc.postToChat("demo5")

mc.setBlocks(10, 63, 10, 20, 70, 20, param.AIR)
sleep(3)

mc.postToChat("ピラミッド作成開始")
X = 10   #X座標
Y = 63   #Y座標
Z = 10   #Z座標
POS = 0   #位置情報
AT = 0   #位置情報 
for i in range(7):
    for i in range(11-POS*2):
        for i in range(11-POS*2):
            mc.setBlock(X+AT+POS, Y+POS, Z+POS, param.GOLD_BLOCK)
            AT += 1
            sleep(0.1)
        AT = 0
        Z += 1
        sleep(0.3)
    POS += 1
    Z = 10
mc.postToChat("ピラミッド作成完了!!")
mc.setBlock(15, 68, 15, param.GLOWSTONE)