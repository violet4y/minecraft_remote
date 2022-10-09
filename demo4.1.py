# ピラミッド作成プログラム
from mcje.minecraft import Minecraft
import param_MCJE as param
"""
from multiprocessing.connection import wait
from re import X
from time import sleep
from tkinter import Y
"""
"量産型"

import demo4

mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711
mc.postToChat("demo4")

