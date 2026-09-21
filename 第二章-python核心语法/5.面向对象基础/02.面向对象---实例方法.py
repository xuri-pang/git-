# 一.类中定义实例方法
# 定义语法与之前学习的函数定义的方式是一致的
from functools import total_ordering


# 语法结构
# class 类名:
#     def __init__(self,参数1,参数2,...):
#         self.属性1 = 参数1
#         self.属性2 = 参数2

#     def __init__(self,形参列表):
#         ...

#     def __init__(self,参数1,形参列表):
#         ...

# 创建对象
# 对象名 = 类名(参数1,参数2,...)
# 对象名.方法名(实参)


# -------------------------------代码演示-------------------------------------------

class Car:
    def __init__(self,c_color, c_brand,c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕,对象属性已经添加完毕")

    def running(self):
        print(f"{self.brand}的{self.name} 正在速行驶...")

    def total_cost(self,discount,rate=0.1):              #rate可以设置默认值,这样等调用方法时不写这个参数也会运行
        """
        计算车的总价,包含两个部分:车的价格,税费
        :param discount:折扣
        :param rate:税率
        :return:提车的总费用
        """
        total_cost = self.price * discount + self.price * rate
        return total_cost
    # 魔法方法
    def __str__(self):
        return f"{self.color}的{self.brand} {self.name} {self.price}"
# 测试
c1 = Car("红色","奔驰","C200",500000)

#调用对象中的方法
c1.running()

total1 = c1.total_cost(0.9,0.05)
print("车的总价为:",total1)
total2 = c1.total_cost(0.9)
print("车的总价为:",total2)
# --------------------------------------------------------------------------------