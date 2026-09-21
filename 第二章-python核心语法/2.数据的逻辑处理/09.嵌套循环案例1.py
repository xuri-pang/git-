# 一.for循环的嵌套
# for 元素 in 待处理的数据集
#     循环体的代码1
#     循环体的代码2
#     for 元素 in 待处理数据集:
#         循环体的代码1
#         循环体的代码2

# 案例1:打印一个长度为10,宽度为5的长方形.
# 1.接受键盘的录入
# m = int(input("请输入长方形的长:"))
# n = int(input("请输入长方形的宽:"))
#
# # 2.打印长方形
# for j in range(n):  #控制行--这里表示是宽---外层遍历每一行,每次输出一行
#     for i in range(m):  #控制列--这里表示是长---内层遍历每一列,每次输出一列
#         # 内层循环m次,外层循环一次(相当于分针与时针)
#     # print("*")  #这样不是在一行
#          print("*",end="  ")  #end表示是每次输出以什么结束   print()默认是以end="\n"
#     print()  #这里的作用是换行

# # 案例2:打印99乘法表
# # 输出都是一行一行的输出
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}",end="\t")  #\t表示制表符--相当于一个tab
#     print()
#
# # 案例3:根据输入的直角边的边长,打印等腰直角三角形
# # 1.接受键盘的输入
# a = int(input("请输入直角边的边长:"))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print("*",end="  ")
#     print()

# 案例4.根据输入的数字,打印对应的金字塔
# 1.接受键盘的输入
# a = int(input("请输入数字:"))
# for j in range(1,a+1):
#     for i in range(1,j+1):
#         print(i,end="  ")   #在内层for附属的循环中,print打印的数字是递增的
#     print()

# 案例5:打印国际象棋
# 1.
# for j in range(1,9):
#     for i in range(1,9):
#         if i % 2 == 0 and j % 2 == 0:
#             print("■",end="  ")
#         elif i % 2 != 0 and j % 2 != 0:
#             print("■",end="  ")
#         else:
#             print("□",end="  ")
#     print()  #重点没有不成形状
#
# # 2.
# for j in range(1,9):
#     for i in range(1,9):
#         if (i+j)%2==0:
#             print("■",end="  ")
#         else:
#             print("□",end="  ")
#     print()




