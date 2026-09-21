# print(100) #整型--int
# print(3.14)#浮点型--float
# print(True, False)#布尔型--bool  首字母大写  本质属于整型
# print('hello world')#字符串型--str
# print(None)#空值--NoneType

# type()   查看数据类型
print(type(100))
print(type("Hello"))
print(type(True))
print(type(None))
print(type(3.14))
num = -100
print(type(num))  #如果print(type())中传的是一个变量则会测值的数据类型

#isinstance(数据,类型)  判断数据类型  返回一个布尔值
num = 100
print(num)
print(isinstance(num, int))

