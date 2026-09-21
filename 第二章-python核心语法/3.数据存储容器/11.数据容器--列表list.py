# 1.数据容器
# score_list = [90, 80, 70, 60, 50]
# # 容器分为5类
# # 列表 list 字符串 str 元组 tuple 集合 set 字典 dict
#
# # 一.列表
# # 1.定义
# # 列表名称 = [元素1, 元素2, 元素3, ...]  #注意是[]中括号
# # 2.特点
# #可以存储不同类型的元素
# #元素有序,可以重复,元素可以修改
#     #有下标有索引---默认第一个下标是0
# s = [1, 2, 3, 4, 5,"A","True","Hello"] #数字、字符串、布尔值、字符都可以作为元素

# # 1.获取  两种方法
# print(s[2]) #正向索引 下标从0开始
# print(s[-6]) #反向索引 最后一个是-1 依次类推

# # 2.修改
# s[5] = 10   #直接列表下标=新值
# print(s)
# s[2:4] = [20, 30]   #切片赋值第三个,第四个改了
# # s [10] = 100    #索引超过范围报错
# # print(s)

# # 3.删除
# del s[6]    #deline的简写是删除的意思
# print(s)

# # 4.遍历    #证明是有序的
# for item in s:
#     print(item)


# 列表-切片(列表,字符串,元组都支持切片操作)  算是修改里的
# 语法: 序列数据[开始索引:结束索引:步长]  用双引 号
# 1.不包含结束索引位置的元素 开始索引默认为0 步长默认为0
# 2.索引采用正向和反向都可以
# 3.步长  从第一个开始算,步长是几中间隔几个元素
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(s[1:5:2])
# print(type(s[1:5:2]))
# print(s[-5:-1])
# print(s[::2])  #开始和结束空表示整个列表
# # 省略问题
# # print(s[:5:])表示从零开始和到5结束
# print(s[:5 ]) #最终省略版本
# print(s[5])  #直接是第六个元素



# # 二.运算方法
# # 列表的常用方法就是指列表这种类型内置的常见功能(添加元素,删除元素,排序等)
# s = [1, 2, 3, 4, 5, "Hello","True","False","A"]
# # 1.append()----在列表的尾部添加元素----s.appemd(元素)
        # s.append("张三")
        # print(s)
# # 2.insert()----在列表指定位置添加元素----s.insert(索引, 元素)
        # s.insert(2, "李四")
        # print(s)
# # 3.remove()----移除列表中指定的元素(第一个出现的元素)----s.remove(元素)
        # s.remove("Hello")
        # print(s)
# # 4.pop()----删除列表中指定索引位置的元素(如果未指引索引,则删除列表最后一个元素)----s.pop(索引)
        # e = s.pop(4)  #可以用一个变量存储删除的元素
        # print(e)
        # print(s)
# # 5.sort()----对列表进行排序(列表中的数据类型一致,才可进行排序)----s.sort()
        # a=[44,556,2,5,66,7,9,1,-2,-99]
        # a.sort()
        # print(a)
# # 6.reverse()----对列表进行反转----s.reverse()   
        # s.reverse()
        # print(s)

# 注意事项:
# 方法不能写成是print(s.append())
# s.后会显示各种方法只需知道即可不用死记硬背
# 7.clear()-----清空列表中的元素----s.clear()




# 练习1

# # 1.定义列表
# num_list=  []
# # 2.将用户输入的10个数字存入列表
# for i in range(10):
#     num = int(input("请输入数字:"))
#     num_list.append(num)
# # 3.排序
# num_list.reverse()
# print("排序后的数字列表是:",num_list)
# #4.输出其中最小值,最大值,和平均值
# print("最小值是:",min(num_list))  #这里不用min函数min(num_list)
# print("最大值是:",max(num_list))
# # sum语句是累加列表中所有的元素   len语句是计算列表的长度
# print("平均值是:",sum(num_list)/len(num_list))


# 练习2
# 方法一
# # 合并两个列表中的元素,并对合并的结果进行重处理
# num_list1 =[19,23,54,64,875,20,109,232,123,54]
# num_list2 =[55,80,72,35,60,123,54,29,91]
# # 1.合并列表
# # for循环将表2的元素遍历出来一个个加入表1
# for i in num_list2:
#     # if i not in num_list1:  #直接去重添加
#     #     num_list1.append(i)
#     num_list1.append(i)
# print(num_list1)  #占位很有影响 顶格是只输出一次不在for循环  与num_list1同行的话输出多次
#
# # 2.去重复记
# new_list = []
# for num in num_list1 :
#     if num not in new_list:
#         new_list.append(num)
# print(new_list)


# # 方法二 比较简单
# # 合并两个列表中的元素,并对合并的结果进行重处理
# num_list1 =[19,23,54,64,875,20,109,232,123,54]
# num_list2 =[55,80,72,35,60,123,54,29,91]
#
# # 1.合并列表
# # 解包:将列表这一类容器解开成一个一个独立的元素  *num_list1
# num_list = [*num_list1,*num_list2]  #相当于将两个列表解开变成一个大列表
# print("合并后的原始列表:",num_list)
# # 组包:将两个解包放到一块合成一个列表
# # 2.去重复记
# new_list = []
# repeat_count = 0
# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)
#     else :
#         print("重复元素是:",num)
#         repeat_count += 1
# print(new_list)
# print(f"重复的元素个数是:",{repeat_count})


# # 方法三
# num_list1 =[19,23,54,64,875,20,109,232,123,54]
# num_list2 =[55,80,72,35,60,123,54,29,91]
#
# num_list = num_list1 + num_list2
# print("合并后的列表",num_list)
# new_list = []
# repeat_count = 0
# for num in num_list :
#     if num not in new_list:
#         new_list.append(num)
#     else :
#         print("重复元素是:",num)
#         repeat_count += 1
# print(new_list)
# print(f"重复的元素的个数是:",{repeat_count})


# 练习3
# 生成1~20的平方的列表
# 1.传统方式
new_list =[]
for i in range(1,21):
    new_list.append(i**2)
# print("1~20平方的列表是:",new_list) #普通输出
print(f"1~20的平方列表是:,{new_list})")  #不是{}里不能放列表是需要将所有文字和{}写到同一个""里
# 2.简化方式
# 列表推导式---就是快速生成一个列表的方法
# 语法格式:  格式1和2差别就是列表后面的  if条件语句
# [要插入的值(可以是变量也可以是表达式)for i in  序列/表达式  后面可以接判断语句]
new_list = [i**2 for i in range(1,21)]
print(f"1~20的平方列表是:,{new_list})")


# 练习4
# 从一个数字列表中提取所有偶数,并计算其平方,组成一个新的列表
# 1.传统方式
num_list = [12,32,45,77,80,92,33,57,97,98]
new_list = []
for i in num_list:
    if i % 2 == 0:
        new_list.append(i**2)
print(f"这个新列表是:,{new_list})")
# 2.简化方式
num_list = [12,32,45,77,80,92,33,57,97,98]
# 要插入的数是符合条件元素的平方及i**2
new_list = [i**2 for i in num_list if i % 2 == 0]
print(f"这个新列表数是:,{new_list})")
