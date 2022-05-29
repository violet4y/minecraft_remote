# It is test file
from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711
mc.postToChat("demo4")

mc.postToChat("Hello!")
mc.postToChat("set goldblock 0 110 0")
mc.setBlock(0, 110, 0, param.GOLD_BLOCK)
