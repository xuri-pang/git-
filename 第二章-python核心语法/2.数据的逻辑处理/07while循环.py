# 一.基础while循环
# 语法结构
# while 条件:
#     循环体语句1
#     循环体语句2
#     ...
# while 条件:  false,循环整场结束时执行

# 二.无限循环（死循环）
# while True: 条件永远成立，不停循环。
# 必须要有 break 才有出口，否则程序停不下来。

# 三.两个关键字：break 和 continue
# 1.continue:跳过本次循环剩下代码，直接回到 while 条件判断开头，不结束循环

# 2.break:立即结束本次循环

# 四. while 嵌套----（while 里面套 while）
# 外层循环跑 1 次，内层 while 完整跑完一遍。
# python
# 运行
# i = 1
# while i <=3:    # 外层
#     j = 1
#     while j <=2: # 内层
#         print(f"i={i},j={j}")
#         j +=1
#     i +=1
# 内层循环变量，每次外层循环开始要重新初始化（j=1 写在内层 while 上面）

# 五. while + match  #多选择模式
# continue：某个 case 里用，直接回到 while 开头，重新输入菜单
# break：case5 退出，终止 while 循环

# ----------------------------------------代码演示-----------------------------------
# 1.打印10遍 "人生苦短,我用python"

i = 0
while i < 10 :
    print("人生苦短,我用python")
    i += 1
else :
    print("循环结束")

# 2,计算1~100所有偶数的累加之和
# 如何获取到偶数 : num %2 == 0
# 累加运算用什么运算符 : +=

total = 0 #用来记录累加之和
i = 1 #循环开始的数字

while i <= 100 :
    if i % 2 == 0 :
        total += i
    i += 1

print(f"1~100之间的偶数的累加之和为:{total}")

total1 = 0
i = 1

while i <= 100 :
    if i % 2 != 0 :
        total1 += i
    i += 1

print(f"1~100之间的奇数的累加之和为:{total1}")


