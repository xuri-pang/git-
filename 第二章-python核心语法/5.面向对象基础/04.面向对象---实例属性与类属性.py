# 一.属性的分类
# 实例属性: 实例属性属于每个具体对象的属性,每个对象都是独立的 (各个对象特有的数据)
    # self.brand ---通过 实例对象.属性 的方式操作
# 类属性: 类属性是属于类本身的属性,所有实例共享的 (所有对象共享的数据或配置)
    # 放到与def同级别里 wheel = 4 ,不放到__init__方法中,因为在self是实例属性

# 说明: 通过实例查找属性时,会先查找实力树形,实例属性不存在时,再查找类属性

#---------------------------------------代码演示--------------------------------------------------
class Car:
    # 类属性 (所有实例对象共享的)
    wheel = 4
    tax_rate = 0.1  # 税率

    def __init__(self,c_color, c_brand,c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        self.tax_rate = 0.2
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

# 测试
c1 = Car("red","BWM","X5",1000000)
print(c1.brand)
print(c1.wheel)  # 查询类属性,可以通过实例对象来查类属性,但是会优先查找实例属性,实例属性不存在时再查找类属性
#------------------------------------------------------------------------------------------------