

# 模式匹配  match---case 语句
# 结构模式匹配就是用一个清晰的模板去精准的匹配数据的结构和内容,匹配成功则返回对应的结果,匹配失败则返回None
# 1.match---case语法
# match 表达式 :
#     case 模式1:
#         执行语句1
#     case 模式2:
#         执行语句2
#     case 模式3:
#         执行语句3
#     case _:  # _表示匹配其他所有情况    相当于else
#         执行语句4

# 2.match---case的应用场景    不能替代if判断
# match : 基于某个变量的多个固定值进行分支判断时,可以使用
# if :涉及复杂的逻辑判断判定时,可以使用


# 例子
# 工作日程安排
# day = input("请输入星期几(1~7):")
# if day == "1":
#     print("今天是周一")
# elif day == "2":
#     print("今天是周二")
# elif day == "3":
#     print("今天是周三")
# elif day == "4":
#     print("今天是周四")
# elif day == "5":
#     print("今天是周五")
# elif day == "6":
#     print("今天是周六")
# elif day == "7":
#     print("今天是周日")
# else :
#     print("输入的星期有误")

# 改后的
# Debug运行(也就是虫子模式)需要打断点否则是直接运行

# day = input("请输入星期几:")
# match day :
#     case "1":
#         print("今天是周一")
#     case "2":
#         print("今天是周二")
#     case "3":
#         print("今天是周三")
#     case "4":
#         print("今天是周四")
#     case "5":
#         print("今天是周五")
#     case "6":
#         print("今天是周六")
#     case "7":
#         print("今天是周日")
#     case _:  # _表示匹配其他所有情况    相当于else
#         print("输入的星期有误")

# 基于match---case实现一个简易的计算机,输入数字和运算符,返回结果
# case里可以加if判断

num1 = float(input("请输入数字1:"))
num2 = float(input("请输入数字2:"))
oper = input("请输入运算符(+ - * /) : ")

match oper :
    case "+" :
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-" :
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*" :
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")  #0不能做除数
    case _:
        print("输入的运算符有误")