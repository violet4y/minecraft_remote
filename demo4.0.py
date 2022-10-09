# ピラミッド作成プログラム
from multiprocessing.connection import wait
from re import X
from time import sleep
from tkinter import Y
from mcje.minecraft import Minecraft
import param_MCJE as param

"6段ピラミッド基準"

mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711
mc.postToChat("demo4")

X = 10   #X座標
Y = 63   #Y座標
Z = 10   #Z座標
POS = 0   #位置情報 

mc.setBlocks(X, Y, Z, X+10, Y+10, Z+10, param.AIR)
sleep(3)

mc.postToChat("ピラミッド作成開始")

for i in range(7):
    for i in range(11-POS*2):
        mc.setBlocks(X+POS, Y+POS, Z+POS, X+10-POS, Y+POS, Z+POS, param.GOLD_BLOCK)
        Z += 1
        sleep(0.8)
    Z -= 11-POS*2
    POS += 1
mc.postToChat("ピラミッド作成完了!!")
mc.setBlock(X+POS-2, Y+POS-2, Z+POS-3, param.GLOWSTONE)