# It is test file
from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711
mc.postToChat("demo4")

mc.postToChat("ピラミッド作成")
mc.postToChat("set goldblock at 10 63 10")
mc.setBlock(10, 63, 10, param.GOLD_BLOCK)
