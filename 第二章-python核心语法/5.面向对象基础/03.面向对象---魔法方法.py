# 一.魔法方法的介绍
# 魔法方法:是指python中提供的以双下划线开头和结尾的特殊方法,用于定义类的特殊行为,比如:__init__
# 魔法方法是不需要我们手动调用的,python会在合适的时机自动调用
# 常见的魔法方法:
# 1.__init__ : 构造方法,用于初始化对象
# 2.__str__ : 字符串方法,用于返回对象的描述信息
# 3.__eq__ : 比较两个对象是否相等(equal)
# 4.__lt__ , __le__ , __gt__ , __ge__ : 支持比较两个对象的大小(less than),小于等于(less than or equal),大于(greater than),大于等于(greater than or equal)

# -------------------------------代码演示-------------------------------------------
class Car:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    def running(self):
        print(f'{self.brand} {self.name} 正在高速行驶...')
    def __str__(self):  #定义了__str__方法后,print输出对象的时候,就会自动调用__str__方法
        return f'{self.brand} {self.name} {self.price}'  #转成字符串来输出出来
    def __eq__(self,other):  #定义了__eq__方法后,比较两个对象是否相等的时候,就会自动调用__eq__方法
        return self.price == other.price and self.brand == other.brand and self.name == other.name  #具体的比较方法由自己来决定
    def __lt__(self,other):  #定义了__lt__方法后,比较两个对象大小的时候,就会自动调用__lt__方法
        return self.price < other.price  #具体的比较方法由自己来决定


c1 = Car('BMW','X5',50000)
print(c1)                                    #默认输出出来的是对象的内存地址(16进制)
c2 = Car('BMW','X5',50000)
print(c2)

print(c1 == c2)   #False    #默认情况下,比较两个对象是否相等,比较的是两个对象的内存地址
print(c1 < c2)              #默认自定义的对象之间不可以进行大小比较,这就需要用定义魔法方法来比较
# --------------------------------------------------------------------------------


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
        return f"{self.color} {self.brand} {self.name} {self.price}"   # 具体的展示模式自己定制

    def __eq__(self, other):
        return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price

    def __lt__(self, other):
        return self.price < other.price
# 测试
c1 = Car("白色","BYD","汉",100000)
print(c1)
c2 = Car("白色","BYD","汉",100000)
print(c2)

print(c1 == c2)  # False

print(c1 < c2)
# --------------------------------------------------------------------------------