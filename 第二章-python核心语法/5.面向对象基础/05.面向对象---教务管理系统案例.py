# 一.案例
# 采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，控制台菜单与用户交互，具体的功能如下:
# 1.添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
# 2.修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
# 3.删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
# 4.查询指定学生成绩：根据输入的学生姓名，查找对应的学生，并输出
# 5.展示全部学生成绩：展示出系统中所有学生的成绩
from google.protobuf.text_format import PrintField
from lxml.html.builder import INPUT


# 二.思考
# 需要建学生类(Student)和教务系统类(EduMangement)
# 上面的案例都是教务系统的功能
# 修改学生成绩的是学生的操作

# 三.需求分析
# 1.添加学生信息,根据输入的学生姓名、语文成绩、数学成绩、英语成绩、记录在系统中
#     1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
#     1.2 检查学生姓名是否已存在，如果学生不存在，再添加（存在则，不添加）
#     1.3 验证成绩范围（0-100 分）
#     1.4 创建学生对象并添加到系统
# 2.修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
#     2.1 输入要修改的学生姓名
#     2.2 根据姓名查找该学生，显示该生当前成绩信息
#     2.3 输入新的语文、数学、英语成绩
#     2.4 更新学生成绩数据
# 3.删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
# 4.查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
#     4.1 输出格式为："姓名：张三 | 语文: 85 | 数学: 90 | 英语: 88 | 总分: 263"

# 三.报错问题
# 1.add_student---定义和调用传参不同, 例如:函数定义时写了 4 个参数，但是调用函数的时候，一个参数都没传，两边对不上，Python 直接报错。
#---------------------------------------代码演示--------------------------------------------------
# 1.学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name              # 赋值操作
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):                # 定义一个魔法方法来将输出结果转化为字符串----4.1
        return f"姓名:{self.name} | 语文成绩:{self.chinese} | 数学成绩:{self.math} | 英语成绩:{self.english} | 总分:{self.chinese + self.math + self.english }"
    # 修改学生的成绩
    def update_score(self,chinese=None, math=None, english=None):        # 设置默认值
        if chinese is not None:       # 判断传递的成绩是否为空,不空则传递---1.2
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

# 2.教务系统类
class EduManagement:
    system_version = "1.0"   # 类属性---版本信息
    system_name = "教务系统"   # 类属性---系统名称

    def __init__(self):
        self.student_list = []   # 初始化一个空列表，记录的是在校学生的成绩


    # 添加学生成绩
    def add_student(self):
        # 1.1 输入学生姓名、语文成绩、数学成绩、英语成绩

        name = input("请输入学生姓名:")

        # 1.2 判断学生姓名是否已存在，如果学生不存在，再添加（存在则，不添加）

        for s in self.student_list:       # 遍历出来的s就是学生student
            if s.name == name:        # 如果遍历出来的学生姓名和输入的学生姓名一样,则表示该学生已存在
                print("该学生已存在,添加失败,请重新输入")
                return                # 退出该函数,不往下执行

        chinese = int(input("请输入语文成绩:"))
        math = int(input("请输入数学成绩:"))
        english = int(input("请输入英语成绩:"))

        # 1.3 验证成绩范围（0-100 分）
        # 1.4 创建学生对象并添加到系统

        if 0 < chinese <= 100 and 0 < math <= 100 and 0 < english <= 100:    # 判断输入的成绩是否在0-100之间,如果不在,则提示输入错误
            stu = Student(name,chinese,math, english)                        # 1.4 创建学生对象并添加到系统
            self.student_list.append(stu)                                    # 将创建的学生对象添加到系统
            print("学生信息添加成功")
        else:
            print("输入的成绩有误,各科成绩必须在 0 ~ 100 之间 !")


    # 修改学生成绩
    def update_student(self):

        # 2.1 输入要修改的学生姓名
        name = input("请输入要修改的学生姓名:")

        # 2.2 根据学生姓名找到该学生的信息
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩:{s}")   # s 是上面遍历的信息

                chinese = int(input("请输入新的语文成绩:"))
                math = int(input("请输入新的数学成绩:"))
                english = int(input("请输入新的英语成绩:"))

                # 判断分数是否在 0~100 之间
                if 0 < chinese <= 100 and 0 < math <= 100 and 0 < english <= 100:  # 判断输入的成绩是否在0-100之间,如果不在,则提示输入错误
                    s.update_score(chinese, math, english)   # 修改学生成绩  update_sorce
                    print("学生信息修改成功")
                    print(f"修改后的学生成绩: {s}")
                    return    # 结束运行,后面的不在运行
                else:
                     print("输入的成绩有误,各科成绩必须在 0 ~ 100 之间 !")
                     return
        print("该学生不存在,请重新输入")   # 用来返回,学生没在学生表的情况的结果


    # 删除学生成绩
    def delete_student(self):
        name = input("请输入要删除的学生姓名:")

        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)    # 列表自带的方法
                print("学生信息删除成功")
                return
        print("该学生不存在,请重新输入")   # 用来返回,学生没在学生表的情况的结果


    # 查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名:")

        for s in self.student_list:
            if s.name == name:
                print(f"学生信息: {s}")
                return
        print("该学生不存在,请重新输入")   # 用来返回,学生没在学生表的情况的结果


    # 展示全部学生成绩
    def show_all(self):
        for s in self.student_list:
            print(f"学生信息: {s}")


    # 菜单
    def run(self):
        print(f"欢迎使用 {self.system_name} V{self.system_version}")

        while True:
            print()
            print("############## 教务管理系统 ################")
            print("#              1.添加学生                  #")
            print("#              2.修改学生                  #")
            print("#              3.删除学生                  #")
            print("#              4.查询学生                  #")
            print("#              5.展示所有学生               #")
            print("#              6.退出系统                  #")
            print("############## 教务管理系统 ################")

            choice = input("请输入你的选择:")
            match choice:
                case "1":  # 添加学生
                    self.add_student()
                case "2":  # 修改学生
                    self.update_student()
                case "3":  # 删除学生
                    self.delete_student()
                case "4":  # 查询学生
                    self.query_student()
                case "5":  # 展示所有学生
                    self.show_all()
                case "0":  # 退出系统
                    print("退出系统")
                    break
                case _:   # 其他
                    print("输入有误,请重新输入")



# 测试
# 只有直接运行当前这个 .py 文件的时候，才执行下面缩进里的代码；如果是别的文件导入这个文件，就不执行。
# 如果别的文件写 import 教务系统 把这个文件当成模块导入，此时 __name__ 就等于文件名，不等于__main__
# → if 条件不成立，里面代码不会自动跑起来，只导入 Student、ScoreSystem 类，不会直接弹出菜单

if __name__ == '__main__':    # __name__ 自动被赋值为字符串 '__main__'
    edu_management = EduManagement()
    edu_management.run()
# 2.教务系统类

#------------------------------------------------------------------------------------------------