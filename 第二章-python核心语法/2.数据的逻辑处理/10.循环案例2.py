# 案例1.根据输入的用户名密码执行登陆操作
# 1.正确用户名和密码为admin/666888 ,zhangsan/123456,taoge/888666
# 2.输入用户名和密码进行登录,直到登录成功,程序结束运行;如果登陆失败,则继续输入用户名和密码进行登录
# 3.输入的用户名和密码不能为空
# 4.登录成功:输出"登录成功,进入B站首页-"
# 5.登陆失败:输出"用户名或密码错误.请重新输入!"
# 关键字
# 1. break 跳出当前循环
# 2. continue 跳过当前循环


# 首先判断用什么循环--看2不知循环多少次所以用while循环
# 1.用continue版
# while True :   # 死循环 需要用break结束(只能出现在循环里)
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#     if username == "" or password == "" :  #如果输入的用户名和密码为空还接着进行下一个判断用continue来结束本次循环不用进行下一个判断
#         print("用户名或密码不能为空")
#         continue  #适用于两个if判断  如果是一个if判断 则不用continue
#     if username =="admin" and password == 666888 or username == "zhangsan" and password == 123456 or username == "taoge" and password == 888666:
#         print("登录成功,进入B站首页-")
#         break  #重点是结束while循环
#     else:
#         print("用户名或密码错误.请重新输入!")

# # 2.不用continue版
# while True :   # 死循环 需要用break结束(只能出现在循环里)
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#     if username == "" or password == "" :  #如果输入的用户名和密码为空还接着进行下一个判断用continue来结束本次循环不用进行下一个判断
#         print("用户名或密码不能为空")
# #这里就不需要continue
#     elif username =="admin" and password == 666888 or username == "zhangsan" and password == 123456 or username == "taoge" and password == 888666:
#         print("登录成功,进入B站首页-")
#         break  #重点是结束while循环
#     else:
#         print("用户名或密码错误.请重新输入!")
#
# 练习:加一个操作输入五次就不允许操作了
# i = 0
# while i<5 :   # 死循环 需要用break结束(只能出现在循环里)
#     i += 1
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#     if username == "" or password == "" :  #如果输入的用户名和密码为空还接着进行下一个判断用continue来结束本次循环不用进行下一个判断
#         print("用户名或密码不能为空")
#         continue  #适用于两个if判断  如果是一个if判断 则不用continue
#     if username =="admin" and password == 666888 or username == "zhangsan" and password == 123456 or username == "taoge" and password == 888666:
#         print("登录成功,进入B站首页-")
#         break  #重点是结束while循环
#     else:
#         print(f"输入的用户名或密码错误,您还有{5-i}次机会")


# 案例2.
# 1.系统随机生成一个随机数---
# import random
# num = random.randint(1,100)
# 2.用户根据提示输入一个数字,并将所猜的数字输入系统
# 3.如果猜错,系统给出的提示是猜大了,还是猜小了,然后继续输入猜的数字
# 并不确定循环次数所以用while循环
# 4.如果猜对,系统自动退出,游戏结束

# 先写基本流程再加循环
# import random
# random_num = random.randint(1,100)
#
# while True:
#     num = int(input("请输入一个数字:"))
#
#     if num > random_num:
#         print("猜大了")
#     elif num < random_num:
#         print("猜小了")
#     else:
#         print("恭喜您,猜对了")
#         break   #不能和if,else在一行否则不管是否都会结束while循环
# print("随机生成的数字是:",random_num)  #前面的break是结束循环,如果没有后面print会变成灰色(永远运行不到)


# 需求1.将1~1000之间(包含1000)所有的5的倍数的数字累加起来
# 需求2.统计字符串"akiwksjskdiklowiqaamnvbamvaxnsjdsjkaaxkjd"  中有多少个a和k
total = 0
for i in range(1,1001):
    if i % 5 ==0 :
        total += i
print(f"1~1000之间所有5的倍数的数字累加和为:{total}")

a = "akiwksjskdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
count = 0    #total是累加和  count是计数
for char in a:   #char表示的是字母 i表示的是数字
    if char == "a" or char == "k":
    # if char == "a" or "k":  不能简写否则结果就是41
        count += 1# count = count + 1 == count += 1  #total += 1是累加和 不改变这个结果永远是41
print(f"字符串中a出现的次数为:{count}")