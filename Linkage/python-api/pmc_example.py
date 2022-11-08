#块缓存创建
#注释
import sys
import time
sys.dont_write_bytecode = True
######################
#从这里开始

#导入模块
import tsujicon_pyapi.pmc as pmc

#制作控制器项目
c = pmc.pmc()

#与控制器连接
#connect(ip, port)
#返回值：无
c.connect('192.168.1.55', 7777)

#控制器版本
#ver()
#返回值：版本的字节串
print(c.ver())
time.sleep(1)

#当前位置
#get_pos()
#返回值：各频道位置的配列
print(c.get_pos('0'))
time.sleep(1)
i=1
while i>0:
	print(c.get_pos16())
	time.sleep(1)
	print(c.get_status())
	time.sleep(1)
	print(c.send_recv('VER?'))
	time.sleep(1)
	print(c.get_pos('3'))
	c.set_pos('3','-943')
	c.send('LOC')
	time.sleep(1)
	c.send('REM')
	time.sleep(1)
	i-=1