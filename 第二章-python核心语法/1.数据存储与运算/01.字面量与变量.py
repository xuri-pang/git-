print(100) #整型int
print(3.14)#浮点型float
print(True, False)#布尔型bool  首字母大写  本质属于整型
print('hello world')#字符串型str
print(None)#空值NoneType


print(True + 1)#2  True会转为1
print(False - 1)#-1  False会转为0

# 变量
# 格式 <变量名> = <值>  例子 num=2026
# 变量不用声明,变量在运行中一直变化.动态变量  一个变量可以存储不同变量的值.
# num = 1114.1
# print(num)
#
# num = num + 1
# print(num)
#
# num = "ok"
# print(num)
#
# num = True
# print(num)

# 案例
# 基础变量是20.7 每月增加50 未来了两个月的播放量
base = 20.7  #一次可以生成多个变量  升级版本  :  base,incr = 20.7,50
incr = 50
print("未来第一个月的播放总量:",base+incr)   #快速复制一行是ctrl + d
print("未来第二个月的播放总量:",base + incr + incr)
