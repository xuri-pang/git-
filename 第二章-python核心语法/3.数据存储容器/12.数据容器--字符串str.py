# 一.介绍
# 字符串是字符的容器,一个字符转中可以存放任意数量的字符.
# 如"Python",'Python',"""Python"""
# 特点:
# 1.不可变性(不可更改)
# 2.有序性---跟列表差不多都是有正反索引(正反下标)
# 3.可迭代---跟列表一样都是可迭代的就是可以for循环遍历
from itertools import count
from logging.config import stopListening

# 字符串-切片
# 语法: 序列对象[索引1:索引2:步长]
# 举例:
# s = "Python"
# print(s[3])
# print(s[-1])
# print(s[0:5:2])
# print(s[::2])
# print(s[:5])
# print(s[-1:-5:-1])
#
#
# # s[4] = "x"  #会直接报错
# # print(s)
#
# # 验证迭代
# for i in s:
#     print(i)
#
# a = "abcdefg"
# print(a[::-1])#相当于列表中的reverse()倒序
# # a.reverse( ) #在字符串中不可用


# # 二.字符串-常用方法
# # 1.find()---在字符串中查找子串,返回第一次出现  索引位置  ,找不到返回-1----s.find('Python')
# s = "Hello-word-python-Hello"
# print(s.find('ello'))
# # 2.count()----统计字串在字符串中出现的次数----s.count('y')
# print(s.count('Hello'))
# # 3.upper()----将字符串中的字母全换成大写----s.upper()
# ss = s.upper()
# print(ss)
# # 4.lower()----将字符串中的字母全换成小写----s.lower()
# sss = s.lower()
# print(sss)
# # 5.split()----将字符串按指定字符进行切割(不包含本身及去除本身)----s.split('f')
# slist= s.split('-') #将切割的封装到一个列表中
# print(slist)
# # 6.strip()----去除字符串头尾指定的字符（默认空格）----s.strip(' ')
# a = "-Hello-word-python-Hello"
# strp = a.strip('-')
# print(strp)
# # 7.replace()----替换字符串中指定的字符----s.replace('f','g')
# print(s.replace('H','g'))
# # 8.startswith----判断字符串是否以指定字符开头,返回布尔值----s.startwith('')
# # 9.endswith----判断字符串是否以指定字符结尾,返回布尔值----s.endwith('')
# print(s.startswith("Hello"))
# print(s.endswith(' '))  #''里可以是空格还有字符,如果什么也不填则返回都是True


# 三.案例
# 邮箱格式验证:用户输入一个邮箱,验证邮箱格式是否正确(包含一个@和至少一个.)
# 例如ithem@mail.itcast.con,如果输入正确,输出"邮箱格式正确,否则输出"邮箱格式错误"
# 方式一
# 1.接收用户输入的邮箱
# email = input("请输入邮箱:")
# # 2.判断邮箱格式是否正确
# #用count()来统计@出现的次数
# while True:
#     if email.count('@') == 1 and email.count('.') >= 1:  #ithem@mail.itcast.con所以是>=1
#         print("邮箱格式正确")
#         break
#     else:
#         email = input("请重新输入邮箱:")

# 方式二
# email = input("请输入邮箱:")
# # 用in来判断子串是否在字符串中   ('.')这个可能是一个或者多个所以用in来判断是否存在存在是True
# while True:
#     if email.count('@') and '.' in email:
#         print("邮箱格式正确")
#         break
#     else:
#         email = input("邮箱格式错误,请重新输入邮箱:")

# 练习1.输入一个字符串,判断该字符串是否是回文(两边对称)
# num = input("请输入一个字符串:")
# if num == num[:: -1]:
#     print("该数字是回文")
# else:
#     print("该数字不是回文")

# 练习2.将用户输入的10个字符串,反转后全部转换为大写,然后记录在列表中,最后将列表内容,遍历输出
num = input("请输入10个字符串:")
num_list = num.upper()
for i in num_list :
    print(i)