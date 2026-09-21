# 1.字符串的定义的三种方式
# s1 = 'Hello'  # 单引号  同下
# s2 = "Hello"  # 双引号  但是不能换行
# s3 = """
#       Hello
#       World
#       """     #三引号支持换行
#
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))


# 单引号定义字符串   ''中间不能再加'否则将字符串拆开了
# mag ='It's very good'   #错误示例
# 转义字符
# \'-----表示单引号
# \"-----表示双引号
# \n-----表示换行
# \t-----表示制表符  增加一个缩进符 tab

mag = "It's very good"
mag1 ='It\'s very good'    #正确示例  加个斜杠
mag2 = 'Hello 的意思是 "您好"'
mag3 = "Hello 的意思是 \"您好\""
print( mag)
print(mag2)
print(mag3)


#字符串的拼接
sloagn ="黑马程序员" "成就IT黑马"   # 字符串拼接  字符串之间自动拼接
print(sloagn)

# 字符串用加号拼接  既可拼接变量也可拼接自变量
s1 ="人生苦短"
s2 ="我用python"
print("吉多-范罗苏姆:" + s1 + "," + s2)

name = "涛哥"
age = 18
pro = ("软件工程")
hobby = "python.java"
print("大家好,我是" + name + "今年" + str(age) + "岁,学习的专业" + pro + ",爱好" + hobby)
# 加号只能拼接字符串  age 是整形(int)  用str(age)将age转化为字符串

# 用加号拼接会导致1.拼接繁琐 2.数据类型转换麻烦 3.拼接结果不可读(需要换成str)

# 字符串的格式化
# 1.通过占位符 % 来完成字符串喝啊变量的快速拼接  %s  s表示将变量转化为字符串放入占位的位置
s1 = "旭日"
s2 = 18
print("hello,我是%s,今年%s" % (s1,s2))  #后面接%,两个以上的占位符后面需要把变量用元组()括起来

name = "涛哥"
age = 18
pro = ("软件工程")
hobby = "python.java"
print("大家好,我是%s,今年%s岁,学习的专业是%s,爱好%s" % (name,age,pro,hobby) )


# f"内容{变量\表达式}"
# 2.通过f"内容{变量\表达式}"来完成快速格式化--就是将{}里的转化成字符串嵌入到文本中 ----更推荐
# {}里面可以放变量,表达式,函数,列表,判断表达式---注意需要将全部文字和{}放到同一对""中


name = "涛哥"
print(f"大家好,我是{name}")
# 用途
# 例如  要进行年龄的计算,首先需要将
age = int(input("请输入年龄:"))
print("年龄 :"+ str(age))  #这里不将age转化为字符串--会报错
print(f"大家好,我明年{age+1}岁")  #这里将age转化为字符串--不会报错

