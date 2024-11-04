from gpiozero import LED
from time import sleep
from gpiozero.pins.mock import MockFactory
from gpiozero import Device

# 使用 MockFactory 代替真实的引脚工厂
Device.pin_factory = MockFactory()

makerobo_RelayPin = LED(17)

def makerobo_setup():
    makerobo_RelayPin.off() # 关闭继电器	

def makerobo_loop():
	while True:
		# 继电器打开
		makerobo_RelayPin.on()  # 打开继电器
		sleep(0.5)              # 延时500ms
		# 继电器关闭
		makerobo_RelayPin.off() # 关闭继电器
		sleep(0.5)         # 延时500ms

# 释放资源
def makerobo_destroy():
    makerobo_RelayPin.close()

# 程序入口
if __name__ == '__main__':
	makerobo_setup()           #  初始化
	try:
		makerobo_loop()        #  调用循环函数
	except KeyboardInterrupt:  #  当按下Ctrl+C时，将执行destroy()子程序。
		makerobo_destroy()     #  释放资源

