# 1.if语句的基本格式
# if 要判断的条件:-------判断语句的结果必须是布尔类型True或 False
    # 条件成立时,执行对应的操作-----True才运行

# 例子1:如果高考分超过680分,我就去清华
# score = int(input("请输入你的高考分:"))
# if score >680:
#     print(f"你的分数是{ score},恭喜你进入清华")
# else :
#     print(f"你的分数是{ score},未到分数线")

# 案例2

# 1.基础语句----只有if语句
# 模拟b站的登录功能(账号密码分别是 188888888  666888)
#
# ok_account = 188888888
# ok_password = 666888

# account = int(input("请输入账号:"))
# password = int(input("请输入密码:"))
# if account == ok_account and password ==ok_password:
#     print("登录成功")
#     print("欢迎来到B站")
# if account != ok_account or password !=ok_password:  #-----冗杂步骤其实用else: 更简单
#     print("账号或密码错误")
#


# 1.进阶语句-----if else 语句  if  elif  else
#例子1
# ok_account = 188888888
# ok_password = 666888
#
# account = int(input("请输入账号:"))
# password = int(input("请输入密码:"))
# if account == ok_account and password ==ok_password:
#     print("登录成功")
#     print("欢迎来到B站")
# else :
#     print("登录失败")
#     print("账号或密码错误")
#
#例子2
# 根据用户输出的年份,判断这一年是平年还是闰年
# (非整百的年份且能被4整除为闰年,整百年且能被400整除为闰年
#
# year = int(input("请输入年份:"))
# if (year %100 !=0 and year %4 ==0) or (year %400 ==0):
#     print(f"{year}是闰年")
# else :
#     print(f"{year}是平年")
#
# 练习1:输入一个数字,判断这个数字是偶数还是奇数

# num = int(input("请输入一个数字"))
# if num %2 == 0 :
#     print(f"{num}是偶数")
# else :
#     print(f"{num}是奇数")

# 练习2:根据用户输入的年龄,判断该用户是否已成年

# ok_age = 18
# age = int(input("请输入年龄:"))
# if age >=ok_age :
#     print(f"{age}已成年")
# else :
#     print(f"{age}未成年")

# 练习3:输入一个数字,判断这个数字是正数,负数还是零

# 1.
# num1 = int(input("请输入数字:"))
# if num1 > 0 :
#     print(f"{num1}是正数")
#     if num < 0 :
#         print(f"{num1}是负数")
# else :
#     print(f"{num1}是零")

# # 2.
# num2 = int(input("请输入数字:"))
# if num2 > 0 :
#     print(f"{num2}是正数")
# elif num2 <0 :
#     print(f"{num2}是奇数")
# else :
#     print(f"{num2}是零")

# # 练习4:根据用户输入的考试分数,判断分数是否及格(>=60就是及格)

# ok_score = 60
# score = int(input("请输入分数:"))
# if score >= ok_score :
#     print(f"你的分数是{score},恭喜通过考试")
# else :
#     print(f"你的分数是{score},考试未及格没有通过考试")

# 3.if进阶语法:if--elif--else 进阶语句三个是并列的  elif可以是多个

# 例子2:输入用户名,密码登录 (用户名密码为 admin/666888 或 root/123456 或 zhangsan/56789)

# username = input("请输入用户名:")
# password = input("请输入密码:")    #只要后面不用到密码的运算不用转换为数字int()
#
# if username == "admin" and password == "666888" :
#     print("登录成功1")
# elif username == "root" and password == "123456" :
#     print("登录成功2")
# elif username == "zhangsan" and password == "56789" :
#     print("登录成功3")
# else :
#     print("登录失败")

# 练习
# 1.输入考试成绩,判断成绩等级
#   大于等于85分为优秀
#   60~85为及格
#   否则就是不及格

# score = float( input ("请输入你的成绩:"))
# if score >= 85 :
#     print("你的成绩等级为优秀")
# elif score >60 and score <85 :
#     print("你的成绩登记为及格")
# else :
#     print("你的成绩等级为不及格")

# 2.根据输入购物车的商品总额,根据以下折扣规则,计算实际应付的金额
#   金额 >= 500 ; 8折
#   300 <= 金额 <500 ; 9折
#   100 <= 金额 < 300 ; 95折
#   金额 < 100 ; 无折扣

money = float(input ("请输入你购物车的商品总额"))
if money >= 500 :
    print(f"你应付的金额是:{money *0.8}")
elif money >= 300 and money < 500 :
    print(f"你应付的金额是:{money * 0.9}")
elif money >=100 and money <300 :
    print(f"你应付的金额是:{money * 0.95}")
else :
    print(f"你应付的金额是:{money}")

# 1.三角形的判断
# if的嵌套


# # 根据输入的三个边的边长(正整数)判定是什么三角形,还是不构成三角形
# a ,b , c = int(input("请输入三角形的三个边长:")),int(input("请输入三角形的三个边长:")),int(input("请输入三角形的三个边长:"))
# if a + b > c and a + c > b and b + c > a :   # 构成三角形的条件:三条边之和大于任意一条边
#     if a==b and b==c:
#         print(f"{a,b,c}等边三角形")
#     elif a==b or a==c or b==c :
#         print(f"{a,b,c}等腰三角形")
#     else :
#         print(f"{a,b,c}普通三角形")
# else :
#     print(f"{a,b,c}不构成三角形")
